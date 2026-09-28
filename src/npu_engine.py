import os
import sys
import logging
import onnxruntime as ort

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("EdgeFix-NPU")

class NPUEngine:
    """
    Inference Engine for EdgeFix AI targeting Qualcomm Hexagon NPU
    via ONNX Runtime QNN Execution Provider with CPU Fallback.
    """
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.session = self._initialize_session()

    def _initialize_session(self) -> ort.InferenceSession:
        if not os.path.exists(self.model_path):
            logger.warning(f"Model path {self.model_path} not found. Operating in simulation mode.")
            return None

        # Preferred provider: Qualcomm Hexagon HTP
        qnn_options = {
            "backend_path": "QNNHtp.dll",
            "profiling_level": "basic"
        }

        providers = [
            ('QNNExecutionProvider', qnn_options),
            'CPUExecutionProvider'  # Fallback for evaluation safety
        ]

        try:
            logger.info("Initializing ONNX session with Hexagon NPU priority...")
            session = ort.InferenceSession(self.model_path, providers=providers)
            active_providers = session.get_providers()
            logger.info(f"Session initialized successfully. Active Providers: {active_providers}")
            return session
        except Exception as e:
            logger.error(f"Failed to initialize QNN Execution Provider: {e}. Falling back to CPU execution.")
            return ort.InferenceSession(self.model_path, providers=['CPUExecutionProvider'])

if __name__ == "__main__":
    engine = NPUEngine("models/vision_yolo_int8.onnx")
