## For Developers

[Japanese](/README_dev_ja.md) [Russian](/README_dev_ru.md)

## Prerequisites

- Linux(ubuntu, debian) or WSL2, (not tested for other linux distributions and Mac)
- Anaconda

## Preparation

1. Create an Anaconda virtual environment

```
$ conda create -n vcclient-dev python=3.10
$ conda activate vcclient-dev
```

2. Clone the repository

```
$ git clone https://github.com/w-okada/voice-changer.git
```

## For Server Developer

1. Install requirements

```
$ cd voice-changer/server
$ pip install -r requirements.txt
```

2. Run the server

Start the server with the command below. Replace the paths to the model weights as needed.

```
$ python3 MMVCServerSIO.py -p 18888 --https true \
    --content_vec_500 pretrain/checkpoint_best_legacy_500.pt  \
    --content_vec_500_onnx pretrain/content_vec_500.onnx \
    --content_vec_500_onnx_on true \
    --hubert_base pretrain/hubert_base.pt \
    --hubert_base_jp pretrain/rinna_hubert_base_jp.pt \
    --hubert_soft pretrain/hubert/hubert-soft-0d54a1f4.pt \
    --nsf_hifigan pretrain/nsf_hifigan/model \
    --crepe_onnx_full pretrain/crepe_onnx_full.onnx \
    --crepe_onnx_tiny pretrain/crepe_onnx_tiny.onnx \
    --rmvpe pretrain/rmvpe.pt \
    --model_dir model_dir \
    --samples samples.json

```

Access the displayed URL with a browser (currently only Chrome is supported) to open the GUI.

2-1. Trouble shoot

(1) OSError: PortAudio library not found
If you encounter the message below, you should install additional libraries.

```
OSError: PortAudio library not found
```

Install the libraries with the following commands.

```
$ sudo apt-get install libportaudio2
$ sudo apt-get install libasound-dev
```

(2) It's not starting up!

The client does not start automatically. Launch your browser and open the URL displayed in the console.

(3) Could not load library libcudnn_cnn_infer.so.8

When using WSL, you might see `Could not load library libcudnn_cnn_infer.so.8. Error: libcuda.so: cannot open shared object file: No such file or directory`. This usually means the path isn't set correctly. Set the path as shown below; adding it to your startup script such as `.bashrc` may help.

```
export LD_LIBRARY_PATH=/usr/lib/wsl/lib:$LD_LIBRARY_PATH
```

- reference
  - https://qiita.com/cacaoMath/items/811146342946cdde5b83
  - https://github.com/microsoft/WSL/issues/8587

3. Enjoy developing.

### Appendix

1. Win + Anaconda (not supported)

use conda to install pytorch

```
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
```

Also run these commands.

```
pip install chardet
pip install numpy==1.24.0
```

## For Client Developer

1. Import modules and initial build

```
cd client
cd lib
npm install
npm run build:dev
cd ../demo
npm install
npm run build:dev
```

2. Enjoy developing.
