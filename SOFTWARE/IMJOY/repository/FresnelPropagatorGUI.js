<script lang="javascript">
class ImJoyPlugin {
  async setup() {

    // bind predict() to the button
    const processBtn = document.getElementById('predict-btn');
    processBtn.onclick = ()=>{
      this.predict()
    }

    // Display image when a file is selected.
    const fileInput = document.getElementById("file-input");
    const canvas = document.getElementById("input-canvas");
    const drawImage = (url, callback)=>{
        var img = new Image()
        img.crossOrigin = "anonymous"
        img.onload = function(){
            const ctx = canvas.getContext("2d");
            canvas.width = Math.min(this.width, 512);
            canvas.height= Math.min(this.height, parseInt(512*this.height/this.width), 1024);
            // draw the img into canvas
            ctx.drawImage(this, 0, 0, canvas.width, canvas.height);
            if(callback) callback();
        }
        img.src = url;
    }

    //load a preset image

    drawImage('https://raw.githubusercontent.com/bionanoimaging/UC2-GIT/master/WORKSHOP/INLINE-HOLOGRAMM/PYTHON/hologram_mouse.jpg')

    const readImageFile = ()=>{
        return new Promise((resolve, reject)=>{
            const U = window.URL || window.webkitURL;
            // this works for safari
            if(U.createObjectURL){
                drawImage(U.createObjectURL(fileInput.files[0]), resolve)
            }
            // fallback
            else{
                var fr = new FileReader();
                // when image is loaded, set the src of the image where you want to display it
                fr.onload = function(e) {
                    drawImage(e.target.result, resolve)
                };
                fr.onerror = reject
                // fill fr with image data
                fr.readAsDataURL(fileInput.files[0]);
            }
        })
    }

    // If user selected a new file or take a new photo, load it and do prediction.
    fileInput.addEventListener("change", ()=>{
      readImageFile().then((base64_url)=>{
          const pluginB = api.getPlugin('pluginB')
          pluginB.process_hologram(base64_url)
      })
    }, true);



    document.getElementById("hero_title").innerHTML = 'Model loaded'
    statusElement.innerHTML = '1. Open image (.png/.jpg) or use pre-loaded image. <br> 2. Click `Compute` to refocus the image!';

    // Display the predict button and file selection
    processBtn.style.display = "inline";
    fileInput.style.display = "inline";
  }


}
