# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.


from torchrl.modules.tensordict_module.common import DistributionalDQNnet

from .batchrenorm import BatchRenorm1d

from .decision_transformer import DecisionTransformer
from .exploration import (
    ConsistentDropout,
    ConsistentDropoutModule,
    NoisyLazyLinear,
    NoisyLinear,
    reset_noise,
)
from .llm import GPT2RewardModel
from .model_based import (
    DreamerActor,
    ObsDecoder,
    ObsEncoder,
    RSSMPosterior,
    RSSMPrior,
    RSSMRollout,
)
from .models import (
    Conv2dNet,
    Conv3dNet,
    ConvNet,
    DdpgCnnActor,
    DdpgCnnQNet,
    DdpgMlpActor,
    DdpgMlpQNet,
    DTActor,
    DuelingCnnDQNet,
    DuelingMlpDQNet,
    MLP,
    OnlineDTActor,
)
from .multiagent import (
    MultiAgentConvNet,
    MultiAgentMLP,
    MultiAgentNetBase,
    QMixer,
    VDNMixer,
)
from .utils import Squeeze2dLayer, SqueezeLayer

__all__ = [
    "DistributionalDQNnet",
    "BatchRenorm1d",
    "DecisionTransformer",
    "GPT2RewardModel",
    "ConsistentDropout",
    "ConsistentDropoutModule",
    "NoisyLazyLinear",
    "NoisyLinear",
    "reset_noise",
    "DreamerActor",
    "ObsDecoder",
    "ObsEncoder",
    "RSSMPosterior",
    "RSSMPrior",
    "RSSMRollout",
    "Conv2dNet",
    "Conv3dNet",
    "ConvNet",
    "DdpgCnnActor",
    "DdpgCnnQNet",
    "DdpgMlpActor",
    "DdpgMlpQNet",
    "DTActor",
    "DuelingCnnDQNet",
    "DuelingMlpDQNet",
    "MLP",
    "OnlineDTActor",
    "MultiAgentConvNet",
    "MultiAgentMLP",
    "MultiAgentNetBase",
    "QMixer",
    "VDNMixer",
    "Squeeze2dLayer",
    "SqueezeLayer",
]
