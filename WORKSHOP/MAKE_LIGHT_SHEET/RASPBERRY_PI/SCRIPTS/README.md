# Small Scripts to help setting-up or fix your RasPi

## Fixing the date-error
Typically Linux refuses to get new updates or even access to internet if time-settings are heavily wrong. If adding ntp as well as ntpd services to invoke auto-time-synchronization does not work for you, we offer a small script to [make the input handyhere](./FIX_date).
1. If you got here from setting up the RasPi the first time and updates are not working then do the following:
    *   Download the [date_manfix script](./FIX_date/date_manfix.py) and save in Downloads-directory.
    *   Open a terminal and type:
        ```
        $ python3 Downloads/date_manfix.py
        ```
        and follow the instructions.
2. **After UC2env is setup** If you want to longterm avoid any such problems ...will be explained soon.
