# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class ACC_H100(OfflineGPUBaseConfig):
    system = KnownSystem.ACC_H100
    gpu_batch_size = 2048
    use_graphs = True  # MLPINF-1773
    offline_expected_qps = 17000
    disable_encoder_plugin = False

