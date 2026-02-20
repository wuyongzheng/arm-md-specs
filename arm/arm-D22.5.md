## D22.5 Floating-point behaviors in Streaming SVE mode

- DDMPBW Unless stated otherwise, the behaviors in this section apply when the PE is in Streaming SVE mode, to floating-point

instructions that place their results in SIMD&amp;FP registers or SVE scalable vector registers, except for:

- SVE BFloat16 instructions BFDOT and BFMMLA , for which, see BFloat16 behaviors for instructions that compute sum-of-products.
- FP8 instructions, for which, see Summary of FP8 instruction behaviors.

## The instructions:

- RPHDZL · Honor FPCR.{DN, FZ, RMode, FZ16, AH, FIZ}, unless specified otherwise in Flushing denormalized numbers to zero or Alternate BFloat16 behaviors.
- RGTYSK · Produce the expected IEEE 754 default result and update the FPSR cumulative exception flag bits, unless specified otherwise in Alternate BFloat16 behaviors.
- RFBFNT
- Disable trapped floating-point exceptions as if FPCR.{IDE, IXE, UFE, OFE, DZE, IOE} are all 0, and treat the NEP element preserve control as if it is 0, if FEAT\_SME\_FA64 is not implemented or not enabled at the current Exception level.

## See also:

- Streaming SVE mode.