# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class ACC_H100(OfflineGPUBaseConfig):
    system = KnownSystem.ACC_H100
    gpu_batch_size = 2048
    offline_expected_qps = 57000


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class ACC_H100_Triton(ACC_H100):
    use_triton = True

