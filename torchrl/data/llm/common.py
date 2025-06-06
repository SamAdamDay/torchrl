# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import annotations

import torch

from tensordict import TensorClass


class LLMData(TensorClass["nocast"]):
    """Represents the input or output of a Large Language Model (LLM).

    Other algorithm-specific attributes such as `reward`, `advantages` or done states are handled automatically by the
    envs and, therefore, are not included in this class.

    Attributes:
        tokens (torch.Tensor): The input/output tokens as a tensor.
        attention_mask (torch.Tensor, optional): The attention mask for the input tokens. Default to `None`.
        tokens_response (torch.Tensor, optional): The response tokens generated by the model. Default to `None`.

            .. note:: the reponse is the sequence of tokens output by a model, excluding the input
                tokens.

        token_list (list[int] | list[list[int]], optional): The output tokens as a list of integers or a list of lists
            of integers. Default to `None`.
        tokens_response_list (list[list[int]], optional): The response tokens generated by the model as a list of
            lists of integers. Default to `None`.
        logits (torch.Tensor, optional): The logits of the output tokens. Default to `None`.
        log_probs (torch.Tensor, optional): The log probabilities of the output tokens. Default to `None`.
        text (str | list[str], optional): The output text as a string or a list of strings. Default to `None`.

    .. seealso:: :class:`~torchrl.data.LLMInput` and :class:`~torchrl.data.LLMOutput`.

    """

    tokens: torch.Tensor | None = None
    tokens_response: torch.Tensor | None = None
    attention_mask: torch.Tensor | None = None
    token_list: list[int] | list[list[int]] | None = None
    tokens_response_list: list[list[int]] | None = None
    logits: torch.Tensor | None = None
    log_probs: torch.Tensor | None = None
    text: str | list[str] | None = None
    text_response: torch.Tensor | None = None
