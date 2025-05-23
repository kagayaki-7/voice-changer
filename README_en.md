## VC Client

[Japanese](/README_ja.md) [Korean](/README_ko.md) [Russian](/README_ru.md)

## What's New!
- We have released a sister product, the Text-to-Speech client.
  - Voice generation can be enjoyed through a simple interface.
  - For more details, click [here](https://github.com/w-okada/ttsclient).
- Beatrice V2 Training Code Released!!!
  - [Training Code Repository](https://huggingface.co/fierce-cats/beatrice-trainer)
  - [Colab Version](https://github.com/w-okada/beatrice-trainer-colab)
- v.2.0.70-beta (only for m1 mac)
  - [HERE](https://github.com/w-okada/voice-changer/tree/v.2)
  - new feature:
    - The M1 Mac version of VCClient now supports Beatrice v2 beta.1.
- v.2.0.69-beta (only for win)
  - [HERE](https://github.com/w-okada/voice-changer/tree/v.2)
  - bugfix:
    - Fixed a bug where the start button would not be displayed in case of some exceptions
    - Adjusted the output buffer for server device mode
    - Fixed a bug where the sampling rate would change when settings were modified while using server device mode
    - Fixed a bug when using Japanese hubert
  - misc:
    - Added host API filter (highlighted) for server device mode
- v.2.0.65-beta
  - [HERE](https://github.com/w-okada/voice-changer/tree/v.2)
  - new feature: We have supported Beatrice v2 beta.1, enabling even higher quality voice conversion.

# What is VC Client

1. This software performs real-time voice conversion using several Voice Conversion (VC) AIs. The supported methods are listed below.

- [MMVC](https://github.com/isletennos/MMVC_Trainer) (only v1)
- [so-vits-svc](https://github.com/svc-develop-team/so-vits-svc) (only v1)
- [RVC(Retrieval-based-Voice-Conversion)](https://github.com/liujing04/Retrieval-based-Voice-Conversion-WebUI)
- [DDSP-SVC](https://github.com/yxlllc/DDSP-SVC) (only v1)
- [Beatrice JVS Corpus Edition](https://prj-beatrice.com/) * experimental,  (***NOT MIT License*** see [readme](https://github.com/w-okada/voice-changer/blob/master/server/voice_changer/Beatrice/))
  - [Beatrice v2](https://prj-beatrice.com/) (only for v2)

1. Distribute the processing load by running Voice Changer on another PC.
   The application works in a server–client configuration. Running the MMVC server on a different machine reduces the impact on resource-intensive tasks such as game streaming.

![image](https://user-images.githubusercontent.com/48346627/206640768-53f6052d-0a96-403b-a06c-6714a0b7471d.png)

3. Platform
   Supports Mac (Apple Silicon) only.
## Related Software
- [Real-time Voice Changer VCClient](https://github.com/w-okada/voice-changer)
- [Text-to-Speech Software TTSClient](https://github.com/w-okada/ttsclient)
- [Real-Time Speech Recognition Software ASRClient](https://github.com/w-okada/asrclient)
# usage

This application performs voice conversion with MMVC and so-vits-svc.

You can use it in two primary ways, ordered by difficulty:

- Using a pre-built binary
- Setting up an environment with Docker or Anaconda and using it

## (1) Usage with pre-built binaries

- You can download and run executable binaries.

- Please see [here](tutorials/tutorial_rvc_en_latest.md) for the tutorial. ([trouble shoot](https://github.com/w-okada/voice-changer/blob/master/tutorials/trouble_shoot_communication_ja.md))

- It's now easy to try it out on [Google Colaboratory](https://github.com/w-okada/voice-changer/tree/v.2/w_okada's_Voice_Changer_version_2_x.ipynb) (requires a ngrok account). You can launch it from the 'Open in Colab' button in the top left corner.

<img src="https://github.com/w-okada/voice-changer/assets/48346627/3f092e2d-6834-42f6-bbfd-7d389111604e" width="400" height="150">

- We offer a Mac version on [hugging face](https://huggingface.co/wok000/vcclient000/tree/main)
- v2 for Mac (Apple Silicon)
    - Please download and use `vcclient_mac_xxx.zip`.
    - To leverage the Apple Silicon GPU, install PyTorch with [MPS support](https://pytorch.org/docs/stable/notes/mps.html) and set the device to `mps` in your Python environment.
    - If CPU usage is high or audio becomes choppy, increase **CHUNK** (e.g. 1024) and set **F0 Det** to `dio` in the GUI.
    - For lower resource usage, you can try the [Light VCClient for Beatrice v2](https://huggingface.co/wok000/light_vcclient_beatrice/tree/main).
- For the Mac version, after unzipping the file, double-click `startHttp.command`. If you see a warning that the developer cannot be verified, hold the Control key and click again (or right-click).
- If connecting remotely, use the `.command` file (Mac) with HTTPS instead of HTTP.
 - If you are connecting remotely, please use the `.command` file with https instead of http.

- The encoder of DDPS-SVC only supports hubert-soft.

- [Download from hugging face](https://huggingface.co/wok000/vcclient000/tree/main)

## (2) Usage after setting up the environment such as Docker or Anaconda

Clone this repository and use it. On Mac, setting up Python virtual environments such as Anaconda is necessary. **<font color="red"> Even without a GPU, it may work well enough with a reasonably new CPU </font>(refer to the section on real-time performance below)**.

To run docker, see [start docker](docker_vcclient/README_en.md).

To run on Anaconda venv, see [server developer's guide](README_dev_en.md)


# Software Signing

This software is not signed by the developer. macOS may display a warning, but you can run the application by holding the Control key and clicking the icon (or by right-clicking). This behavior is due to Apple's security policy. Use the software at your own risk.

![image](https://user-images.githubusercontent.com/48346627/212567711-c4a8d599-e24c-4fa3-8145-a5df7211f023.png)

https://user-images.githubusercontent.com/48346627/212569645-e30b7f4e-079d-4504-8cf8-7816c5f40b00.mp4

# Acknowledgments

- [Tachizunda-mon materials](https://seiga.nicovideo.jp/seiga/im10792934)
- [Irasutoya](https://www.irasutoya.com/)
- [Tsukuyomi-chan](https://tyc.rei-yumesaki.net)

> This software uses the voice data of the free material character "Tsukuyomi-chan," which is provided for free by CV. Yumesaki Rei.
>
> - Tsukuyomi-chan Corpus (CV. Yumesaki Rei)
>
> https://tyc.rei-yumesaki.net/material/corpus/
>
> Copyright. Rei Yumesaki

- [Amitaro's Onsozai kobo](https://amitaro.net/)
- [Replica doll](https://kikyohiroto1227.wixsite.com/kikoto-utau)

# Terms of Use

In accordance with the Tsukuyomi-chan Corpus Terms of Use for the Tsukuyomi-chan Real-time Voice Changer, the use of the converted voice for the following purposes is prohibited.

- Criticizing or attacking individuals (the definition of "criticizing or attacking" is based on the Tsukuyomi-chan character license).

- Advocating for or opposing specific political positions, religions, or ideologies.

- Publicly displaying strongly stimulating expressions without proper zoning.

- Publicly disclosing secondary use (use as materials) for others.
  (Distributing or selling as a work for viewing is not a problem.)

Regarding the Real-time Voice Changer Amitaro, the following uses are prohibited in accordance with the terms of use of Amitaro's koe-sozai kobo. [Details](https://amitaro.net/voice/faq/#index_id6)

Regarding the Real-time Voice Changer Kikoto Mahiro, the following uses are prohibited in accordance with the terms of use of Replica Doll. [Details](https://kikyohiroto1227.wixsite.com/kikoto-utau/ter%EF%BD%8Ds-of-service)

# Disclaimer

We are not liable for any direct, indirect, consequential, incidental, or special damages arising out of or in any way connected with the use or inability to use this software.
