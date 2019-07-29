#include <Arduino.h>
#include <Wire.h>
#include <string.h>
#include <StepMotor.h>
#include <TimerObject.h>
#include <SPI.h>

#define SLAVE_ADDRESS 0x08
#define CLOCK_FREQUENCY 100000 //choose according to frequency of I2C-Master
#define HEARTBEAT_INTERVAL 300000
#define LED 13
#define LEDARR_PIN 13
#define MAX_MSG_LEN 32
#define MAX_INST 10

typedef int (*callback)(int, int);

const char *delim_strt = "*";
const char *delim_stop = "#";
const char *delim_cmds = ";";
const char *delim_inst = "+";
const char *delim_tbc = "...";
int delim_strt_len;
int delim_stop_len;
int delim_tbc_len;
char *ptr_strt = NULL;
char *ptr_stop = NULL;

//User-defined commands
char msg[7];


//Device Identifier
const char *DEVICE_ID = "MOTORS";

const int nCommands = 3;
const char *COMMANDSET[nCommands] = {"DRVX", "DRVY", "DRVZ"};
const char *INSTRUCTS[nCommands] = {"1", "1", "1"};

const int nComCMDs = 4;
const char *COM_CMDS[nComCMDs] = {"STATUS", "LOGOFF", "NAME", "ANNOUNCE"};

char busy_msg[7];

char receiveBuffer[MAX_MSG_LEN];
char sendBuffer[MAX_MSG_LEN];

char CMD[MAX_MSG_LEN];
int INST[MAX_INST];
char instBuffer[MAX_INST];

const int outBufLen = MAX_MSG_LEN * 4;
char outBuffer[outBufLen];

const size_t max_msg_size = sizeof(sendBuffer);

//flag to escape Wire-library callback-function (less error-prone)
volatile boolean receiveFlag = false;

//custom flags
bool registered = false;
volatile bool busy = false;

//Arduino devices
StepMotor stepperX = StepMotor(2, 3, 4, 5);
StepMotor stepperY = StepMotor(10, 11, 12, 13);
StepMotor stepperZ = StepMotor(6, 7, 8, 9);

//look up specific task to according user-defined command
void executeCommand(int nINST)
{
  if (strcmp(CMD, COM_CMDS[0]) == 0)
  {
    const char *response = registered ? "registered" : "not registered";
    strlcat(outBuffer, response, outBufLen);
  }
  else if (strcmp(CMD, COM_CMDS[1]) == 0)
  {
    strlcat(outBuffer, "Received LOGOFF.", outBufLen);
    registered = false;
  }
  else if (strcmp(CMD, COM_CMDS[2]) == 0)
  {
    strlcat(outBuffer, DEVICE_ID, outBufLen);
  }
  else if (strcmp(CMD, COM_CMDS[3]) == 0)
  {
    if (!registered)
    {
      announce();
      registered = true;
    }
  }

  else if (strcmp(CMD, COMMANDSET[0]) == 0)
  {
    strlcat(outBuffer, "Pressed DRVX. Number of steps is: ", outBufLen);
    strlcat(outBuffer, msg, outBufLen);
    stepperX.Move(INST[0]);
  }
  else if (strcmp(CMD, COMMANDSET[1]) == 0)
  {
    strlcat(outBuffer, "Pressed DRVY. Number of steps is: ", outBufLen);
    strlcat(outBuffer, msg, outBufLen);
    stepperY.Move(INST[0]);
  }
  else if (strcmp(CMD, COMMANDSET[2]) == 0)
  {
    strlcat(outBuffer, "Pressed DRVZ. Number of steps is: ", outBufLen);
    strlcat(outBuffer, msg, outBufLen);
    stepperZ.Move(INST[0]);
  }
  else
  {
    strlcat(outBuffer, "Command not found.", outBufLen);
  }
}

void setup()
{
  pinMode(LED, OUTPUT);
  //Wire-library callbacks
  Wire.begin(SLAVE_ADDRESS);
  Wire.setClock(CLOCK_FREQUENCY);
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);

  memset(receiveBuffer, 0, max_msg_size);
  memset(sendBuffer, 0, max_msg_size);
  memset(outBuffer, 0, sizeof(outBuffer));

  delim_strt_len = (int)strlen(delim_strt);
  delim_stop_len = (int)strlen(delim_stop);
  delim_tbc_len = (int)strlen(delim_tbc);

  strlcat(busy_msg, delim_strt, sizeof(busy_msg));
  strlcat(busy_msg, "BUSY", sizeof(busy_msg));
  strlcat(busy_msg, delim_stop, sizeof(busy_msg));
}

