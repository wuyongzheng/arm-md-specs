## F5.1.45 DCPS2

Debug Change PE State to EL2 allows the debugger to move the PE into EL2 from a lower Exception level.

DCPS2 is UNDEFINED if any of:

- The PE is in Non-debug state.
- EL2 is not implemented.
- The PE is in Secure state and any of:
- Secure EL2 is not implemented.
- Secure EL2 is implemented and Secure EL2 is disabled.

When the PE executes DCPS2 :

- If EL2 is using AArch32, the PE enters Hyp mode and ELR\_hyp, HSR, SPSR\_hyp, DLR and DSPSR become UNKNOWN.
- If EL2 is using AArch64, the PE enters EL2 using AArch64, selects SP\_EL2, and ELR\_EL2, ESR\_EL2, SPSR\_EL2, DLR\_EL0 and DSPSR\_EL0 become UNKNOWN.

For more information on the operation of the DCPS&lt;n&gt; instructions, see DCPS.

<!-- image -->

## Encoding

DCPS2

## Decode for this encoding

if !HaveEL(EL2) then UNDEFINED; end

## Operation

```
if !Halted() || !EL2Enabled() then UNDEFINED; end if ELUsingAArch32(EL2) then AArch32.WriteMode(M32_Hyp); PSTATE.E = HSCTLR.EE; ELR_hyp = bits(32) UNKNOWN; HSR = bits(32) UNKNOWN; SPSR_hyp = bits(32) UNKNOWN; DLR = bits(32) UNKNOWN; DSPSR = bits(32) UNKNOWN; else // Targeting EL2 using AArch64 AArch64.MaybeZeroRegisterUppers(); MaybeZeroSVEUppers(EL2); PSTATE.nRW = '0'; PSTATE.SP = '1'; PSTATE.EL = EL2; if IsFeatureImplemented(FEAT_PAN) && SCTLR_EL2.SPAN == '0' && ELIsInHost(EL0) then PSTATE.PAN = '1'; end
```

Listing F5-27

Listing F5-28

```
if IsFeatureImplemented(FEAT_UAO) then PSTATE.UAO = '0'; end ELR_EL2 = bits(64) UNKNOWN; ESR_EL2 = bits(64) UNKNOWN; SPSR_EL2 = bits(64) UNKNOWN; DLR_EL0 = bits(64) UNKNOWN; DSPSR_EL0 = bits(64) UNKNOWN; // SCTLR_EL2.IESB might be ignored in Debug state. if (IsFeatureImplemented(FEAT_IESB) && SCTLR_EL2.IESB == '1' && !ConstrainUnpredictableBool(Unpredictable_IESBinDebug)) then SynchronizeErrors(); end end UpdateEDSCRFields(); // Update EDSCR PE state flags
```