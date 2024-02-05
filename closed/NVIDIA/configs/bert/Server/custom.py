# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class ACC_H100(ServerGPUBaseConfig):
    system = KnownSystem.ACC_H100
    use_small_tile_gemm_plugin = False
    enable_interleaved = False
    use_graphs = False
    graphs_max_seqlen = 200
    gpu_batch_size = 256
    server_target_qps = 2000
    server_num_issue_query_threads = 1
    workspace_size = 7516192768
    # soft_drop = 1.0
    soft_drop = 0.99


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class ACC_H100_HighAccuracy(ACC_H100):
    precision = "fp16"
    use_fp8 = True
    server_target_qps = 4000
    soft_drop = 1.0


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class ACC_H100_Triton(ACC_H100):
    use_triton = True
    server_target_qps = 2300


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class ACC_H100_HighAccuracy_Triton(ACC_H100_HighAccuracy):
    use_triton = True
    server_target_qps = 1150

