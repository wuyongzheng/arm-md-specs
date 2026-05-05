## C6.2.161 GCSB

Guarded Control Stack barrier

This instruction generates a GCSB effect.

If FEAT\_GCS is not implemented, this instruction executes as a NOP .

## System

(FEAT\_GCS)

<!-- image -->

## Encoding

GCSB

DSYNC

## Decode for this encoding

if !IsFeatureImplemented(FEAT\_GCS) then EndOfDecode(Decode\_NOP);

## Operation

GCSSynchronizationBarrier();
