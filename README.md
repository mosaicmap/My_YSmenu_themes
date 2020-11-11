YSmenu_themes
=============
My themes for YSmenu. YSmenu is an alternative free (but closed-source) firmware for R4 cartridges for game handhelds Nintendo DS.

TODO

For more information, see articles:  
[Nintendo DS Lite on Wikipedia](https://en.wikipedia.org/wiki/Nintendo_DS_Lite) and 
[R4 cartridge on Wikipedia](https://en.wikipedia.org/wiki/R4_cartridge)

## Theme installation

You can simply copy `YSmenu.ini`, `YSMenu2.bmp`, `YSMenu2.bmp` to `<SD_card>/TTmenu/`

If you have custom `YSmenu.ini` then overwrite only sections `[FILELIST]` and `[FILEINFO]`

## Tips

See [Excellent ZX Spectrum emulator ZXDS written by Patrik Rak](http://zxds.raxoft.cz/)

You can buy "R4 SDHC" card on eBay or AliExpress (now, 2020).

## YSmenu theme

`YSmenu.ini` code colors are in an uncommon format BGR15. For converting colors to this format, you can use my simple Python script `html2bgr15.py` For more information:

    python3 html2bgr15.py --help 

`YSMenu*.bmp` images have to be saved in the format:

![Do not write color space information, 24 bits color, R8 G8 B8](screenshots/GIMP_export_bmp_.png)

