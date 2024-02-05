# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class ACC_H100(ServerGPUBaseConfig):
    system = KnownSystem.ACC_H100
    gpu_batch_size = 2048
    server_target_qps = 15000
    audio_buffer_num_lines = 8192
    audio_batch_size = 512
    use_graphs = True  # MLPINF-1773

