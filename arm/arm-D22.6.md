## D22.6 Floating-point behaviors for instructions that target the SME ZA array

DHTZVK

Unless stated otherwise, the behaviors in this section apply to SME and SME2 floating-point instructions that place their results in the ZA array, except the SME BFloat16 instructions BFMOPA (widening), BFMOPS (widening), BFDOT, and BFVDOT , for which, see BFloat16 behaviors for instructions that compute sum-of-products.

## The instructions:

RWLPHB

•

Honor FPCR.{FZ, RMode, FZ16, AH, FIZ}, unless specified otherwise in Flushing denormalized numbers to

zero or Alternate BFloat16 behaviors.

RRKHHZ

- Generate the Default NaN, as if FPCR.DN is 1.

RTGSKG

- Produce the expected IEEE 754 default result but do not update the FPSR cumulative exception flag bits.

RFSWYW

- Disable trapped floating-point exceptions, as if FPCR.{IDE, IXE, UFE, OFE, DZE, IOE} are all 0.

RBWKKQ The SME instructions that accumulate dot products of pairs of adjacent half-precision elements in the source vectors into single-precision elements in the ZA array:

- Perform a fused sum-of-products without rounding of the intermediate products, but rounding the single-precision sum before addition to the accumulator tile or multi-vector operand element.
- Generate the default NaN as intermediate sum-of-products when any of the following are true:
- -Any multiplier input is a NaN.
- -Any product is infinity × 0.0.
- -Both products are infinity of differing signs.
- Generate an intermediate sum-of-products of the same infinity when there are products that are infinity all with the same sign.

If FEAT\_AFP is implemented, the instructions honor FPCR.{AH, FIZ}, in which case:

- When FPCR.AH is 1, the sign bit of a generated default NaN result is set to 1 instead of 0.
- When FPCR.AH is 1 and FPCR.FZ is 1, a denormal result, detected after rounding with an unbounded exponent has been applied, is flushed to zero.
- When FPCR.AH is 1, the FPCR.FZ control does not cause denormalized inputs to be flushed to zero.
- When FPCR.FIZ is 1, all denormalized inputs are flushed to zero.
- Honor FPCR.RMode, supporting all four IEEE 754 rounding modes.
- Honor FPCR.FZ.
- Honor FPCR.FZ16.

Those instructions that multiply single elements from each source vector and accumulate their product into the ZA array perform a fused multiply-add to each accumulator tile or multi-vector operand element without rounding of the intermediate products.

RRPSLK

RTCLRM

RVVVNR

RTXKVK

RJRRMJ