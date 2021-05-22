YSmenu_themes
=============
My themes for YSmenu. YSmenu is a free (but closed-source) alternative *menu system / firmware* for R4 cartridges for Nintendo DS.

For more information, see articles on Wikipedia: 
[R4 cartridge](https://en.wikipedia.org/wiki/R4_cartridge), [Nintendo DS Lite](https://en.wikipedia.org/wiki/Nintendo_DS_Lite), [Nintendo DS](https://en.wikipedia.org/wiki/Nintendo_DS), [Nintendo DSi](https://en.wikipedia.org/wiki/Nintendo_DSi)

## Motivation

I bought "R4 SDHC 2020" on AliExpress. But I was disappointed with the original firmware because of the awful user interface and "timebomb feature". "Timebomb feature" causes failure of the firmware after five years! (So shameful!)  

I found out somebody canny modified an R4 firmware to boot directly to *YSmenu* to fix the "timebomb". But I couldn't find a theme I would be satisfied with...


## Links, tips

See ["How To Setup An R4 Card"](https://www.youtube.com/watch?v=7yTyDVl1ICc) video on YouTube describing how to install YSmenu to "R4 SDHC 2020". Link from the video to download YSmenu: ["R4 Card TimeBomb Fix.zip"](https://mega.nz/file/05sFxDiC#PrL6yFpo_qBgEXs3bixQTmHupjOu_wsCednBWwRGtSg)

You can buy a new R4 cartridge [on AliExpress](https://www.aliexpress.com/wholesale?catId=0&SearchText=R4+SDHC) or on eBay (At least now, in 2021).

See [Excellent ZX Spectrum emulator ZXDS written by Patrik Rak](http://zxds.raxoft.cz/)

"R4 SDHC 2021" (r4isdhc.com.cn) doesn't have a "timebomb". It also uses different R4 firmware (it requires file `_dsmenu.dat`). It works well with firmware "R4 Kernal" / "R4 Wood". 


## Theme installation

You can simply copy `YSmenu.ini`, `YSMenu2.bmp`, `YSMenu2.bmp` to `<your_SD_card>/TTmenu/`

If you have custom `YSmenu.ini` then *overwrite only sections* `[FILELIST]` and `[FILEINFO]`...


## YSmenu theme files

### `YSmenu.ini`

Color definitions are in the sections `[FILELIST]` and `[FILEINFO]`

`YSmenu.ini` uses color codes in a format "BGR15". For converting colors to this format, you can use my simple Python script `html2bgr15.py` For more information see source code or run:

    python3 html2bgr15.py --help 

### `YSMenu1.bmp` and `YSMenu2.bmp`

Background images. `YSMenu1.bmp` for the top and `YSMenu2.bmp` for the bottom screen.

Images have to be saved in the format:

![Do not write color space information, 24 bits color, R8 G8 B8](images/GIMP_export_bmp_.png)

