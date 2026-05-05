## C6.2.149 DGH

## Data gathering hint

This instruction is a hint instruction that indicates that it is not expected to be performance optimal to merge memory accesses with Normal Non-cacheable or Device-GRE attributes appearing in program order before the hint instruction with any memory accesses appearing after the hint instruction into a single memory transaction on an interconnect.

## System

(FEAT\_DGH)

<!-- image -->

## Encoding

DGH

## Decode for this encoding

if !IsFeatureImplemented(FEAT\_DGH) then EndOfDecode(Decode\_NOP);

## Operation

Hint\_DGH();
