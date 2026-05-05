## C6.2.482 TSB

Trace synchronization barrier

This instruction is a barrier that synchronizes the trace operations of instructions, see Trace Synchronization Barrier (TSB).

If FEAT\_TRF is not implemented, this instruction executes as a NOP .

## System

(FEAT\_TRF)

<!-- image -->

## Encoding

TSB CSYNC

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_TRF) then EndOfDecode(Decode_NOP);
```

## Operation

```
if IsFeatureImplemented(FEAT_FGT2) && IsFeatureImplemented(FEAT_TRBEv1p1) then constant boolean trap_to_el2 = (PSTATE.EL IN {EL0, EL1} && EL2Enabled() && !IsInHost() && (!HaveEL(EL3) || SCR_EL3.FGTEn2 == '1') && HFGITR2_EL2.TSBCSYNC == '1'); if trap_to_el2 then ExceptionRecord except = ExceptionSyndrome(Exception_LDST64BTrap); // to except.syndrome.iss = \texttt{0x4}<24:0>; constant bits(64) preferred_exception_return = ThisInstrAddr(64); constant integer vect_offset = \texttt{0x0}; AArch64.TakeException(EL2, except, preferred_exception_return, vect_offset);
```

```
be renamed TraceSynchronizationBarrier();
```
