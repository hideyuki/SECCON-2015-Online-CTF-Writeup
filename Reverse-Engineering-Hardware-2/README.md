## Reverse-Engineering Hardware 2

### 設問
我々は2つの74HC161を使ったエンコーダーボードによるバイナリを入手した。  
復元を手伝ってほしい。  

gpio2.py  
encripted  
counterhardware.zip  

### 答え

```
$ ./gpio2_sim.py encripted output.gz
$ gunzip output.gz
$ cat output
The flag is SECCON{7xgxUbQYixmiJAvtniHF}.
```





