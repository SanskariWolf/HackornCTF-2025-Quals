In the instance source code i found this comment

```
<!--
To: localh0ste (System Admin)
Hi System Admin,  
Please update the webpage. I couldn’t upload it as I’m away on holidays this week.
I’ll share my credentials for a temporary shares(SMB) account — please use it only for this update.
After use, please disable PS Remoting as we discussed on the call.
Thanks
BSides Noida
Development Team
Sneha
Credentials:
developer:C|>@|#v863u)zl9G^&4}8kHl
-->
```

this hints that The comment also alluded to a temporary SMB share and the need to disable PS Remoting, strongly suggesting that both the SMB and WinRM services are active.


therefore i tried connecting with Credentials: developer:C|>@|#v863u)zl9G^&4}8kHl
```evil-winrm -i 13.71.126.207 -u 'developer' -p 'C|>@|#v863u)zl9G^&4}8kHl'```

but failed badly, 

```
──(sanskariwolf㉿sanskariwolf)-[~/Documents/CTFs/HackornCTF 2025 Quals/Pwn]
└─$ # In your attacker machine's terminal
evil-winrm -i 13.71.126.207 -u 'developer'
Enter Password: 
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
ls
                                        
Error: An error of type HTTPClient::ConnectTimeoutError happened, message is execution expired
                                        
Error: Exiting with code 1
```
                                                            

stuggled over 15-20 minutes over the issue that windows might be blocking the connection or my wsl is having problems.(Ai is cool u know)

i left evil-winrm then, 
went with smbclient

```
sanskariwolf@SanskariWolf:/mnt/c/Users/tanus$ smbclient -L //13.71.126.207 -U developer
Password for [WORKGROUP\developer]:

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        flag            Disk      BSides Noida - Initial Foothold
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share
        SYSVOL          Disk      Logon server share
        Users           Disk
SMB1 disabled -- no workgroup available
sanskariwolf@SanskariWolf:/mnt/c/Users/tanus$
```

tried the workgroup flag

```
sanskariwolf@SanskariWolf:/mnt/c/Users/tanus$ smbclient //13.71.126.207/flag -U developer
Password for [WORKGROUP\developer]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Sep 23 09:22:41 2025
  ..                                 DR        0  Tue Sep 23 11:30:40 2025
  flag.txt                            A      202  Tue Sep 23 09:28:17 2025

                33147379 blocks of size 4096. 28713691 blocks available
smb: \>
```

with the commaand ```more flag.txt``` read the file and got svc-flag credentials

```
Hello Participant,
Nice to See You here ;

Your Credentitals  :

svc-flag:2<wN5cf4Zhu£mr!tP"5*,4v]

{Hint: PS Remoting can sometimes be useful for gaining an initial foothold.}
@localh0ste
/tmp/smbmore.s5aIjF (END)
```

Credentitals : svc-flag:2<wN5cf4Zhu£mr!tP"5*,4v]

I tried connecting with the new credentails

```
sanskariwolf@SanskariWolf:/mnt/c/Users/tanus$ smbclient //13.71.126.207/flag -U svc-flag
Password for [WORKGROUP\svc-flag]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Sep 23 09:22:41 2025
  ..                                 DR        0  Tue Sep 23 11:30:40 2025
  flag.txt                            A      202  Tue Sep 23 09:28:17 2025

                33147379 blocks of size 4096. 28713692 blocks available
smb: \> more flag.txt
getting file \flag.txt of size 202 as /tmp/smbmore.W8EFGM (1.4 KiloBytes/sec) (average 1.4 KiloBytes/sec)
smb: \> cd .
smb: \> cd ..
smb: \> ls
  .                                   D        0  Tue Sep 23 09:22:41 2025
  ..                                 DR        0  Tue Sep 23 11:30:40 2025
  flag.txt                            A      202  Tue Sep 23 09:28:17 2025

                33147379 blocks of size 4096. 28713691 blocks available
smb: \> cd ..
smb: \> ls
  .                                   D        0  Tue Sep 23 09:22:41 2025
  ..                                 DR        0  Tue Sep 23 11:30:40 2025
  flag.txt                            A      202  Tue Sep 23 09:28:17 2025

                33147379 blocks of size 4096. 28713691 blocks available
smb: \>
```

i found myself getting the same flag.txt so i spend 10-15 minutes trying things

Eventually tried Users workgroup,

```
sanskariwolf@SanskariWolf:/mnt/c/Users/tanus$ smbclient //13.71.126.207/Users -U svc-flag
Password for [WORKGROUP\svc-flag]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                  DR        0  Thu Sep 25 20:36:44 2025
  ..                                DHS        0  Thu Sep 25 20:36:39 2025
  0xC0de                              D        0  Thu Sep 25 15:24:42 2025
  admin-test                          D        0  Thu Sep 25 11:20:34 2025
  All Users                       DHSrn        0  Sat May  8 14:04:03 2021
  BSN-F                               D        0  Tue Sep 23 11:02:26 2025
  Default                           DHR        0  Wed Sep  3 17:15:35 2025
  Default User                    DHSrn        0  Sat May  8 14:04:03 2021
  desktop.ini                       AHS      174  Sat May  8 13:48:31 2021
  evil                                D        0  Thu Sep 25 12:15:42 2025
  file.txt                            A      145  Tue Sep 23 11:36:22 2025
  gobey                               D        0  Thu Sep 25 14:14:32 2025
  grin                                D        0  Thu Sep 25 11:48:46 2025
  hacker                              D        0  Thu Sep 25 08:32:39 2025
  localh0ste                          D        0  Mon Sep 22 20:52:23 2025
  Public                             DR        0  Wed Sep  3 17:15:55 2025
  svc-flag                            D        0  Thu Sep 25 20:04:41 2025

                33147379 blocks of size 4096. 28712634 blocks available
smb: \>
```

went inside svc-flag directory

```cd svc-flag``` or was is hacker one or file.txt has it, i don't remember

and i guess there i found the flag. Currently the challenge is down therefore can't try get the exact steps but this was the final go-through, traversing across directories, and one can find the flag. 