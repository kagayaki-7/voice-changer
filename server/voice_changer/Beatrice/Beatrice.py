from data.ModelSlot import BeatriceModelSlot
import gc
import torch
from mods.log_control import VoiceChangaerLogger

from voice_changer.utils.VoiceChangerModel import AudioInOut, VoiceChangerModel
from voice_changer.utils.VoiceChangerParams import VoiceChangerParams


logger = VoiceChangaerLogger.get_instance().getLogger()


class Beatrice(VoiceChangerModel):
    def __init__(self, params: VoiceChangerParams, slotInfo: BeatriceModelSlot):
        raise RuntimeError("not implemented")

    def initialize(self):
        raise RuntimeError("not implemented")

    def setSamplingRate(self, inputSampleRate, outputSampleRate):
        raise RuntimeError("not implemented")

    def update_settings(self, key: str, val: int | float | str):
        raise RuntimeError("not implemented")

    def get_info(self):
        raise RuntimeError("not implemented")

    def get_processing_sampling_rate(self):
        raise RuntimeError("not implemented")

    def generate_input(
        self,
        newData: AudioInOut,
        crossfadeSize: int,
        solaSearchFrame: int = 0,
    ):
        raise RuntimeError("not implemented")

    def inference(self, receivedData: AudioInOut, crossfade_frame: int, sola_search_frame: int):
        raise RuntimeError("not implemented")

    def __del__(self):
        if hasattr(self, "pipeline"):
            del self.pipeline
            self.pipeline = None

        if getattr(torch.backends, "mps", None) is not None and torch.backends.mps.is_available():
            torch.mps.empty_cache()
        elif torch.cuda.is_available():
            torch.cuda.empty_cache()
        gc.collect()

    def get_model_current(self):
        return [
            {
                "key": "dstId",
                "val": self.settings.dstId,
            },
        ]
