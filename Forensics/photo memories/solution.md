I did the following analysis, command runs and tools,

```
                                                                                                                    
┌──(sanskariwolf㉿sanskariwolf)-[~/…/CTFs/HackornCTF 2025 Quals/Forensics/photo memories]
└─$ file bill_harper.jpg 
bill_harper.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 96x96, segment length 16, baseline, precision 8, 1280x720, components 3
                                                                                                                    
┌──(sanskariwolf㉿sanskariwolf)-[~/…/CTFs/HackornCTF 2025 Quals/Forensics/photo memories]
└─$ exiftool bill_harper.jpg 
ExifTool Version Number         : 13.25
File Name                       : bill_harper.jpg
Directory                       : .
File Size                       : 282 kB
File Modification Date/Time     : 2025:09:12 12:31:46+05:30
File Access Date/Time           : 2025:09:26 15:51:46+05:30
File Inode Change Date/Time     : 2025:09:25 12:51:48+05:30
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 96
Y Resolution                    : 96
Image Width                     : 1280
Image Height                    : 720
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 1280x720
Megapixels                      : 0.922
                                                                                                                    
┌──(sanskariwolf㉿sanskariwolf)-[~/…/CTFs/HackornCTF 2025 Quals/Forensics/photo memories]
└─$ binwalk bill_harper.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01

                                                                                                                    
┌──(sanskariwolf㉿sanskariwolf)-[~/…/CTFs/HackornCTF 2025 Quals/Forensics/photo memories]
└─$ 
```
Ran Stegseek
```
┌──(sanskariwolf㉿sanskariwolf)-[~/…/CTFs/HackornCTF 2025 Quals/Forensics/photo memories]
└─$ stegseek bill_harper.jpg 
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: ""
[i] Original filename: "secret.txt".
[i] Extracting to "bill_harper.jpg.out".

                                                                                                                    
┌──(sanskariwolf㉿sanskariwolf)-[~/…/CTFs/HackornCTF 2025 Quals/Forensics/photo memories]
└─$ strings bill_harper.jpg.out 
SPL{2dfa898b8659508904d0c321d3139e4885a441442d7b587e938b31fa84e0d678}
                                                                                                                    
┌──(sanskariwolf㉿sanskariwolf)-[~/…/CTFs/HackornCTF 2025 Quals/Forensics/photo memories]
└─$ 
```



Upon running strings one can get this
```
SOi7t
i+-t]z+v
ZU8 
SPL{eeff11779250b3bc2b7ac074f86bd1d7}
```
But it's a fake flag


```Flag - SPL{2dfa898b8659508904d0c321d3139e4885a441442d7b587e938b31fa84e0d678}```