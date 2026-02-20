## F5.1.46 DCPS3

Debug Change PE State to EL3 allows the debugger to move the PE into EL3 from a lower Exception level or to a specific mode at the current Exception level.

DCPS3 is UNDEFINED if any of:

- The PE is in Non-debug state.
- EL3 is not implemented.
- EDSCR.SDD is set to 1.

When the PE executes DCPS3 :

- If EL3 is using AArch32, the PE enters Monitor mode and LR\_mon, SPSR\_mon, DLR and DSPSR become UNKNOWN. If DCPS3 is executed in Monitor mode, SCR.NS is cleared to 0.
- If EL3 is using AArch64, the PE enters EL3 using AArch64, selects SP\_EL3, and ELR\_EL3, ESR\_EL3, SPSR\_EL3, DLR\_EL0 and DSPSR\_EL0 become UNKNOWN.

For more information on the operation of the DCPS&lt;n&gt; instructions, see DCPS.

<!-- image -->

## Encoding

DCPS3

## Decode for this encoding

if !HaveEL(EL3) then UNDEFINED; end

## Operation

```
if !Halted() || EDSCR.SDD == '1' then UNDEFINED; end if ELUsingAArch32(EL3) then constant boolean from_secure = (CurrentSecurityState() == SS_Secure); if PSTATE.M == M32_Monitor then SCR.NS = '0'; end AArch32.WriteMode(M32_Monitor); if IsFeatureImplemented(FEAT_PAN) then if !from_secure then PSTATE.PAN = '0'; elsif SCTLR.SPAN == '0' then PSTATE.PAN = '1'; end end PSTATE.E = SCTLR.EE; LR_mon = bits(32) UNKNOWN; SPSR_mon = bits(32) UNKNOWN; DLR = bits(32) UNKNOWN; DSPSR = bits(32) UNKNOWN; else // Targeting EL3 using AArch64 AArch64.MaybeZeroRegisterUppers();
```

Listing F5-29

Listing F5-30

```
MaybeZeroSVEUppers(EL3); PSTATE.nRW = '0'; PSTATE.SP = '1'; PSTATE.EL = EL3; if IsFeatureImplemented(FEAT_UAO) then PSTATE.UAO = '0'; end ELR_EL3 = bits(64) UNKNOWN; ESR_EL3 = bits(64) UNKNOWN; SPSR_EL3 = bits(64) UNKNOWN; DLR_EL0 = bits(64) UNKNOWN; DSPSR_EL0 = bits(64) UNKNOWN; boolean sync_errors = IsFeatureImplemented(FEAT_IESB) && SCTLR_EL3.IESB == '1'; if IsFeatureImplemented(FEAT_DoubleFault) && EffectiveEA() == '1' && SCR_EL3.NMEA == '1' then sync_errors = TRUE; end // SCTLR_EL3.IESB might be ignored in Debug state. if !ConstrainUnpredictableBool(Unpredictable_IESBinDebug) then sync_errors = FALSE; end if sync_errors then SynchronizeErrors(); end end UpdateEDSCRFields(); // Update EDSCR PE state flags
```