import torch
import onnxruntime


class DeviceManager(object):
    _instance = None
    forceTensor: bool = False

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.mps_enabled: bool = (
            getattr(torch.backends, "mps", None) is not None
            and torch.backends.mps.is_available()
        )
        # Assume execution on Apple Silicon only
        self.gpu_num = 1 if self.mps_enabled else 0

    def getDevice(self, id: int):
        if id < 0 or self.gpu_num == 0:
            dev = torch.device("mps") if self.mps_enabled else torch.device("cpu")
        else:
            dev = torch.device("mps") if self.mps_enabled else torch.device("cpu")
        return dev

    def getOnnxExecutionProvider(self, gpu: int):
        # Only CPU execution provider is supported
        return ["CPUExecutionProvider"], [
            {
                "intra_op_num_threads": 8,
                "execution_mode": onnxruntime.ExecutionMode.ORT_PARALLEL,
                "inter_op_num_threads": 8,
            }
        ]

    def setForceTensor(self, forceTensor: bool):
        self.forceTensor = forceTensor

    def halfPrecisionAvailable(self, id: int):
        # Half precision is not supported on MPS
        return False

    def getDeviceMemory(self, id: int):
        # Device memory information is not available on MPS
        return 0
