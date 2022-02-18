YSmenu_themes
=============
My themes for YSmenu. YSmenu is a free (but closed-source) alternative *menu system / firmware* for R4 cartridges for Nintendo DS ([Nintendo DS Lite](https://en.wikipedia.org/wiki/Nintendo_DS_Lite), [Nintendo DS](https://en.wikipedia.org/wiki/Nintendo_DS), [Nintendo DSi](https://en.wikipedia.org/wiki/Nintendo_DSi)).

For more information about YSmenu see [YSMenu on gamebrew.org](https://www.gamebrew.org/wiki/YSMenu) and [YSMenu on gbatemp.net](https://wiki.gbatemp.net/wiki/YSMenu)

For more information about R4, see articles on Wikipedia: 
[R4 cartridge](https://en.wikipedia.org/wiki/R4_cartridge), [R4i_SDHC](https://en.wikipedia.org/wiki/List_of_Nintendo_DS_and_3DS_flash_cartridges#R4i_3DS_and_R4i_SDHC)


## Motivation

I bought "R4 SDHC 2020" on AliExpress. But I was disappointed with the original firmware because of the awful user interface and moreover, I found out it has a "timebomb feature". The "Timebomb feature" causes a "failure" of the firmware after five years! So shameful!

I found out somebody clever modified an R4 firmware to boot directly to the *YSmenu* to fix the "timebomb". 

But I couldn't find a YSmenu theme I would be satisfied with...


## YSmenu installation

See ["How To Setup An R4 Card"](https://www.youtube.com/watch?v=7yTyDVl1ICc) video on YouTube describing how to install YSmenu to "R4 SDHC 2020". Link from the video to download YSmenu: ["R4 Card TimeBomb Fix.zip"](https://mega.nz/file/05sFxDiC#PrL6yFpo_qBgEXs3bixQTmHupjOu_wsCednBWwRGtSg)
Or an alternative video: ["How to Install YSMenu on your DS Flashcart"](https://www.youtube.com/watch?v=9_mnV4ZbUF0) And link to get YSmenu: ["YSmenu.7z"](https://drive.google.com/file/d/14pcOGd-O9zYMVxO0JpK5QQjjwRvMqldc/view))

[YSmenu "multi-cart-update"](https://gbatemp.net/download/retrogamefan-multi-cart-update.35737/)


## Theme installation

You can simply copy `YSmenu.ini`, `YSMenu2.bmp`, `YSMenu2.bmp` to `<your_SD_card>/TTmenu/`

If you have custom `YSmenu.ini` then *overwrite only sections* `[FILELIST]` and `[FILEINFO]`...


## YSmenu theme files

### `YSmenu.ini`

Color definitions are in the sections `[FILELIST]` and `[FILEINFO]`

`YSmenu.ini` uses color codes in a format "BGR15". For converting colors to this format, you can use my simple Python script `html2bgr15.py` For more information see source code or run:

    python3 html2bgr15.py --help 
    
Alternatively, there is an [online converter http://www.conradshome.com/html2bgr15/](http://www.conradshome.com/html2bgr15/)

### `YSMenu1.bmp` and `YSMenu2.bmp`

Background images. `YSMenu1.bmp` for the top and `YSMenu2.bmp` for the bottom screen.

Images have to be saved in the format:

- write without color space information
- 24 bits color - R8 G8 B8

![Do not write color space information, 24 bits color, R8 G8 B8](images/GIMP_export_bmp_.png)


## Another links; tips

[flashcard-archive](https://github.com/DS-Homebrew/flashcard-archive)

[YSmenu "multi-cart-update"](https://gbatemp.net/download/retrogamefan-multi-cart-update.35737/)

[Excellent ZX Spectrum emulator ZXDS written by Patrik Rak](http://zxds.raxoft.cz/)

You can buy a new R4 cartridge [on AliExpress](https://www.aliexpress.com/wholesale?catId=0&SearchText=R4+SDHC) or on eBay (At least now, in 2022).

Some cheaper R4s (older versions?) from AliExpress use a different R4 firmware. They require file `_dsmenu.dat` or `_ds_menu.dat`. They usually work well with firmware "R4 Kernal" or "R4 Wood" and they have no "timebomb feature" (as far as I know).

