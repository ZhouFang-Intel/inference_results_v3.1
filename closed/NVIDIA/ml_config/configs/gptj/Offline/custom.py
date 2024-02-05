# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class ACC_H100(OfflineGPUBaseConfig):
    system = KnownSystem.ACC_H100
    gpu_batch_size = 32
    use_fp8 = True
    offline_expected_qps = 9.5
    enable_sort = True


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class ACC_H100_HighAccuracy(ACC_H100):
    pass