void loop()
{
  if (receiveFlag)
  {
    busy = true;
    int nINST = separateCommand();
    executeCommand(nINST);
    cleanUpReceive();
    busy = false;
    receiveFlag = false;
  }
}

//request callback of Wire-library
void requestEvent()
{
  if (!busy)
  {
    prepareSend();
    Wire.write(sendBuffer);
    memset(sendBuffer, 0, max_msg_size);
  }
  else
  {
    Wire.write(busy_msg);
  }
}

//receive callback for incoming data of Wire-library
void receiveEvent(int byteCount)
{
  Wire.readBytes(receiveBuffer, byteCount);
  receiveFlag = byteCount > 1;
}

void cleanUpReceive()
{
  memset(CMD, 0, max_msg_size);
  memset(INST, 0, 10);
  memset(receiveBuffer, 0, max_msg_size);
}
void cleanUpRequest()
{
  memset(outBuffer, 0, sizeof(outBuffer));
  memset(sendBuffer, 0, max_msg_size);
}

int separateCommand()
{
  int count = 0;
  ptr_strt = strstr(receiveBuffer, delim_strt);
  ptr_stop = strstr(receiveBuffer, delim_stop);
  if ((ptr_strt != NULL) && (ptr_stop != NULL))
  {
    int len = ptr_stop - ptr_strt - 1;
    memcpy(CMD, ptr_strt + 1, len);
    CMD[len] = '\0';

    char *ptr_inst = NULL;
    ptr_inst = strstr(receiveBuffer, delim_inst);

    if (ptr_inst != NULL)
    {
      len = ptr_inst - ptr_strt - 1;
      CMD[len] = '\0';

      while (ptr_inst != ptr_stop)
      {
        ptr_strt = ptr_inst;
        ptr_inst = strstr(ptr_strt + 1, delim_inst);
        if (!ptr_inst)
          ptr_inst = ptr_stop;
        len = ptr_inst - ptr_strt - 1;
        if (len < MAX_INST)
        {
          memcpy(instBuffer, ptr_strt + 1, len);
          instBuffer[len] = '\0';
          INST[count] = atoi(instBuffer);
        }
        count++;
      }
    }
  }
  return count;
}

//fill outBuffer to make slave-device and its commands known to I2C-master
void announce()
{
  for (int i = 0; i < nCommands; i++)
  {
    strlcat(outBuffer, COMMANDSET[i], outBufLen);
    strlcat(outBuffer, delim_inst, outBufLen);
    strlcat(outBuffer, INSTRUCTS[i], outBufLen);
    strlcat(outBuffer, delim_cmds, outBufLen);
  }
}

int numberOfSends()
{
  int offset = delim_strt_len + delim_stop_len;
  int n = (int)strlen(outBuffer) / (MAX_MSG_LEN - offset);
  return n + 1;
}

void prepareSend()
{
  int n = numberOfSends();
  strlcat(sendBuffer, delim_strt, MAX_MSG_LEN);
  if (n > 1)
  {
    int bound = MAX_MSG_LEN - delim_strt_len - delim_tbc_len;
    strlcat(sendBuffer, outBuffer, bound);
    strlcat(sendBuffer, delim_tbc, MAX_MSG_LEN);
    shiftOutBuffer(bound - delim_strt_len - 1);
  }
  else
  {
    strlcat(sendBuffer, outBuffer, MAX_MSG_LEN);
    memset(outBuffer, 0, outBufLen);
  }
  strlcat(sendBuffer, delim_stop, MAX_MSG_LEN);
}

void shiftOutBuffer(int shiftLength)
{
  if (shiftLength >= (int)strlen(outBuffer))
  {
    memset(outBuffer, 0, sizeof(outBuffer));
  }
  else
  {
    for (int i = 0; i < (outBufLen - shiftLength); i++)
    {
      outBuffer[i] = outBuffer[i + shiftLength];
    }
  }
}

int countInstructions()
{
  int n = 10;
  int count;
  char *p = receiveBuffer;
  for (count = 0; count <= n; count++)
  {
    p = strstr(p, delim_inst);
    if (!p)
      break;
    p++;
  }
  return count;
}
