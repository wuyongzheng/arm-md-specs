## C6.2.318 PSB

Profiling synchronization barrier

This instruction is a barrier that ensures that all existing profiling data for the current PE has been formatted, and profiling buffer addresses have been translated such that all writes to the profiling buffer have been initiated. A following DSB instruction completes when the writes to the profiling buffer have completed.

If FEAT\_SPE is not implemented, this instruction executes as a NOP .

## System

(FEAT\_SPE)

<!-- image -->

## Encoding

PSB CSYNC

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SPE) then EndOfDecode(Decode_NOP);
```

## Operation

```
if IsFeatureImplemented(FEAT_FGT) && IsFeatureImplemented(FEAT_SPEv1p5) then constant boolean trap_to_el2 = (PSTATE.EL IN {EL0, EL1} && EL2Enabled() && !IsInHost() && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && HFGITR_EL2.PSBCSYNC == '1'); if trap_to_el2 then ExceptionRecord except = ExceptionSyndrome(Exception_LDST64BTrap); // to be renamed except.syndrome.iss = \texttt{0x3}<24:0>; constant bits(64) preferred_exception_return = ThisInstrAddr(64); constant integer vect_offset = \texttt{0x0}; AArch64.TakeException(EL2, except, preferred_exception_return, vect_offset);
```

ProfilingSynchronizationBarrier();
