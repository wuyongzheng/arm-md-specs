## J1.3 Shared pseudocode

This section holds the pseudocode that is common to execution in AArch64 state and in AArch32 state. Functions listed in this section are identified only by a FunctionName , without an AArch64. or AArch32. prefix. This section is organized by functional groups, with the functional groups being indicated by hierarchical path names, for example shared/debug/DebugTarget .

The top-level sections of the shared pseudocode hierarchy are:

- shared/debug.
- shared/exceptions.
- shared/functions.
- shared/trace.
- shared/translation.

## J1.3.1 shared/debug

This section includes the following pseudocode functions:

- ClearStickyErrors
- DebugTarget
- DebugTargetFrom
- DoubleLockStatus
- OSLockStatus
- Component
- GetAccessComponent
- SoftwareLockStatus
- IsG1ActivityMonitorImplemented
- IsG1ActivityMonitorOffsetImplemented
- AllowExternalDebugAccess
- AllowExternalPMSSAccess
- AllowExternalPMUAccess
- AllowExternalTraceAccess
- Debug
- ExternalInvasiveDebugEnabled
- ExternalNoninvasiveDebugAllowed
- ExternalNoninvasiveDebugEnabled
- ExternalRealmInvasiveDebugEnabled
- ExternalRealmNoninvasiveDebugEnabled
- ExternalRootInvasiveDebugEnabled
- ExternalRootNoninvasiveDebugEnabled
- ExternalSecureInvasiveDebugEnabled
- ExternalSecureNoninvasiveDebugEnabled

•

InvasiveDebugPermittedPAS

- IsAccessNonSecure
- IsAccessRealm
- IsAccessRoot
- IsAccessSecure
- IsCorePowered
- IsPASValid

- BreakpointInfo
- BreakpointType
- CheckValidStateMatch
- ContextAwareBreakpointRange
- IsContextAwareBreakpoint
- NumBreakpointsImplemented
- NumContextAwareBreakpointsImplemented
- NumWatchpointsImplemented
- CTI\_ProcessEvent
- CTI\_SetEventLevel
- CTI\_SignalEvent
- CrossTrigger
- CheckForDCCInterrupts
- DTR
- Read\_DBGDTRRX\_EL0
- Read\_DBGDTRTX\_EL0
- Read\_DBGDTR\_EL0
- Write\_DBGDTRRX\_EL0
- Write\_DBGDTRTX\_EL0
- Write\_DBGDTR\_EL0
- Write\_EDITR
- DCPSInstruction
- DRPSInstruction

•

DebugHalt

- DebugRestorePSR
- DisableITRAndResumeInstructionPrefetch
- ExecuteA64
- ExecuteT32
- ExitDebugState
- Halt
- HaltOnBreakpointOrWatchpoint

•

Halted

- HaltingAllowed
- Restarting
- StopInstructionPrefetchAndEnableITR
- UpdateDbgAuthStatus
- UpdateEDHSR
- UpdateEDSCRFields
- CheckEDBGRQ
- CheckExceptionCatch
- CheckExternalDebugRequestEvents
- CheckHaltingStep
- CheckOSUnlockCatch
- CheckPMUHalt
- CheckPendingExceptionCatch
- CheckPendingOSUnlockCatch
- CheckPendingResetCatch

- CheckResetCatch
- CheckSoftwareAccessToDebugRegisters
- CheckTRBEHalt
- EDBGRQ
- ExternalDebugRequest
- HSAdvance
- HaltingStep\_DidNotStep
- HaltingStep\_SteppedEX
- ExternalDebugInterruptsDisabled
- pmu
- CYCLE\_COUNTER\_ID
- CheckForPMUOverflow
- CheckPMUOverflowCondition
- ClearEventCounters
- CountPMUEvents
- EffectiveEPMN
- EffectiveHPMN
- GetNumEventCountersAccessible
- GetNumEventCountersSelfHosted
- GetPMUAccessMask
- GetPMUCounterRange
- GetPMUReadMask
- GetPMUWriteMask
- HasElapsed64Cycles
- INSTRUCTION\_COUNTER\_ID
- IncrementInstructionCounter
- IsMostSecureAccess
- IsRange3Counter
- PMUCaptureEvent
- PMUCaptureEventAllowed
- PMUCaptureEventEnabled
- PMUCountValue
- PMUCounterRange
- PMUEvent
- PMUOverflowCondition
- PMUSwIncrement
- ReservedPMUThreshold
- SMEPMUEventPredicate
- SVEPMUEventPredicate
- ShouldPMUFreeze
- ZeroCycleCounter
- ZeroPMUCounters
- CreatePCSample
- PCSRSuspended
- PCSample
- Read\_EDPCSRlo
- Read\_PMPCSR

- SetPCSRActive
- SetPCSRUnknown
- SetPCSample
- CheckSoftwareStep
- DebugExceptionReturnSS
- SSAdvance
- SoftwareStepOpEnabled
- SoftwareStep\_DidNotStep
- SoftwareStep\_SteppedEX
- DataCacheWatchpointSize
- WatchpointInfo
- WatchpointType

## J1.3.1.1 ClearStickyErrors

```
// ClearStickyErrors() // =================== ClearStickyErrors() EDSCR.TXU = '0'; // Clear TX underrun flag EDSCR.RXO = '0'; // Clear RX overrun flag if Halted() then // in Debug state EDSCR.ITO = '0'; // Clear ITR overrun flag // If halted and the ITR is not empty then it is UNPREDICTABLE whether the EDSCR.ERR is cleared. // The UNPREDICTABLE behavior also affects the instructions in flight, but this is not described // in the pseudocode. if (Halted() && EDSCR.ITE == '0' && ConstrainUnpredictableBool(Unpredictable_CLEARERRITEZERO)) then return; EDSCR.ERR = '0'; // Clear cumulative error flag return;
```

## J1.3.1.2 DebugTarget

```
// DebugTarget() // ============= // Returns the debug exception target Exception bits(2) DebugTarget() ss = CurrentSecurityState(); return DebugTargetFrom(ss);
```

## J1.3.1.3 DebugTargetFrom

```
// DebugTargetFrom() // ================= bits(2) DebugTargetFrom(SecurityState from_state) boolean route_to_el2; if HaveEL(EL2) && (from_state != SS_Secure || (IsFeatureImplemented(FEAT_SEL2) && (!HaveEL(EL3) || SCR_EL3.EEL2 == '1'))) then if ELUsingAArch32(EL2) then route_to_el2 = (HDCR.TDE == '1' || HCR.TGE == '1'); else
```

```
level
```

```
route_to_el2 = (MDCR_EL2.TDE == '1' || HCR_EL2.TGE == '1'); else route_to_el2 = FALSE; bits(2) target; if route_to_el2 then target = EL2; elsif HaveEL(EL3) && !HaveAArch64() && from_state == SS_Secure then target = EL3; else target = EL1; return target;
```

## J1.3.1.4 DoubleLockStatus

```
// DoubleLockStatus() // ================== // Returns the state of the OS Double Lock. // FALSE if OSDLR_EL1.DLK == 0 or DBGPRCR_EL1.CORENPDRQ == 1 or the PE is in Debug state. // TRUE if OSDLR_EL1.DLK == 1 and DBGPRCR_EL1.CORENPDRQ == 0 and the PE is in Non-debug state. boolean DoubleLockStatus() if !IsFeatureImplemented(FEAT_DoubleLock) then return FALSE; if ELUsingAArch32(EL1) then return DBGOSDLR.DLK == '1' && DBGPRCR.CORENPDRQ == '0' && !Halted(); else return OSDLR_EL1.DLK == '1' && DBGPRCR_EL1.CORENPDRQ == '0' && !Halted();
```

## J1.3.1.5 OSLockStatus

```
// OSLockStatus() // ============== // Returns the state of the OS Lock. boolean OSLockStatus() return (if ELUsingAArch32(EL1) then DBGOSLSR.OSLK else OSLSR_EL1.OSLK) ==
```

## J1.3.1.6 Component

```
// Component // ========= // Component Types. enumeration Component { Component_ETE, Component_TRBE, Component_RAS, Component_GIC, Component_PMU, Component_Debug, Component_CTI };
```

```
'1';
```

## J1.3.1.7 GetAccessComponent

```
// GetAccessComponent() // ==================== // Returns the accessed component. Component GetAccessComponent();
```

## J1.3.1.8 SoftwareLockStatus

```
// SoftwareLockStatus() // ==================== // Returns the state of the Software Lock. boolean SoftwareLockStatus() constant Component component = GetAccessComponent(); if !HaveSoftwareLock(component) then return FALSE; case component of when Component_ETE return TRCLSR.SLK == '1'; when Component_Debug return EDLSR.SLK == '1'; when Component_PMU return PMLSR.SLK == '1'; when Component_CTI return CTILSR.SLK == '1'; otherwise return FALSE;
```

## J1.3.1.9 IsG1ActivityMonitorImplemented

```
// IsG1ActivityMonitorImplemented() // ================================ // Returns TRUE if a G1 activity monitor is implemented for the counter // and FALSE otherwise.
```

boolean IsG1ActivityMonitorImplemented(integer i);

## J1.3.1.10 IsG1ActivityMonitorOffsetImplemented

```
// IsG1ActivityMonitorOffsetImplemented() // ====================================== // Returns TRUE if a G1 activity monitor offset is implemented for the counter, // and FALSE otherwise. boolean IsG1ActivityMonitorOffsetImplemented(integer i);
```

## J1.3.1.11 AllowExternalDebugAccess

```
// AllowExternalDebugAccess() // ========================== // Returns TRUE if an external debug interface access to the External DBGBVR<n>_EL1, // DBGBCR<n>_EL1, DBGWVR<n>_EL1, DBGWCR<n>_EL1 registers, and, from Armv8.2, the // OSLAR_EL1 register is allowed for the access. Returns FALSE otherwise. boolean AllowExternalDebugAccess(AddressDescriptor addrdesc) // The access may also be subject to OS Lock, power-down, etc. if IsFeatureImplemented(FEAT_RME) then
```

```
case MDCR_EL3.<EDADE,EDAD> of when '00' return TRUE; when '01' return addrdesc.paddress.paspace IN {PAS_Root, PAS_Secure}; when '10' return addrdesc.paddress.paspace IN {PAS_Root, PAS_Realm}; when '11' return addrdesc.paddress.paspace == PAS_Root; if IsFeatureImplemented(FEAT_Debugv8p4) then if addrdesc.paddress.paspace == PAS_Secure then return TRUE; else if !ExternalInvasiveDebugEnabled() then return FALSE; if ExternalSecureInvasiveDebugEnabled() then return TRUE; if HaveEL(EL3) then EDAD_bit = if ELUsingAArch32(EL3) then SDCR.EDAD else MDCR_EL3.EDAD; return EDAD_bit == '0'; else return NonSecureOnlyImplementation(); J1.3.1.12 AllowExternalPMSSAccess // AllowExternalPMSSAccess() // ========================= // Returns TRUE if an external debug interface access to the PMU Snapshot // registers is allowed for the given Security state, FALSE otherwise. boolean AllowExternalPMSSAccess(AddressDescriptor addrdesc) assert IsFeatureImplemented(FEAT_PMUv3_SS) && HaveAArch64(); // FEAT_Debugv8p4 is always implemented when FEAT_PMUv3_SS is implemented. assert IsFeatureImplemented(FEAT_Debugv8p4); // The access may also be subject to the OS Double Lock, power-down, etc. bits(2) epmssad = if HaveEL(EL3) then MDCR_EL3.EPMSSAD else '11'; // Check for reserved values if !IsFeatureImplemented(FEAT_RME) && epmssad IN {'01','10'} then (-, epmssad) = ConstrainUnpredictableBits(Unpredictable_RESEPMSSAD, 2); // The value returned by ConstrainUnpredictableBits() must be a // non-reserved value assert epmssad IN {'00','11'}; case epmssad of when '00' if IsFeatureImplemented(FEAT_RME) then return addrdesc.paddress.paspace == PAS_Root; else return addrdesc.paddress.paspace == PAS_Secure; when '01' assert IsFeatureImplemented(FEAT_RME); return addrdesc.paddress.paspace IN {PAS_Root, PAS_Realm}; when '10' assert IsFeatureImplemented(FEAT_RME); return addrdesc.paddress.paspace IN {PAS_Root, PAS_Secure}; when '11' return TRUE; J1.3.1.13 AllowExternalPMUAccess is
```

```
// AllowExternalPMUAccess() // ======================== // Returns TRUE if an external debug interface access to the PMU registers // allowed for the given Security state, FALSE otherwise. boolean AllowExternalPMUAccess(AddressDescriptor addrdesc)
```

```
// The access may also be subject to OS Lock, power-down, etc. if IsFeatureImplemented(FEAT_RME) then case MDCR_EL3.<EPMADE,EPMAD> of when '00' return TRUE; when '01' return addrdesc.paddress.paspace IN when '10' return addrdesc.paddress.paspace IN {PAS_Root, PAS_Realm}; when '11' return addrdesc.paddress.paspace == PAS_Root; if IsFeatureImplemented(FEAT_Debugv8p4) then if addrdesc.paddress.paspace == PAS_Secure then return TRUE; else if !ExternalInvasiveDebugEnabled() then return FALSE; if ExternalSecureInvasiveDebugEnabled() then return TRUE; if HaveEL(EL3) then EPMAD_bit = if ELUsingAArch32(EL3) then SDCR.EPMAD else MDCR_EL3.EPMAD; return EPMAD_bit == '0'; else return NonSecureOnlyImplementation();
```

```
// AllowExternalTraceAccess() // ========================== // Returns TRUE if an external Trace access to the Trace registers is allowed // given PAS, FALSE otherwise. boolean AllowExternalTraceAccess(AddressDescriptor addrdesc) // The access may also be subject to OS lock, power-down, etc. if !IsFeatureImplemented(FEAT_TRBE) then return TRUE; assert IsFeatureImplemented(FEAT_Debugv8p4); if IsFeatureImplemented(FEAT_RME) then case MDCR_EL3.<ETADE,ETAD> of when '00' return TRUE; when '01' return addrdesc.paddress.paspace IN {PAS_Root, PAS_Secure}; when '10' return addrdesc.paddress.paspace IN {PAS_Root, PAS_Realm}; when '11' return addrdesc.paddress.paspace == PAS_Root; if addrdesc.paddress.paspace == PAS_Secure then return TRUE; if HaveEL(EL3) then // External Trace access is not supported for EL3 using AArch32 assert !ELUsingAArch32(EL3); return MDCR_EL3.ETAD == '0'; else return NonSecureOnlyImplementation();
```

```
{PAS_Root, PAS_Secure}; J1.3.1.14 AllowExternalTraceAccess for the
```

## J1.3.1.15 Debug

```
signals // ============================
```

```
// Debug authentication Signal DBGEN; Signal NIDEN; Signal SPIDEN; Signal SPNIDEN; Signal RLPIDEN; Signal RTPIDEN;
```

## J1.3.1.16 ExternalInvasiveDebugEnabled

```
// ExternalInvasiveDebugEnabled() // ============================== // The definition of this function is IMPLEMENTATION DEFINED. // In the recommended interface, this function returns the state of the DBGEN boolean ExternalInvasiveDebugEnabled() return DBGEN == HIGH;
```

```
signal.
```

## J1.3.1.17 ExternalNoninvasiveDebugAllowed // ExternalNoninvasiveDebugAllowed() // ================================= // Returns TRUE if Trace and PC Sample-based Profiling are allowed boolean ExternalNoninvasiveDebugAllowed() return ExternalNoninvasiveDebugAllowed(PSTATE.EL); // ExternalNoninvasiveDebugAllowed() // ================================= boolean ExternalNoninvasiveDebugAllowed(bits(2) el) if !ExternalNoninvasiveDebugEnabled() then return FALSE; ss = SecurityStateAtEL(el); if ((ELUsingAArch32(EL3) || ELUsingAArch32(EL1)) &amp;&amp; el == EL0 &amp;&amp; ss == SS\_Secure &amp;&amp; SDER.SUNIDEN == '1') then return TRUE; case ss of when SS\_NonSecure return TRUE; when SS\_Secure return ExternalSecureNoninvasiveDebugEnabled(); when SS\_Realm return ExternalRealmNoninvasiveDebugEnabled(); when SS\_Root return ExternalRootNoninvasiveDebugEnabled(); J1.3.1.18 ExternalNoninvasiveDebugEnabled // ExternalNoninvasiveDebugEnabled() // ================================= // This function returns TRUE if the FEAT\_Debugv8p4 is implemented. // Otherwise, this function is IMPLEMENTATION DEFINED, and, in the // recommended interface, ExternalNoninvasiveDebugEnabled returns // the state of the (DBGEN OR NIDEN) signal. boolean ExternalNoninvasiveDebugEnabled() return (IsFeatureImplemented(FEAT\_Debugv8p4) || ExternalInvasiveDebugEnabled() || NIDEN == HIGH); J1.3.1.19 ExternalRealmInvasiveDebugEnabled

```
// ExternalRealmInvasiveDebugEnabled() // =================================== // The definition of this function is IMPLEMENTATION DEFINED. // In the recommended interface, this function returns the state of // (DBGEN AND RLPIDEN) signal. boolean ExternalRealmInvasiveDebugEnabled() if !IsFeatureImplemented(FEAT_RME) then return FALSE; return ExternalInvasiveDebugEnabled() && RLPIDEN == HIGH;
```

```
the
```

## J1.3.1.20 ExternalRealmNoninvasiveDebugEnabled

```
// ExternalRealmNoninvasiveDebugEnabled() // ====================================== // The definition of this function is IMPLEMENTATION DEFINED. // In the recommended interface, this function returns the state of the // (DBGEN AND RLPIDEN) signal. boolean ExternalRealmNoninvasiveDebugEnabled() if !IsFeatureImplemented(FEAT_RME) then return FALSE; return ExternalRealmInvasiveDebugEnabled();
```

## J1.3.1.21 ExternalRootInvasiveDebugEnabled

```
// ExternalRootInvasiveDebugEnabled() // ================================== // The definition of this function is IMPLEMENTATION DEFINED. // In the recommended interface, this function returns the state of the // (DBGEN AND RLPIDEN AND RTPIDEN AND SPIDEN) signal when FEAT_SEL2 is implemented // and the (DBGEN AND RLPIDEN AND RTPIDEN) signal when FEAT_SEL2 is not implemented. boolean ExternalRootInvasiveDebugEnabled() if !IsFeatureImplemented(FEAT_RME) then return FALSE; return (ExternalInvasiveDebugEnabled() && (!IsFeatureImplemented(FEAT_SEL2) || ExternalSecureInvasiveDebugEnabled()) && ExternalRealmInvasiveDebugEnabled() && RTPIDEN == HIGH);
```

## J1.3.1.22 ExternalRootNoninvasiveDebugEnabled

```
// ExternalRootNoninvasiveDebugEnabled() // ===================================== // The definition of this function is IMPLEMENTATION DEFINED. // In the recommended interface, this function returns the state of // (DBGEN AND RLPIDEN AND SPIDEN AND RTPIDEN) signal. boolean ExternalRootNoninvasiveDebugEnabled() if !IsFeatureImplemented(FEAT_RME) then return FALSE; return ExternalRootInvasiveDebugEnabled();
```

## J1.3.1.23 ExternalSecureInvasiveDebugEnabled

```
// ExternalSecureInvasiveDebugEnabled() // ==================================== // The definition of this function is IMPLEMENTATION DEFINED. // In the recommended interface, this function returns the state of the (DBGEN AND SPIDEN) signal. // CoreSight allows asserting SPIDEN without also asserting DBGEN, but this is not recommended. boolean ExternalSecureInvasiveDebugEnabled() if !HaveSecureState() then return FALSE; return ExternalInvasiveDebugEnabled() && SPIDEN == HIGH;
```

## J1.3.1.24 ExternalSecureNoninvasiveDebugEnabled

```
// ExternalSecureNoninvasiveDebugEnabled() // ======================================= // This function returns the value of ExternalSecureInvasiveDebugEnabled() when FEAT_Debugv8p4 // is implemented. Otherwise, the definition of this function is IMPLEMENTATION DEFINED. // In the recommended interface, this function returns the state of the (DBGEN OR NIDEN) AND
```

```
the
```

```
// (SPIDEN OR SPNIDEN) signal. boolean ExternalSecureNoninvasiveDebugEnabled() if !HaveSecureState() then return FALSE; if !IsFeatureImplemented(FEAT_Debugv8p4) then return (ExternalNoninvasiveDebugEnabled() && (SPIDEN == HIGH || SPNIDEN == HIGH)); else return ExternalSecureInvasiveDebugEnabled();
```

## J1.3.1.25 InvasiveDebugPermittedPAS

```
// InvasiveDebugPermittedPAS() // =========================== // Returns TRUE if the invasive debug of the configured PASpace is permitted by // the authentication interface, and FALSE otherwise. boolean InvasiveDebugPermittedPAS(PASpace pas) case pas of when PAS_Secure return ExternalSecureInvasiveDebugEnabled(); when PAS_NonSecure return ExternalInvasiveDebugEnabled(); when PAS_Root return ExternalRootInvasiveDebugEnabled(); when PAS_Realm return ExternalRealmInvasiveDebugEnabled(); otherwise return FALSE;
```

## J1.3.1.26 IsAccessNonSecure

```
// IsAccessNonSecure() // =================== // Returns TRUE when an access is Non-Secure boolean IsAccessNonSecure(AddressDescriptor addrdesc) return addrdesc.paddress.paspace == PAS_NonSecure;
```

## J1.3.1.27 IsAccessRealm

```
// IsAccessRealm() // =============== // Returns TRUE when an access is Realm boolean IsAccessRealm(AddressDescriptor addrdesc) return addrdesc.paddress.paspace == PAS_Realm;
```

## J1.3.1.28 IsAccessRoot

```
// IsAccessRoot() // ============== // Returns TRUE when an access is Root boolean IsAccessRoot(AddressDescriptor addrdesc) return addrdesc.paddress.paspace == PAS_Root;
```

## J1.3.1.29 IsAccessSecure

```
// IsAccessSecure() // ================ // Returns TRUE when an access is Secure boolean IsAccessSecure(AddressDescriptor addrdesc) return addrdesc.paddress.paspace == PAS_Secure;
```

## J1.3.1.30 IsCorePowered

```
// IsCorePowered() // =============== // Returns TRUE if the Core power domain is powered on, FALSE otherwise. boolean IsCorePowered();
```

## J1.3.1.31 IsPASValid

```
// IsPASValid() // ============ // Returns TRUE if the given value of 'pas' is not reserved, and FALSE otherwise. boolean IsPASValid(bits(2) pas) case pas of when '00' return IsFeatureImplemented(FEAT_Secure); when '01' return TRUE; when '10' return IsFeatureImplemented(FEAT_RME); when '11' return IsFeatureImplemented(FEAT_RME);
```

## J1.3.1.32 BreakpointInfo

```
// BreakpointInfo // ============== // Breakpoint related fields. type BreakpointInfo is ( BreakpointType bptype, // Type of breakpoint matched boolean match, // breakpoint match boolean mismatch // breakpoint mismatch )
```

## J1.3.1.33 BreakpointType

```
// BreakpointType // ============== enumeration BreakpointType { BreakpointType_Inactive, // Breakpoint inactive or disabled BreakpointType_AddrMatch, // Address Match breakpoint BreakpointType_AddrMismatch, // Address Mismatch breakpoint BreakpointType_CtxtMatch };// Context matching breakpoint
```

## J1.3.1.34 CheckValidStateMatch

```
// CheckValidStateMatch() // ====================== // Checks for an invalid state match that will generate Constrained // Unpredictable behavior, otherwise returns Constraint_NONE. (Constraint, bits(2), bit, bit, bits(2)) CheckValidStateMatch(bits(2) ssc_in, bit ssce_in, bit hmc_in, bits(2) pxc_in, boolean isbreakpnt) if !IsFeatureImplemented(FEAT_RME) then assert ssce_in == '0'; boolean reserved = FALSE; bits(2) ssc = ssc_in; bit ssce = ssce_in; bit hmc = hmc_in; bits(2) pxc = pxc_in; // Values that are not allocated in any architecture version case hmc:ssce:ssc:pxc of when '0 0 11 10' reserved = TRUE; when '0 0 1x xx' reserved = !HaveSecureState(); when '1 0 00 x0' reserved = TRUE; when '1 0 01 10' reserved = TRUE; when '1 0 1x 10' reserved = TRUE; when 'x 1 xx xx' reserved = ssc != '01' || (hmc:pxc) IN {'000','110'}; otherwise reserved = FALSE; // Match 'Usr/Sys/Svc' valid only for AArch32 breakpoints if (!isbreakpnt || !HaveAArch32EL(EL1)) && hmc:pxc == '000' && ssc != '11' then reserved = TRUE; // Both EL3 and EL2 are not implemented if !HaveEL(EL3) && !HaveEL(EL2) && (hmc != '0' || ssc != '00') then reserved = TRUE; // EL3 is not implemented if !HaveEL(EL3) && ssc IN {'01','10'} && hmc:ssc:pxc != '10100' then reserved = TRUE; // EL3 using AArch64 only if (!HaveEL(EL3) || !HaveAArch64()) && hmc:ssc:pxc == '11000' then reserved = TRUE; // EL2 is not implemented if !HaveEL(EL2) && hmc:ssc:pxc == '11100' then reserved = TRUE; // Secure EL2 is not implemented if !IsFeatureImplemented(FEAT_SEL2) && (hmc:ssc:pxc) IN {'01100','10100','x11x1'} then reserved = TRUE; if reserved then // If parameters are set to a reserved type, behaves as either disabled or a defined type Constraint c; bits(6) unpred_state_bits; (c, unpred_state_bits) = ConstrainUnpredictableBits(Unpredictable_RESBPWPCTRL, 6); hmc = unpred_state_bits<5>; ssc = unpred_state_bits<4:3>; ssce = unpred_state_bits<2>; pxc = unpred_state_bits<1:0>; assert c IN {Constraint_DISABLED, Constraint_UNKNOWN}; if c == Constraint_DISABLED then return (c, bits(2) UNKNOWN, bit UNKNOWN, bit UNKNOWN, bits(2) UNKNOWN); // Otherwise the value returned by ConstrainUnpredictableBits must be a not-reserved value return (Constraint_NONE, ssc, ssce, hmc, pxc);
```

## J1.3.1.35 ContextAwareBreakpointRange

```
// ContextAwareBreakpointRange() // ============================= // Returns two numbers indicating the index of the first and last context-aware breakpoint. (integer, integer) ContextAwareBreakpointRange() constant integer b = NumBreakpointsImplemented(); constant integer c = NumContextAwareBreakpointsImplemented(); if b <= 16 then return (b -c, b - 1); elsif c <= 16 then return (16 c, 15); else return (0, c - 1);
```

## J1.3.1.36 IsContextAwareBreakpoint

```
// IsContextAwareBreakpoint() // ========================== // Returns TRUE if DBGBCR_EL1[n] is a context-aware breakpoint. boolean IsContextAwareBreakpoint(integer n) (lower, upper) = ContextAwareBreakpointRange(); return n >= lower && n <= upper;
```

## J1.3.1.37 NumBreakpointsImplemented

```
// NumBreakpointsImplemented() // =========================== // Returns the number of breakpoints implemented. integer NumBreakpointsImplemented() return integer IMPLEMENTATION_DEFINED "Number of breakpoints";
```

## J1.3.1.38 NumContextAwareBreakpointsImplemented

```
// NumContextAwareBreakpointsImplemented() // ======================================= // Returns the number of context-aware breakpoints implemented. integer NumContextAwareBreakpointsImplemented() return integer IMPLEMENTATION_DEFINED "Number of context-aware breakpoints";
```

## J1.3.1.39 NumWatchpointsImplemented

```
// NumWatchpointsImplemented() // =========================== // Returns the number of watchpoints implemented. integer NumWatchpointsImplemented() return integer IMPLEMENTATION_DEFINED "Number
```

```
of watchpoints";
```

## J1.3.1.40 CTI\_ProcessEvent

```
// CTI_ProcessEvent() // ================== // Process a discrete event on a Cross Trigger output event trigger. CTI_ProcessEvent(CrossTriggerOut id);
```

## J1.3.1.41 CTI\_SetEventLevel

```
// CTI_SetEventLevel() // =================== // Set a Cross Trigger multi-cycle input event trigger to the specified level. CTI_SetEventLevel(CrossTriggerIn id, Signal level);
```

## J1.3.1.42 CTI\_SignalEvent

```
// CTI_SignalEvent() // ================= // Signal a discrete event on a Cross Trigger input event trigger. CTI_SignalEvent(CrossTriggerIn id);
```

## J1.3.1.43 CrossTrigger

```
// CrossTrigger // ============ enumeration CrossTriggerOut {CrossTriggerOut_DebugRequest, CrossTriggerOut_RestartRequest, CrossTriggerOut_IRQ, CrossTriggerOut_RSVD3, CrossTriggerOut_TraceExtIn0, CrossTriggerOut_TraceExtIn1, CrossTriggerOut_TraceExtIn2, CrossTriggerOut_TraceExtIn3}; enumeration CrossTriggerIn {CrossTriggerIn_CrossHalt, CrossTriggerIn_PMUOverflow, CrossTriggerIn_SPESample, CrossTriggerIn_RSVD3, CrossTriggerIn_TraceExtOut0, CrossTriggerIn_TraceExtOut1, CrossTriggerIn_TraceExtOut2, CrossTriggerIn_TraceExtOut3, CrossTriggerIn_TRBEStop, CrossTriggerIn_TRBEMgmt, CrossTriggerIn_TRBEWrap};
```

## J1.3.1.44 CheckForDCCInterrupts

```
// CheckForDCCInterrupts() // ======================= CheckForDCCInterrupts() commrx = (EDSCR.RXfull == '1'); commtx = (EDSCR.TXfull == '0'); // COMMRX and COMMTX support is optional and not recommended for new designs. // SetInterruptRequestLevel(InterruptID_COMMRX, if commrx then HIGH else LOW); // SetInterruptRequestLevel(InterruptID_COMMTX, if commtx then HIGH else LOW); // The value to be driven onto the common COMMIRQ signal. boolean commirq; if ELUsingAArch32(EL1) then commirq = ((commrx && DBGDCCINT.RX == '1') || (commtx && DBGDCCINT.TX == '1'));
```

```
else commirq = ((commrx && MDCCINT_EL1.RX == '1') || (commtx && MDCCINT_EL1.TX == '1')); SetInterruptRequestLevel(InterruptID_COMMIRQ, if commirq then HIGH else LOW); return;
```

## J1.3.1.45 DTR

```
// DTR // === bits(32) bits(32)
```

```
DTRRX; DTRTX;
```

## J1.3.1.46 Read\_DBGDTRRX\_EL0

```
// Read_DBGDTRRX_EL0() // =================== // Called on reads of debug register 0x080. bits(32) Read_DBGDTRRX_EL0(boolean memory_mapped) return DTRRX;
```

## J1.3.1.47 Read\_DBGDTRTX\_EL0

```
// Read_DBGDTRTX_EL0() // =================== // Called on reads of debug register 0x08C. bits(32) Read_DBGDTRTX_EL0(boolean memory_mapped) underrun = EDSCR.TXfull == '0' || (Halted() && EDSCR.MA == '1' && EDSCR.ITE == '0'); value = if underrun then bits(32) UNKNOWN else DTRTX; if EDSCR.ERR == '1' then return value; // Error flag set: no side-effects if underrun then EDSCR.TXU = '1'; EDSCR.ERR = '1'; // Underrun condition: block side-effects return value; // Return UNKNOWN EDSCR.TXfull = '0'; if Halted() && EDSCR.MA == '1' then EDSCR.ITE = '0'; // See comments in Write_EDITR() if !UsingAArch32() then ExecuteA64(0xB8404401<31:0>); // A64 "LDR W1,[X0],#4" else ExecuteT32(0xF850<15:0> /*hw1*/, 0x1B04<15:0> /*hw2*/); // T32 "LDR R1,[R0],#4" // If the load aborts, the Data Abort exception is taken and EDSCR.ERR is set to 1 if EDSCR.ERR == '1' then EDSCR.TXfull = bit UNKNOWN; DBGDTRTX_EL0 = bits(64) UNKNOWN; else if !UsingAArch32() then ExecuteA64(0xD5130501<31:0>); // A64 "MSR DBGDTRTX_EL0,X1" else ExecuteT32(0xEE00<15:0> /*hw1*/, 0x1E15<15:0> /*hw2*/); // T32 "MSR DBGDTRTXint,R1" // "MSR DBGDTRTX_EL0,X1" calls Write_DBGDTR_EL0() which sets TXfull. assert EDSCR.TXfull == '1'; if !UsingAArch32() then
```

```
X[1, 64] = bits(64) UNKNOWN; else R[1] = bits(32) UNKNOWN; EDSCR.ITE = '1'; // See comments return value;
```

```
// Write_DBGDTRRX_EL0() // ==================== // Called on writes to debug register 0x080. Write_DBGDTRRX_EL0(boolean memory_mapped, bits(32) value) if EDSCR.ERR == '1' then return; // Error flag set: ignore write if EDSCR.RXfull == '1' || (Halted() && EDSCR.MA == '1' && EDSCR.ITE == '0') then EDSCR.RXO = '1'; EDSCR.ERR = '1'; // Overrun condition: ignore write return; EDSCR.RXfull = '1'; DTRRX = value; if Halted() && EDSCR.MA == '1' then EDSCR.ITE = '0'; // See comments in Write_EDITR() if !UsingAArch32() then ExecuteA64(0xD5330501<31:0>); // A64 "MRS X1,DBGDTRRX_EL0" ExecuteA64(0xB8004401<31:0>); // A64 "STR W1,[X0],#4" X[1, 64] = bits(64) UNKNOWN; else ExecuteT32(0xEE10<15:0> /*hw1*/, 0x1E15<15:0> /*hw2*/); // T32 "MRS ExecuteT32(0xF840<15:0> /*hw1*/, 0x1B04<15:0> /*hw2*/); // T32 "STR R1,[R0],#4" R[1] = bits(32) UNKNOWN; // If the store aborts, the Data Abort exception is taken and EDSCR.ERR is set to 1 if EDSCR.ERR == '1' then EDSCR.RXfull = bit UNKNOWN; DBGDTRRX_EL0 = bits(64) UNKNOWN; else // "MRS X1,DBGDTRRX_EL0" calls Read_DBGDTR_EL0() which clears RXfull. assert EDSCR.RXfull == '0'; EDSCR.ITE = '1'; // See comments in Write_EDITR()
```

## in Write\_EDITR() J1.3.1.48 Read\_DBGDTR\_EL0 // Read\_DBGDTR\_EL0() // ================= // System register reads of DBGDTR\_EL0, DBGDTRRX\_EL0 (AArch64) and DBGDTRRXint (AArch32) bits(N) Read\_DBGDTR\_EL0(integer N) // For MRS &lt;Rt&gt;,DBGDTRTX\_EL0 N=32, X[t]=Zeros(32):result // For MRS &lt;Xt&gt;,DBGDTR\_EL0 N=64, X[t]=result assert N IN {32,64}; bits(N) result; if EDSCR.RXfull == '0' then result = bits(N) UNKNOWN; else // On a 64-bit read, implement a half-duplex channel // NOTE: the word order is reversed on reads with regards to writes if N == 64 then result&lt;63:32&gt; = DTRTX; result&lt;31:0&gt; = DTRRX; EDSCR.RXfull = '0'; return result; J1.3.1.49 Write\_DBGDTRRX\_EL0 R1,DBGDTRRXint"

return;

## J1.3.1.50 Write\_DBGDTRTX\_EL0

```
// Write_DBGDTRTX_EL0() // ==================== // Called on writes to debug register 0x08C. Write_DBGDTRTX_EL0(boolean memory_mapped, bits(32) value) DTRTX = value; return;
```

## J1.3.1.51 Write\_DBGDTR\_EL0

```
// Write_DBGDTR_EL0() // ================== // System register writes to DBGDTR_EL0, DBGDTRTX_EL0 (AArch64) and DBGDTRTXint (AArch32) Write_DBGDTR_EL0(bits(N) value_in) bits(N) value = value_in; // For MSR DBGDTRTX_EL0,<Rt> N=32, value=X[t]<31:0>, X[t]<63:32> is ignored // For MSR DBGDTR_EL0,<Xt> N=64, value=X[t]<63:0> assert N IN {32,64}; if EDSCR.TXfull == '1' then value = bits(N) UNKNOWN; // On a 64-bit write, implement a half-duplex channel if N == 64 then DTRRX = value<63:32>; DTRTX = value<31:0>; // 32-bit or 64-bit write EDSCR.TXfull = '1'; return;
```

## J1.3.1.52 Write\_EDITR

```
// Write_EDITR() // ============= // Called on writes to debug register 0x084. Write_EDITR(boolean memory_mapped, bits(32) value) if EDSCR.ERR == '1' then return; // Error flag set: ignore write if !Halted() then return; // Non-debug state: ignore write if EDSCR.ITE == '0' || EDSCR.MA == '1' then EDSCR.ITO = '1'; EDSCR.ERR = '1'; // Overrun condition: block write return; // ITE indicates whether the PE is ready to accept another instruction; the PE // may support multiple outstanding instructions. Unlike the "InstrCompl" flag in [v7A] there // is no indication that the pipeline is empty (all instructions have completed). In this // pseudocode, the assumption is that only one instruction can be executed at a time, // meaning ITE acts like "InstrCompl". EDSCR.ITE = '0'; if !UsingAArch32() then ExecuteA64(value); else ExecuteT32(value<15:0>/*hw1*/, value<31:16> /*hw2*/); EDSCR.ITE = '1'; return;
```

## J1.3.1.53 DCPSInstruction

```
// DCPSInstruction() // ================= // Operation of the DCPS instruction in Debug state DCPSInstruction(bits(2) target_el) SynchronizeContext(); bits(2) handle_el; case target_el of when EL1 if PSTATE.EL == EL2 || (PSTATE.EL == EL3 && !UsingAArch32()) then handle_el = PSTATE.EL; elsif EL2Enabled() && HCR_EL2.TGE == '1' then UNDEFINED; else handle_el = EL1; when EL2 if !HaveEL(EL2) then UNDEFINED; elsif PSTATE.EL == EL3 && !UsingAArch32() then handle_el = EL3; elsif !IsSecureEL2Enabled() && CurrentSecurityState() == SS_Secure then UNDEFINED; else handle_el = EL2; when EL3 if EDSCR.SDD == '1' || !HaveEL(EL3) then UNDEFINED; else handle_el = EL3; otherwise Unreachable(); from_secure = CurrentSecurityState() == SS_Secure; if ELUsingAArch32(handle_el) then if PSTATE.M == M32_Monitor then SCR.NS = '0'; assert UsingAArch32(); // Cannot move from AArch64 to AArch32 case handle_el of when EL1 AArch32.WriteMode(M32_Svc); if IsFeatureImplemented(FEAT_PAN) && SCTLR.SPAN == '0' then PSTATE.PAN = '1'; when EL2 AArch32.WriteMode(M32_Hyp); when EL3 AArch32.WriteMode(M32_Monitor); if IsFeatureImplemented(FEAT_PAN) then if !from_secure then PSTATE.PAN = '0'; elsif SCTLR.SPAN == '0' then PSTATE.PAN = '1'; if handle_el == EL2 then ELR_hyp = bits(32) UNKNOWN; HSR = bits(32) UNKNOWN; else LR = bits(32) UNKNOWN; SPSR_curr[] = bits(32) UNKNOWN; PSTATE.E = SCTLR_ELx[].EE; DLR = bits(32) UNKNOWN; DSPSR = bits(32) UNKNOWN; else // Targeting AArch64 from_32 = UsingAArch32(); if from_32 then AArch64.MaybeZeroRegisterUppers(); if from_32 && IsFeatureImplemented(FEAT_SME) && PSTATE.SM == '1' then ResetSVEState();
```

```
else MaybeZeroSVEUppers(target_el); PSTATE.nRW = '0'; PSTATE.SP = '1'; PSTATE.EL = handle_el; if IsFeatureImplemented(FEAT_PAN) && ((handle_el == EL1 && SCTLR_EL1.SPAN == '0') || (handle_el == EL2 && ELIsInHost(EL0) && SCTLR_EL2.SPAN == '0')) then PSTATE.PAN = '1'; ELR_ELx[] = bits(64) UNKNOWN; SPSR_ELx[] = bits(64) UNKNOWN; ESR_ELx[] = bits(64) UNKNOWN; DLR_EL0 = bits(64) UNKNOWN; DSPSR_EL0 = bits(64) UNKNOWN; if IsFeatureImplemented(FEAT_UAO) then PSTATE.UAO = '0'; if IsFeatureImplemented(FEAT_MTE) then PSTATE.TCO = '1'; if IsFeatureImplemented(FEAT_GCS) then PSTATE.EXLOCK = '0'; if IsFeatureImplemented(FEAT_UINJ) then PSTATE.UINJ = '0'; UpdateEDSCRFields(); // Update EDSCR PE state flags sync_errors = IsFeatureImplemented(FEAT_IESB) && SCTLR_ELx[].IESB == '1'; if IsFeatureImplemented(FEAT_DoubleFault) && !UsingAArch32() then sync_errors = (sync_errors || (EffectiveEA() == '1' && SCR_EL3.NMEA == '1' && PSTATE.EL == EL3)); // The Effective value of SCTLR[].IESB might be zero in Debug state. if !ConstrainUnpredictableBool(Unpredictable_IESBinDebug) then sync_errors = FALSE; if sync_errors then SynchronizeErrors(); return; J1.3.1.54 DRPSInstruction // DRPSInstruction() // ================= // Operation of the A64 DRPS and T32 ERET instructions in Debug state DRPSInstruction() sync_errors = IsFeatureImplemented(FEAT_IESB) && SCTLR_ELx[].IESB == '1'; if IsFeatureImplemented(FEAT_DoubleFault) && !UsingAArch32() then sync_errors = (sync_errors || (EffectiveEA() == '1' && SCR_EL3.NMEA == '1' && PSTATE.EL == EL3)); // The Effective value of SCTLR[].IESB might be zero in Debug state. if !ConstrainUnpredictableBool(Unpredictable_IESBinDebug) then sync_errors = FALSE; if sync_errors then SynchronizeErrors(); SynchronizeContext(); DebugRestorePSR(); return; J1.3.1.55 DebugHalt // DebugHalt // ========= // Reason codes for entry to Debug state constant bits(6) DebugHalt_Breakpoint = '000111'; constant bits(6) DebugHalt_EDBGRQ = '010011'; constant bits(6) DebugHalt_Step_Normal = '011011'; constant bits(6) DebugHalt_Step_Exclusive = '011111'; constant bits(6) DebugHalt_OSUnlockCatch = '100011'; constant bits(6) DebugHalt_ResetCatch = '100111'; constant bits(6) DebugHalt_Watchpoint = '101011'; constant bits(6) DebugHalt_HaltInstruction = '101111';
```

```
constant bits(6) DebugHalt_SoftwareAccess = '110011'; constant bits(6) DebugHalt_ExceptionCatch = '110111'; constant bits(6) DebugHalt_Step_NoSyndrome = '111011';
```

## J1.3.1.56 DebugRestorePSR

```
// DebugRestorePSR() // ================= DebugRestorePSR() // PSTATE.{N,Z,C,V,Q,GE,SS,D,A,I,F} are not observable and ignored in Debug state, so // behave as if UNKNOWN. if UsingAArch32() then constant bits(32) spsr = SPSR_curr[]; SetPSTATEFromPSR(spsr); PSTATE.<N,Z,C,V,Q,GE,SS,A,I,F> = bits(13) UNKNOWN; // In AArch32, all instructions are T32 and unconditional. PSTATE.IT = '00000000'; PSTATE.T = '1'; // PSTATE.J is RES0 DLR = bits(32) UNKNOWN; DSPSR = bits(32) UNKNOWN; else constant bits(64) spsr = SPSR_ELx[]; SetPSTATEFromPSR(spsr); PSTATE.<N,Z,C,V,SS,D,A,I,F> = bits(9) UNKNOWN; DLR_EL0 = bits(64) UNKNOWN; DSPSR_EL0 = bits(64) UNKNOWN; UpdateEDSCRFields(); // Update EDSCR PE state flags
```

## J1.3.1.57 DisableITRAndResumeInstructionPrefetch

```
// DisableITRAndResumeInstructionPrefetch() // ======================================== DisableITRAndResumeInstructionPrefetch();
```

## J1.3.1.58 ExecuteA64

```
// ExecuteA64() // ============ // Execute an A64 instruction in Debug state. ExecuteA64(bits(32) instr);
```

## J1.3.1.59 ExecuteT32

```
// ExecuteT32() // ============ // Execute a T32 instruction in Debug state. ExecuteT32(bits(16) hw1, bits(16) hw2);
```

## J1.3.1.60 ExitDebugState

```
// ExitDebugState() // ================ ExitDebugState() assert Halted(); SynchronizeContext();
```

```
// Although EDSCR.STATUS signals that the PE is restarting, debuggers must use EDPRSR.SDR to // detect that the PE has restarted. EDSCR.STATUS = '000001'; // Signal restarting // Clear any pending Halting debug events if IsFeatureImplemented(FEAT_Debugv8p8) then EDESR<3:0> = '0000'; else EDESR<2:0> = '000'; bits(64) new_pc; bits(64) spsr; if UsingAArch32() then new_pc = ZeroExtend(DLR, 64); if IsFeatureImplemented(FEAT_Debugv8p9) then spsr = DSPSR2 : DSPSR; else spsr = ZeroExtend(DSPSR, 64); else new_pc = DLR_EL0; spsr = DSPSR_EL0; constant boolean illegal_psr_state = IllegalExceptionReturn(spsr); // If this is an illegal return, SetPSTATEFromPSR() will set PSTATE.IL. SetPSTATEFromPSR(spsr); // Can update privileged bits, even at EL0 constant boolean branch_conditional = FALSE; if UsingAArch32() then if ConstrainUnpredictableBool(Unpredictable_RESTARTALIGNPC) then new_pc<0> = '0'; // AArch32 branch BranchTo(new_pc<31:0>, BranchType_DBGEXIT, branch_conditional); else // If targeting AArch32 then PC[63:32,1:0] might be set to UNKNOWN. if illegal_psr_state && spsr<4> == '1' then new_pc<63:32> = bits(32) UNKNOWN; new_pc<1:0> = bits(2) UNKNOWN; if IsFeatureImplemented(FEAT_BRBE) then BRBEDebugStateExit(new_pc); // A type of branch that is never predicted BranchTo(new_pc, BranchType_DBGEXIT, branch_conditional); (EDSCR.STATUS,EDPRSR.SDR) = ('000010','1'); // Atomically signal restarted EDPRSR.HALTED = '0'; UpdateEDSCRFields(); // Stop signalling PE state DisableITRAndResumeInstructionPrefetch(); return;
```

```
J1.3.1.61 Halt // Halt() // ====== Halt(bits(6) reason) constant boolean is_async = FALSE; constant FaultRecord fault = NoFault(); Halt(reason, is_async, fault); // Halt() // ====== Halt(bits(6) reason, boolean is_async, FaultRecord fault) CTI_SignalEvent(CrossTriggerIn_CrossHalt); // Trigger other cores to halt constant bits(64) preferred_restart_address = ThisInstrAddr(64);
```

```
bits(64) spsr = GetPSRFromPSTATE(DebugState, 64); if (IsFeatureImplemented(FEAT_BTI) && !is_async && ! reason IN {DebugHalt_Step_Normal, DebugHalt_Step_Exclusive, DebugHalt_Step_NoSyndrome, DebugHalt_Breakpoint, DebugHalt_HaltInstruction} && ConstrainUnpredictableBool(Unpredictable_ZEROBTYPE)) then spsr<11:10> = '00'; if UsingAArch32() then DLR = preferred_restart_address<31:0>; DSPSR = spsr<31:0>; if IsFeatureImplemented(FEAT_Debugv8p9) then DSPSR2 = spsr<63:32>; else DLR_EL0 = preferred_restart_address; DSPSR_EL0 = spsr; EDSCR.ITE = '1'; EDSCR.ITO = '0'; if IsFeatureImplemented(FEAT_RME) then if PSTATE.EL == EL3 then EDSCR.SDD = '0'; else EDSCR.SDD = if ExternalRootInvasiveDebugEnabled() then '0' else '1'; elsif CurrentSecurityState() == SS_Secure then EDSCR.SDD = '0'; // If entered in Secure state, allow debug elsif HaveEL(EL3) then EDSCR.SDD = if ExternalSecureInvasiveDebugEnabled() then '0' else '1'; else EDSCR.SDD = '1'; // Otherwise EDSCR.SDD is RES1 EDSCR.MA = '0'; // In Debug state: // * PSTATE.{SS,SSBS,D,A,I,F} are not observable and ignored so behave-as-if UNKNOWN. // * PSTATE.{N,Z,C,V,Q,GE,E,M,nRW,EL,SP,DIT} are also not observable, but since these // are not changed on exception entry, this function also leaves them unchanged. // * PSTATE.{IT,T} are ignored. // * PSTATE.IL is ignored and behave-as-if 0. // * PSTATE.BTYPE is ignored and behave-as-if 0. // * PSTATE.TCO is set 1. // * PSTATE.PACM is ignored and behave-as-if 0. // * PSTATE.{UAO,PAN} are observable and not changed on entry into Debug state. // * PSTATE.UINJ is set to 0. if UsingAArch32() then PSTATE.<IT,SS,SSBS,A,I,F,T> = bits(14) UNKNOWN; else PSTATE.<SS,SSBS,D,A,I,F> = bits(6) UNKNOWN; if IsFeatureImplemented(FEAT_MTE) then PSTATE.TCO = '1'; if IsFeatureImplemented(FEAT_BTI) then PSTATE.BTYPE = '00'; if IsFeatureImplemented(FEAT_PAuth_LR) then PSTATE.PACM = '0'; PSTATE.IL = '0'; if IsFeatureImplemented(FEAT_UINJ) then PSTATE.UINJ = '0'; if IsFeatureImplemented(FEAT_BRBE) then BRBEDebugStateEntry(preferred_restart_address); StopInstructionPrefetchAndEnableITR(); (EDSCR.STATUS,EDPRSR.HALTED) = (reason,'1'); UpdateEDSCRFields(); // Update EDSCR PE state flags. if IsFeatureImplemented(FEAT_EDHSR) then UpdateEDHSR(reason, fault); // Update EDHSR fields. if !is_async then EndOfInstruction(); return;
```

J1.3.1.62 HaltOnBreakpointOrWatchpoint

```
// HaltOnBreakpointOrWatchpoint() // ============================== // Returns TRUE if the Breakpoint and Watchpoint debug events should be considered for Debug // state entry, FALSE if they should be considered for a debug exception. boolean HaltOnBreakpointOrWatchpoint() return HaltingAllowed() && EDSCR.HDE == '1' && OSLSR_EL1.OSLK == '0';
```

## J1.3.1.63 Halted // Halted() // ======== boolean Halted() return ! EDSCR.STATUS IN {'000001', '000010'}; // Halted J1.3.1.64 HaltingAllowed // HaltingAllowed() // ================ // Returns TRUE if halting is currently allowed, FALSE if halting is prohibited. boolean HaltingAllowed() if Halted() || DoubleLockStatus() then return FALSE; ss = CurrentSecurityState(); case ss of when SS\_NonSecure return ExternalInvasiveDebugEnabled(); when SS\_Secure return ExternalSecureInvasiveDebugEnabled(); when SS\_Root return ExternalRootInvasiveDebugEnabled(); when SS\_Realm return ExternalRealmInvasiveDebugEnabled(); J1.3.1.65 Restarting // Restarting() // ============ boolean Restarting() return EDSCR.STATUS == '000001'; // Restarting J1.3.1.66 StopInstructionPrefetchAndEnableITR // StopInstructionPrefetchAndEnableITR() // ===================================== StopInstructionPrefetchAndEnableITR(); J1.3.1.67 UpdateDbgAuthStatus for debug.

```
// UpdateDbgAuthStatus() // ===================== // Provides information about the state of the // IMPLEMENTATION DEFINED authentication interface UpdateDbgAuthStatus() bits(2) nsid, nsnid; bits(2) sid, snid;
```

```
bits(2) rlid, rtid; if SecureOnlyImplementation() then nsid = '00'; elsif ExternalInvasiveDebugEnabled() then nsid = '11'; // Non-secure Invasive debug implemented and enabled. else nsid = '10'; // Non-secure Invasive debug implemented and disabled. if SecureOnlyImplementation() then nsnid = '00'; elsif ExternalNoninvasiveDebugEnabled() then nsnid = '11'; // Non-secure Non-Invasive debug implemented and enabled. else nsnid = '10'; // Non-secure Non-Invasive debug implemented and disabled. if !HaveSecureState() then sid = '00'; elsif ExternalSecureInvasiveDebugEnabled() then sid = '11'; // Secure Invasive debug implemented and enabled. else sid = '10'; // Secure Invasive debug implemented and disabled. if !HaveSecureState() then snid = '00'; elsif ExternalSecureNoninvasiveDebugEnabled() then snid = '11'; // Secure Non-Invasive debug implemented and enabled. else snid = '10'; // Secure Non-Invasive debug implemented and disabled. if !IsFeatureImplemented(FEAT_RME) then rlid = '00'; elsif ExternalRealmInvasiveDebugEnabled() then rlid = '11'; // Realm Invasive debug implemented and enabled. else rlid = '10'; // Realm Invasive debug implemented and disabled. if !IsFeatureImplemented(FEAT_RME) then rtid = '00'; elsif ExternalRootInvasiveDebugEnabled() then rtid = '11'; // Root Invasive debug implemented and enabled. else rtid = '10'; // Root Invasive debug implemented and disabled. DBGAUTHSTATUS_EL1.NSID = nsid; DBGAUTHSTATUS_EL1.NSNID = nsnid; DBGAUTHSTATUS_EL1.SID = sid; DBGAUTHSTATUS_EL1.SNID = snid; DBGAUTHSTATUS_EL1.RLID = rlid; DBGAUTHSTATUS_EL1.RLNID = rlid; // Field has the same value as DBGAUTHSTATUS_EL1.RLID. DBGAUTHSTATUS_EL1.RTID = rtid; DBGAUTHSTATUS_EL1.RTNID = rtid; // Field has the same value as DBGAUTHSTATUS_EL1.RTID. return;
```

## J1.3.1.68 UpdateEDHSR

```
// UpdateEDHSR() // ============= // Update EDHSR watchpoint related fields. UpdateEDHSR(bits(6) reason, FaultRecord fault) bits(64) syndrome = Zeros(64); if reason == DebugHalt_Watchpoint then if IsFeatureImplemented(FEAT_GCS) && fault.accessdesc.acctype == AccessType_GCS then syndrome<40> = '1'; // GCS syndrome<23:0> = WatchpointRelatedSyndrome(fault);
```

```
if IsFeatureImplemented(FEAT_Debugv8p9) then if fault.write then syndrome<6> = '1'; // WnR if fault.accessdesc.acctype IN {AccessType_DC, AccessType_IC, AccessType_AT} then syndrome<8> = '1'; // CM if IsFeatureImplemented(FEAT_NV2) && fault.accessdesc.acctype == AccessType_NV2 then syndrome<13> = '1'; // VNCR else syndrome = bits(64) UNKNOWN; EDHSR = syndrome;
```

## J1.3.1.69 UpdateEDSCRFields

```
// UpdateEDSCRFields() // =================== // Update EDSCR PE state fields UpdateEDSCRFields() if !Halted() then EDSCR.EL = '00'; if IsFeatureImplemented(FEAT_RME) then // SDD bit. EDSCR.SDD = if ExternalRootInvasiveDebugEnabled() then '0' else '1'; EDSCR.<NSE,NS> = bits(2) UNKNOWN; else // SDD bit. EDSCR.SDD = if ExternalSecureInvasiveDebugEnabled() then '0' else '1'; EDSCR.NS = bit UNKNOWN; EDSCR.RW = '1111'; else EDSCR.EL = PSTATE.EL; // SError Pending. if EL2Enabled() && HCR_EL2.<AMO,TGE> == '10' && PSTATE.EL IN {EL0,EL1} then EDSCR.A = if IsVirtualSErrorPending() then '1' else '0'; elsif (IsFeatureImplemented(FEAT_E3DSE) && SCR_EL3.EnDSE == '1' && PSTATE.EL IN {EL0,EL1,EL2}) then EDSCR.A = if IsDelegatedSErrorPending() then '1' else '0'; else EDSCR.A = if IsPhysicalSErrorPending() then '1' else '0'; ss = CurrentSecurityState(); if IsFeatureImplemented(FEAT_RME) then case ss of when SS_Secure EDSCR.<NSE,NS> = '00'; when SS_NonSecure EDSCR.<NSE,NS> = '01'; when SS_Root EDSCR.<NSE,NS> = '10'; when SS_Realm EDSCR.<NSE,NS> = '11'; else EDSCR.NS = if ss == SS_Secure then '0' else '1'; bits(4) RW; RW<1> = if ELUsingAArch32(EL1) then '0' else '1'; if PSTATE.EL != EL0 then RW<0> = RW<1>; else RW<0> = if UsingAArch32() then '0' else '1'; if !EL2Enabled() then RW<2> = RW<1>; else RW<2> = if ELUsingAArch32(EL2) then '0' else '1'; if !HaveEL(EL3) then RW<3> = RW<2>; else RW<3> = if ELUsingAArch32(EL3) then '0' else '1';
```

```
// The least-significant bits of EDSCR.RW are UNKNOWN if any higher EL is using AArch32. if RW<3> == '0' then RW<2:0> = bits(3) UNKNOWN; elsif RW<2> == '0' then RW<1:0> = bits(2) UNKNOWN; elsif RW<1> == '0' then RW<0> = bit UNKNOWN; EDSCR.RW = RW; return;
```

```
J1.3.1.70 CheckEDBGRQ // CheckEDBGRQ() // ============= // Checks IMPLEMENTATION DEFINED EDBGRQ Input Signal of external debug interface. // This is an example of an IMPLEMENTATION DEFINED source of External Debug Request debug events. CheckEDBGRQ() if EDBGRQ == HIGH then ExternalDebugRequest(); J1.3.1.71 CheckExceptionCatch
```

```
// CheckExceptionCatch() // ===================== // Check whether an Exception Catch debug event is set on the current Exception level CheckExceptionCatch(boolean exception_entry) // Called after an exception entry or exit, that is, such that the Security state // and PSTATE.EL are correct for the exception target. When FEAT_Debugv8p2 // is not implemented, this function might also be called at any time. ss = SecurityStateAtEL(PSTATE.EL); integer base; case ss of when SS_Secure base = 0; when SS_NonSecure base = 4; when SS_Realm base = 16; when SS_Root base = 0; if HaltingAllowed() then boolean halt; if IsFeatureImplemented(FEAT_Debugv8p2) then exception_exit = !exception_entry; increment = if ss == SS_Realm then 4 else 8; ctrl = EDECCR<UInt(PSTATE.EL) + base + increment>:EDECCR<UInt(PSTATE.EL) + base>; case ctrl of when '00' halt = FALSE; when '01' halt = TRUE; when '10' halt = (exception_exit == TRUE); when '11' halt = (exception_entry == TRUE); else halt = (EDECCR<UInt(PSTATE.EL) + base> == '1'); if halt then if IsFeatureImplemented(FEAT_Debugv8p8) && exception_entry then EDESR.EC = '1'; else Halt(DebugHalt_ExceptionCatch);
```

## J1.3.1.72 CheckExternalDebugRequestEvents

```
// CheckExternalDebugRequestEvents() // ================================= // Checks for all External Debug Request debug CheckExternalDebugRequestEvents() CheckTRBEHalt(); CheckPMUHalt(); CheckEDBGRQ(); return;
```

```
events. J1.3.1.73 CheckHaltingStep // CheckHaltingStep() // ================== // Check whether EDESR.SS has been set by Halting Step CheckHaltingStep(boolean is_async) step_enabled = EDECR.SS == '1' && HaltingAllowed(); active_pending = step_enabled && EDESR.SS == '1'; if active_pending then if HaltingStep_DidNotStep() then constant FaultRecord fault = NoFault(); Halt(DebugHalt_Step_NoSyndrome, is_async, fault); elsif HaltingStep_SteppedEX() then constant FaultRecord fault = NoFault(); Halt(DebugHalt_Step_Exclusive, is_async, fault); else constant FaultRecord fault = NoFault(); Halt(DebugHalt_Step_Normal, is_async, fault); if step_enabled then ShouldAdvanceHS = TRUE; return; J1.3.1.74 CheckOSUnlockCatch // CheckOSUnlockCatch() // ==================== // Called on unlocking the OS Lock to pend an OS Unlock Catch debug event CheckOSUnlockCatch() if ((IsFeatureImplemented(FEAT_DoPD) && CTIDEVCTL.OSUCE == '1') || (!IsFeatureImplemented(FEAT_DoPD) && EDECR.OSUCE == '1')) then if !Halted() then EDESR.OSUC = '1'; J1.3.1.75 CheckPMUHalt
```

```
// CheckPMUHalt() // ============== CheckPMUHalt() if !IsFeatureImplemented(FEAT_Debugv8p9) || !IsFeatureImplemented(FEAT_PMUv3p9) then return; // The request remains set until the condition is cleared. // For example, an interrupt handler or cross-triggered event handler clears // the overflow status flag by writing to PMOVSCLR_EL0 constant boolean include_r1 = TRUE; constant boolean include_r2 = TRUE; constant boolean include_r3 = TRUE;
```

```
constant boolean pmuhalt = CheckPMUOverflowCondition(PMUOverflowCondition_EDBGRQ, include_r1, include_r2, include_r3); if pmuhalt && EDECR.PME == '1' then ExternalDebugRequest();
```

## J1.3.1.76 CheckPendingExceptionCatch

```
// CheckPendingExceptionCatch() // ============================ // Check whether EDESR.EC has been set by an Exception Catch debug event. CheckPendingExceptionCatch(boolean is_async) if IsFeatureImplemented(FEAT_Debugv8p8) && HaltingAllowed() && EDESR.EC == '1' then constant FaultRecord fault = NoFault(); Halt(DebugHalt_ExceptionCatch, is_async, fault);
```

## J1.3.1.77 CheckPendingOSUnlockCatch

```
// CheckPendingOSUnlockCatch() // =========================== // Check whether EDESR.OSUC has been set by an OS Unlock Catch debug event CheckPendingOSUnlockCatch() if HaltingAllowed() && EDESR.OSUC == '1' then constant boolean is_async = TRUE; constant FaultRecord fault = NoFault(); Halt(DebugHalt_OSUnlockCatch, is_async, fault);
```

## J1.3.1.78 CheckPendingResetCatch

```
// CheckPendingResetCatch() // ======================== // Check whether EDESR.RC has been set by a Reset Catch debug event CheckPendingResetCatch() if HaltingAllowed() && EDESR.RC == '1' then constant boolean is_async = TRUE; constant FaultRecord fault = NoFault(); Halt(DebugHalt_ResetCatch, is_async, fault);
```

## J1.3.1.79 CheckResetCatch

```
// CheckResetCatch() // ================= // Called after reset CheckResetCatch() if ((IsFeatureImplemented(FEAT_DoPD) && CTIDEVCTL.RCE == '1') || (!IsFeatureImplemented(FEAT_DoPD) && EDECR.RCE == '1')) then EDESR.RC = '1'; // If halting is allowed then halt immediately if HaltingAllowed() then Halt(DebugHalt_ResetCatch);
```

## J1.3.1.80 CheckSoftwareAccessToDebugRegisters

```
// CheckSoftwareAccessToDebugRegisters() // ===================================== // Check for access to Breakpoint and Watchpoint registers. CheckSoftwareAccessToDebugRegisters() os_lock = (if ELUsingAArch32(EL1) then DBGOSLSR.OSLK else OSLSR_EL1.OSLK); if HaltingAllowed() && EDSCR.TDA == '1' && os_lock == '0' then Halt(DebugHalt_SoftwareAccess);
```

## J1.3.1.81 CheckTRBEHalt

```
// CheckTRBEHalt() // =============== CheckTRBEHalt() if !IsFeatureImplemented(FEAT_Debugv8p9) || !IsFeatureImplemented(FEAT_TRBE_EXT) then return; if TraceBufferEnabled() && TRBSR_EL1.IRQ == '1' && EDECR.TRBE == '1' then ExternalDebugRequest();
```

## J1.3.1.82 EDBGRQ

```
Signal EDBGRQ; // Input Signal in external debug interface
```

## J1.3.1.83 ExternalDebugRequest

```
// ExternalDebugRequest() // ====================== ExternalDebugRequest() if HaltingAllowed() then constant boolean is_async = TRUE; constant FaultRecord fault = NoFault(); Halt(DebugHalt_EDBGRQ, is_async, fault); // Otherwise the CTI continues to assert the debug request until it is taken.
```

## J1.3.1.84 HSAdvance

```
// HSAdvance() // =========== // Advance the Halting Step State Machine HSAdvance() if !ShouldAdvanceHS then return; step_enabled = EDECR.SS == '1' && HaltingAllowed(); active_not_pending = step_enabled && EDESR.SS == '0'; if active_not_pending then EDESR.SS = '1'; // set as ShouldAdvanceHS = FALSE; return;
```

```
pending.
```

## J1.3.1.85 HaltingStep\_DidNotStep

```
// HaltingStep_DidNotStep() // ======================== // Returns TRUE if the previously executed instruction was executed in the inactive state, that is, // if it was not itself stepped. boolean HaltingStep_DidNotStep();
```

## J1.3.1.86 HaltingStep\_SteppedEX // HaltingStep\_SteppedEX() // ======================= // Returns TRUE if the previously executed instruction was a Load-Exclusive class instruction // executed in the active-not-pending state. boolean HaltingStep\_SteppedEX(); J1.3.1.87 ExternalDebugInterruptsDisabled // ExternalDebugInterruptsDisabled() // ================================= // Determine whether EDSCR disables interrupts routed to 'target'. boolean ExternalDebugInterruptsDisabled(bits(2) target) boolean int\_dis; constant SecurityState ss = SecurityStateAtEL(target); if IsFeatureImplemented(FEAT\_Debugv8p4) then if EDSCR.INTdis&lt;0&gt; == '1' then case ss of when SS\_NonSecure int\_dis = ExternalInvasiveDebugEnabled(); when SS\_Secure int\_dis = ExternalSecureInvasiveDebugEnabled(); when SS\_Realm int\_dis = ExternalRealmInvasiveDebugEnabled(); when SS\_Root int\_dis = ExternalRootInvasiveDebugEnabled(); else int\_dis = FALSE; else case target of when EL3 int\_dis = (EDSCR.INTdis == '11' &amp;&amp; ExternalSecureInvasiveDebugEnabled()); when EL2 int\_dis = (EDSCR.INTdis == '1x' &amp;&amp; ExternalInvasiveDebugEnabled()); when EL1 if ss == SS\_Secure then int\_dis = (EDSCR.INTdis == '1x' &amp;&amp; ExternalSecureInvasiveDebugEnabled()); else int\_dis = (EDSCR.INTdis != '00' &amp;&amp; ExternalInvasiveDebugEnabled()); return int\_dis; J1.3.1.88 pmu array integer PMUEventAccumulator[0..30]; // Accumulates PMU events for a cycle array boolean PMULastThresholdValue[0..30];// A record of the threshold result for each J1.3.1.89 CYCLE\_COUNTER\_ID counter.

```
// Constant used in PMU functions to represent actions on the cycle constant integer CYCLE_COUNTER_ID = 31;
```

## J1.3.1.90 CheckForPMUOverflow

```
// CheckForPMUOverflow() // ===================== // Called before each instruction is executed. // If a PMU event counter has overflowed, this function might do any of: // -Signal a Performance Monitors overflow interrupt request. // -Signal a CTI Performance Monitors overflow event. // -Generate an External Debug Request debug event. // -Generate a BRBE freeze event. CheckForPMUOverflow() constant boolean include_r1 = TRUE; constant boolean include_r2 = TRUE; constant boolean include_r3 = TRUE; constant boolean enabled = PMUInterruptEnabled(); constant boolean pmuirq = CheckPMUOverflowCondition(PMUOverflowCondition_IRQ, include_r1, SetInterruptRequestLevel(InterruptID_PMUIRQ, if enabled && pmuirq then HIGH else LOW); CTI_SetEventLevel(CrossTriggerIn_PMUOverflow, if pmuirq then HIGH else LOW); if ShouldBRBEFreeze() then BRBEFreeze(); return;
```

```
// CheckPMUOverflowCondition() // =========================== // Checks for PMU overflow under certain parameter conditions described by 'reason'. // If 'include_r1' is TRUE, then check counters in the range [0..(HPMN-1)], CCNTR // and ICNTR, unless excluded by 'reason'. // If 'include_r2' is TRUE, then check counters in the range [HPMN..(EPMN-1)]. // If 'include_r3' is TRUE, then check counters in the range [EPMN..(N-1)]. boolean CheckPMUOverflowCondition(PMUOverflowCondition reason, boolean include_r1, boolean include_r2, boolean // 'reason' is decoded into a further set of parameters: // If 'check_e' is TRUE, then check the applicable one of PMCR_EL0.E and MDCR_EL2.HPME. // If 'check_inten' is TRUE, then check the applicable PMINTENCLR_EL1 bit. // If 'exclude_cyc' is TRUE, then CCNTR is NOT checked. // If 'exclude_sync' is TRUE, then counters in synchronous mode are NOT checked. boolean check_e; boolean check_inten; boolean exclude_cyc; boolean exclude_sync; case reason of when PMUOverflowCondition_PMUException check_e = TRUE; check_inten = TRUE; exclude_cyc = FALSE; exclude_sync = IsFeatureImplemented(FEAT_SEBEP); when PMUOverflowCondition_BRBEFreeze check_e = FALSE; check_inten = FALSE; exclude_cyc = TRUE; exclude_sync = IsFeatureImplemented(FEAT_SEBEP);
```

```
include_r2, include_r3); J1.3.1.91 CheckPMUOverflowCondition include_r3)
```

```
when PMUOverflowCondition_Freeze check_e = FALSE; check_inten = FALSE; exclude_cyc = TRUE; exclude_sync = IsFeatureImplemented(FEAT_SEBEP); when PMUOverflowCondition_IRQ, PMUOverflowCondition_EDBGRQ check_e = TRUE; check_inten = TRUE; exclude_cyc = FALSE; exclude_sync = FALSE; otherwise Unreachable(); bits(64) ovsf; if HaveAArch64() then ovsf = PMOVSSET_EL0; ovsf<63:33> = Zeros(31); if !IsFeatureImplemented(FEAT_PMUv3_ICNTR) then ovsf<INSTRUCTION_COUNTER_ID> = '0'; else ovsf = ZeroExtend(PMOVSSET, 64); constant integer counters = NUM_PMU_COUNTERS; // Remove unimplemented counters -these fields are RES0 if counters < 31 then ovsf<30:counters> = Zeros(31-counters); for idx = 0 to counters - 1 bit global_en; case GetPMUCounterRange(idx) of when PMUCounterRange_R1 global_en = if HaveAArch64() then PMCR_EL0.E else PMCR.E; if !include_r1 then ovsf<idx> = '0'; when PMUCounterRange_R2 global_en = if HaveAArch64() then MDCR_EL2.HPME else HDCR.HPME; if !include_r2 then ovsf<idx> = '0'; when PMUCounterRange_R3 global_en = PMCCR.EPME; if !include_r3 then ovsf<idx> = '0'; otherwise Unreachable(); if exclude_sync then constant bit sync = PMEVTYPER_EL0[idx].SYNC; ovsf<idx> = ovsf<idx> AND NOT sync; if check_e then ovsf<idx> = ovsf<idx> AND global_en; // Cycle counter if exclude_cyc || !include_r1 then ovsf<CYCLE_COUNTER_ID> = '0'; if check_e then ovsf<CYCLE_COUNTER_ID> = ovsf<CYCLE_COUNTER_ID> AND PMCR_EL0.E; // Instruction counter if HaveAArch64() && IsFeatureImplemented(FEAT_PMUv3_ICNTR) then if !include_r1 then ovsf<INSTRUCTION_COUNTER_ID> = '0'; if exclude_sync then constant bit sync = PMICFILTR_EL0.SYNC; ovsf<INSTRUCTION_COUNTER_ID> = ovsf<INSTRUCTION_COUNTER_ID> AND NOT sync; if check_e then
```

```
ovsf<INSTRUCTION_COUNTER_ID> = ovsf<INSTRUCTION_COUNTER_ID> AND PMCR_EL0.E; if check_inten then constant bits(64) inten = (if HaveAArch64() then PMINTENCLR_EL1 else ZeroExtend(PMINTENCLR, 64)); ovsf = ovsf AND inten; return !IsZero(ovsf);
```

## J1.3.1.92 ClearEventCounters

```
// ClearEventCounters() // ==================== // Zero all the event counters. // Called on a write to PMCR_EL0 or PMCR that writes '1' to PMCR_EL0.P or PMCR.P. ClearEventCounters() // Although ZeroPMUCounters implements the functionality for PMUACR_EL1 // that is part of FEAT_PMUv3p9, it should be noted that writes to // PMCR_EL0 are not allowed at EL0 when PMUSERENR_EL0.UEN is 1, meaning // it is not relevant in this case. ZeroPMUCounters(Zeros(33) : Ones(31));
```

## J1.3.1.93 CountPMUEvents

```
// CountPMUEvents() // ================ // Return TRUE if counter "idx" should count its event. // For the cycle counter, idx == CYCLE_COUNTER_ID (31). // For the instruction counter, idx == INSTRUCTION_COUNTER_ID (32). boolean CountPMUEvents(integer idx) constant integer counters = NUM_PMU_COUNTERS; assert (idx == CYCLE_COUNTER_ID || idx < counters || (idx == INSTRUCTION_COUNTER_ID && IsFeatureImplemented(FEAT_PMUv3_ICNTR))); boolean debug; boolean enabled; boolean prohibited; boolean filtered; boolean frozen; // Event counting is disabled in Debug state debug = Halted(); // Software can reserve some counters constant PMUCounterRange counter_range = GetPMUCounterRange(idx); ss = CurrentSecurityState(); // Main enable controls bit global_en; bit counter_en; case counter_range of when PMUCounterRange_R1 global_en = if HaveAArch64() then PMCR_EL0.E else PMCR.E; when PMUCounterRange_R2 global_en = if HaveAArch64() then MDCR_EL2.HPME else HDCR.HPME; when PMUCounterRange_R3 assert IsFeatureImplemented(FEAT_PMUv3_EXTPMN); global_en = PMCCR.EPME; otherwise Unreachable();
```

```
case idx of when INSTRUCTION_COUNTER_ID assert HaveAArch64(); counter_en = PMCNTENSET_EL0.F0; when CYCLE_COUNTER_ID counter_en = if HaveAArch64() then PMCNTENSET_EL0.C else PMCNTENSET.C; otherwise counter_en = if HaveAArch64() then PMCNTENSET_EL0<idx> else PMCNTENSET<idx>; // Event counter <n> does not count when all of the following are true: // -FEAT_SEBEP is implemented // -PMEVTYPER<n>_EL0.SYNC == 1 // -Event counter <n> is configured to count an event that is not a synchronous event if (IsFeatureImplemented(FEAT_SEBEP) && PMEVTYPER_EL0[idx].SYNC == '1' && !IsSupportingPMUSynchronousMode(PMEVTYPER_EL0[idx].evtCount)) then counter_en = '0'; enabled = global_en == '1' && counter_en == '1'; // Event counting is allowed unless it is prohibited by any rule below prohibited = FALSE; // Event counting in Secure state or at EL3 is prohibited if all of: // * EL3 is implemented // * One of the following is true: // -EL3 is using AArch64, MDCR_EL3.SPME == 0, and either: // - FEAT_PMUv3p7 is not implemented // - MDCR_EL3.MPMX == 0 // -EL3 is using AArch32 and SDCR.SPME == 0 // * Either not executing at EL0 using AArch32, or one of the following is true: // -EL3 is using AArch32 and SDER.SUNIDEN == 0 // -EL3 is using AArch64, EL1 is using AArch32, and SDER32_EL3.SUNIDEN == 0 // * PMNx is not reserved for use by the external interface if (HaveEL(EL3) && (ss == SS_Secure || PSTATE.EL == EL3) && counter_range != PMUCounterRange_R3) then if !ELUsingAArch32(EL3) then prohibited = (MDCR_EL3.SPME == '0' && (!IsFeatureImplemented(FEAT_PMUv3p7) || MDCR_EL3.MPMX == '0')); else prohibited = SDCR.SPME == '0'; if prohibited && PSTATE.EL == EL0 then if ELUsingAArch32(EL3) then prohibited = SDER.SUNIDEN == '0'; elsif ELUsingAArch32(EL1) then prohibited = SDER32_EL3.SUNIDEN == '0'; // Event counting at EL3 is prohibited if all of: // * FEAT_PMUv3p7 is implemented // * EL3 is using AArch64 // * One of the following is true: // -MDCR_EL3.SPME == 0 // -PMNx is not reserved for EL2 // * MDCR_EL3.MPMX == 1 // * PMNx is not reserved for use by the external interface if (!prohibited && IsFeatureImplemented(FEAT_PMUv3p7) && PSTATE.EL == EL3 && HaveAArch64() && counter_range != PMUCounterRange_R3) then prohibited = (MDCR_EL3.MPMX == '1' && (MDCR_EL3.SPME == '0' || counter_range == PMUCounterRange_R1)); // Event counting at EL2 is prohibited if all of: // * FEAT_PMUv3p1 is implemented // * PMNx is not reserved for EL2 or the external interface // * EL2 is using AArch64 and MDCR_EL2.HPMD == 1, or EL2 is using AArch32 and HDCR.HPMD == 1 if (!prohibited && PSTATE.EL == EL2 && IsFeatureImplemented(FEAT_PMUv3p1) && counter_range == PMUCounterRange_R1) then hpmd = if HaveAArch64() then MDCR_EL2.HPMD else HDCR.HPMD;
```

```
prohibited = hpmd == '1'; // The IMPLEMENTATION DEFINED authentication interface might override software if prohibited && !IsFeatureImplemented(FEAT_Debugv8p2) then prohibited = !ExternalSecureNoninvasiveDebugEnabled(); // If FEAT_PMUv3p7 is implemented, event counting can be frozen if IsFeatureImplemented(FEAT_PMUv3p7) then bit fz; case counter_range of when PMUCounterRange_R1 fz = if HaveAArch64() then PMCR_EL0.FZO else PMCR.FZO; when PMUCounterRange_R2 fz = if HaveAArch64() then MDCR_EL2.HPMFZO else HDCR.HPMFZO; when PMUCounterRange_R3 fz = '0'; otherwise Unreachable(); frozen = (fz == '1') && ShouldPMUFreeze(counter_range); frozen = frozen || SPEFreezeOnEvent(idx); else frozen = FALSE; // PMCR_EL0.DP or PMCR.DP disables the cycle counter when event counting is prohibited // or frozen if (prohibited || frozen) && idx == CYCLE_COUNTER_ID then dp = if HaveAArch64() then PMCR_EL0.DP else PMCR.DP; enabled = enabled && dp == '0'; // Otherwise whether event counting is prohibited or frozen does not affect the cycle // counter prohibited = FALSE; frozen = FALSE; // If FEAT_PMUv3p5 is implemented, cycle counting can be prohibited. // This is not overridden by PMCR_EL0.DP. if IsFeatureImplemented(FEAT_PMUv3p5) && idx == CYCLE_COUNTER_ID then if HaveEL(EL3) && (ss == SS_Secure || PSTATE.EL == EL3) then sccd = if HaveAArch64() then MDCR_EL3.SCCD else SDCR.SCCD; if sccd == '1' then prohibited = TRUE; if PSTATE.EL == EL2 then hccd = if HaveAArch64() then MDCR_EL2.HCCD else HDCR.HCCD; if hccd == '1' then prohibited = TRUE; // If FEAT_PMUv3p7 is implemented, cycle counting an be prohibited at EL3. // This is not overriden by PMCR_EL0.DP. if IsFeatureImplemented(FEAT_PMUv3p7) && idx == CYCLE_COUNTER_ID then if PSTATE.EL == EL3 && HaveAArch64() && MDCR_EL3.MCCD == '1' then prohibited = TRUE; // Event counting can be filtered by the {P, U, NSK, NSU, NSH, M, SH, RLK, RLU, RLH} bits bits(32) filter; case idx of when INSTRUCTION_COUNTER_ID filter = PMICFILTR_EL0<31:0>; when CYCLE_COUNTER_ID filter = if HaveAArch64() then PMCCFILTR_EL0<31:0> else PMCCFILTR; otherwise filter = if HaveAArch64() then PMEVTYPER_EL0[idx]<31:0> else PMEVTYPER[idx]; p = filter<31>; u = filter<30>; nsk = if HaveEL(EL3) then filter<29> else '0'; nsu = if HaveEL(EL3) then filter<28> else '0';
```

```
nsh = if HaveEL(EL2) then filter<27> else '0'; m = if HaveEL(EL3) && HaveAArch64() then filter<26> else '0'; sh = if HaveEL(EL3) && IsFeatureImplemented(FEAT_SEL2) then filter<24> else '0'; rlk = if IsFeatureImplemented(FEAT_RME) then filter<22> else '0'; rlu = if IsFeatureImplemented(FEAT_RME) then filter<21> else '0'; rlh = if IsFeatureImplemented(FEAT_RME) then filter<20> else '0'; ss = CurrentSecurityState(); case PSTATE.EL of when EL0 case ss of when SS_NonSecure filtered = u != nsu; when SS_Secure filtered = u == '1'; when SS_Realm filtered = u != rlu; when EL1 case ss of when SS_NonSecure filtered = p != nsk; when SS_Secure filtered = p == '1'; when SS_Realm filtered = p != rlk; when EL2 case ss of when SS_NonSecure filtered = nsh == '0'; when SS_Secure filtered = nsh == sh; when SS_Realm filtered = nsh == rlh; when EL3 if HaveAArch64() then filtered = m != p; else filtered = p == '1'; if IsFeatureImplemented(FEAT_PMUv3_SME) then constant boolean is_streaming_mode = PSTATE.SM == '1'; bits(2) vs; case idx of when INSTRUCTION_COUNTER_ID vs = PMICFILTR_EL0.VS; when CYCLE_COUNTER_ID vs = PMCCFILTR_EL0.VS; otherwise vs = PMEVTYPER_EL0[idx].VS; boolean streaming_mode_filtered; if vs == '11' then streaming_mode_filtered = ConstrainUnpredictableBool(Unpredictable_RES_PMU_VS); else streaming_mode_filtered = ((is_streaming_mode && vs<0> == '1') || (!is_streaming_mode && vs<1> == '1')); filtered = filtered || streaming_mode_filtered; return !debug && enabled && !prohibited && !filtered && !frozen;
```

## J1.3.1.94 EffectiveEPMN

```
// EffectiveEPMN() // =============== // Returns the Effective value of PMCCR.EPMN. bits(5) EffectiveEPMN() constant integer counters = NUM_PMU_COUNTERS; bits(5) epmn_bits; if IsFeatureImplemented(FEAT_PMUv3_EXTPMN) then epmn_bits = PMCCR.EPMN; if UInt(epmn_bits) > counters then
```

```
(-, epmn_bits) = ConstrainUnpredictableBits(Unpredictable_RES_EPMN, 5); else epmn_bits = counters<4:0>; return epmn_bits;
```

## J1.3.1.95 EffectiveHPMN

```
// EffectiveHPMN() // =============== // Returns the Effective value of MDCR_EL2.HPMN or HDCR.HPMN. bits(5) EffectiveHPMN() constant integer counters = UInt(EffectiveEPMN()); bits(5) hpmn_bits; if HaveEL(EL2) then // Software can reserve some event counters for EL2 hpmn_bits = if HaveAArch64() then MDCR_EL2.HPMN else HDCR.HPMN; // When FEAT_PMUv3_EXTPMN is implemented, out of range values are capped. if UInt(hpmn_bits) > counters && IsFeatureImplemented(FEAT_PMUv3_EXTPMN) then hpmn_bits = counters<4:0>; if (UInt(hpmn_bits) > counters || (!IsFeatureImplemented(FEAT_HPMN0) && IsZero(hpmn_bits))) then (-, hpmn_bits) = ConstrainUnpredictableBits(Unpredictable_RES_HPMN, 5); else hpmn_bits = counters<4:0>; return hpmn_bits;
```

## J1.3.1.96 GetNumEventCountersAccessible

```
// GetNumEventCountersAccessible() // =============================== // Return the number of event counters that can be accessed at the current Exception level. integer GetNumEventCountersAccessible() integer n; // Software can reserve some counters for EL2 if PSTATE.EL IN {EL1, EL0} && EL2Enabled() then n = UInt(EffectiveHPMN()); else n = UInt(EffectiveEPMN()); return n;
```

## J1.3.1.97 GetNumEventCountersSelfHosted

```
// GetNumEventCountersSelfHosted() // =============================== // Return the number of event counters that can be accessed by the Self-hosted software. integer GetNumEventCountersSelfHosted() if IsFeatureImplemented(FEAT_PMUv3_EXTPMN) then return UInt(EffectiveEPMN()); else return NUM_PMU_COUNTERS;
```

## J1.3.1.98 GetPMUAccessMask

```
// GetPMUAccessMask() // ================== // Return a mask of the PMU counters accessible at the current Exception level bits(64) GetPMUAccessMask() bits(64) mask = Zeros(64); // PMICNTR_EL0 is only accessible at EL0 using AArch64 when PMUSERENR_EL0.UEN is if IsFeatureImplemented(FEAT_PMUv3_ICNTR) && !UsingAArch32() then assert IsFeatureImplemented(FEAT_PMUv3p9); if PSTATE.EL != EL0 || PMUSERENR_EL0.UEN == '1' then mask<INSTRUCTION_COUNTER_ID> = '1'; // PMCCNTR_EL0 is always implemented and accessible mask<CYCLE_COUNTER_ID> = '1'; // PMEVCNTR<n>_EL0 constant integer counters = GetNumEventCountersAccessible(); if counters > 0 then mask<counters-1:0> = Ones(counters); // Check EL0 ignore access conditions if (IsFeatureImplemented(FEAT_PMUv3p9) && !ELUsingAArch32(EL1) && PSTATE.EL == EL0 && PMUSERENR_EL0.UEN == '1') then mask = mask AND PMUACR_EL1; // User access control return mask;
```

```
// GetPMUReadMask() // ================ // Return a mask of the PMU counters that can be read at // Exception level.
```

## 1. J1.3.1.99 GetPMUCounterRange // GetPMUCounterRange() // ==================== // Returns the range that a counter is currently in. PMUCounterRange GetPMUCounterRange(integer n) constant integer counters = NUM\_PMU\_COUNTERS; constant integer epmn = UInt(EffectiveEPMN()); constant integer hpmn = UInt(EffectiveHPMN()); if n &lt; hpmn then return PMUCounterRange\_R1; elsif n &lt; epmn then return PMUCounterRange\_R2; elsif n &lt; counters then assert IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN); return PMUCounterRange\_R3; elsif n == CYCLE\_COUNTER\_ID then return PMUCounterRange\_R1; elsif n == INSTRUCTION\_COUNTER\_ID then assert IsFeatureImplemented(FEAT\_PMUv3\_ICNTR); return PMUCounterRange\_R1; else Unreachable(); J1.3.1.100 GetPMUReadMask the current

```
// This mask masks reads from PMCNTENSET_EL0, PMCNTENCLR_EL0, PMINTENSET_EL1, // PMINTENCLR_EL1, PMOVSSET_EL0, and PMOVSCLR_EL0. bits(64) GetPMUReadMask() bits(64) mask = GetPMUAccessMask(); // Additional PMICNTR_EL0 accessibility checks. PMICNTR_EL0 controls read-as-zero // if a read of PMICFILTR_EL0 would be trapped to a higher Exception level. if IsFeatureImplemented(FEAT_PMUv3_ICNTR) && mask<INSTRUCTION_COUNTER_ID> == '1' then // Check for trap to EL3. if HaveEL(EL3) && PSTATE.EL != EL3 && MDCR_EL3.EnPM2 == '0' then mask<INSTRUCTION_COUNTER_ID> = '0'; // Check for trap to EL2. if EL2Enabled() && PSTATE.EL IN {EL0, EL1} && HCR_EL2.<E2H,TGE> != '11' then // If FEAT_PMUv3_ICNTR and EL2 are implemented, then so is FEAT_FGT2. assert IsFeatureImplemented(FEAT_FGT2); if ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || HDFGRTR2_EL2.nPMICFILTR_EL0 == '0') then mask<INSTRUCTION_COUNTER_ID> = '0'; // Traps on other counters do not affect those counters' controls in the same way. return mask; J1.3.1.101 GetPMUWriteMask
```

```
// GetPMUWriteMask() // ================= // Return a mask of the PMU counters writable at the current Exception level. // This mask masks writes to PMCNTENSET_EL0, PMCNTENCLR_EL0, PMINTENSET_EL1, // PMINTENCLR_EL1, PMOVSSET_EL0, PMOVSCLR_EL0, and PMZR_EL0. // 'write_counter' is TRUE for a write to PMZR_EL0, when the counter is being // updated, and FALSE for other cases when the controls are being updated. bits(64) GetPMUWriteMask(boolean write_counter) bits(64) mask = GetPMUAccessMask(); // Check EL0 ignore write conditions if (IsFeatureImplemented(FEAT_PMUv3p9) && !ELUsingAArch32(EL1) && PSTATE.EL == EL0 && PMUSERENR_EL0.UEN == '1') then if (IsFeatureImplemented(FEAT_PMUv3_ICNTR) && PMUSERENR_EL0.IR == '1') then // PMICNTR_EL0 read-only mask<INSTRUCTION_COUNTER_ID> = '0'; if PMUSERENR_EL0.CR == '1' then // PMCCNTR_EL0 read-only mask<CYCLE_COUNTER_ID> = '0'; if PMUSERENR_EL0.ER == '1' then // PMEVCNTR<n>_EL0 read-only mask<30:0> = Zeros(31); // Additional PMICNTR_EL0 accessibility checks. PMICNTR_EL0 controls ignore writes // if a write of PMICFILTR_EL0 would be trapped to a higher Exception level. // Indirect writes to PMICNTR_EL0 (through PMZR_EL0) are ignored if a write of // PMICNTR_EL0 would be trapped to a higher Exception level. if IsFeatureImplemented(FEAT_PMUv3_ICNTR) && mask<INSTRUCTION_COUNTER_ID> == '1' then // Check for trap to EL3. if HaveEL(EL3) && PSTATE.EL != EL3 && MDCR_EL3.EnPM2 == '0' then mask<INSTRUCTION_COUNTER_ID> = '0'; // Check for trap to EL2. if EL2Enabled() && PSTATE.EL IN {EL0, EL1} && HCR_EL2.<E2H,TGE> != '11' then // If FEAT_PMUv3_ICNTR and EL2 are implemented, then so is FEAT_FGT2. assert IsFeatureImplemented(FEAT_FGT2); fgt_bit = (if write_counter then HDFGWTR2_EL2.nPMICNTR_EL0 else HDFGWTR2_EL2.nPMICFILTR_EL0); if (HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || fgt_bit == '0' then
```

```
mask<INSTRUCTION_COUNTER_ID> = '0'; // Traps on other counters do not affect those counters' controls in the same way. return mask;
```

## J1.3.1.102 HasElapsed64Cycles

```
// HasElapsed64Cycles() // ==================== // Returns TRUE if 64 cycles have elapsed between the last count, and FALSE otherwise. boolean HasElapsed64Cycles();
```

## J1.3.1.103 INSTRUCTION\_COUNTER\_ID

```
// Constant used in PMU functions to represent actions on the instruction counter. constant integer INSTRUCTION_COUNTER_ID = 32;
```

## J1.3.1.104 IncrementInstructionCounter

```
// IncrementInstructionCounter() // ============================= // Increment the instruction counter and possibly set overflow bits. IncrementInstructionCounter(integer increment) if CountPMUEvents(INSTRUCTION_COUNTER_ID) then constant integer old_value = UInt(PMICNTR_EL0); constant integer new_value = old_value + increment; PMICNTR_EL0 = new_value<63:0>; // The effective value of PMCR_EL0.LP is '1' for the instruction counter if old_value<64> != new_value<64> then PMOVSSET_EL0.F0 = '1'; if (IsFeatureImplemented(FEAT_SEBEP) && PMINTENSET_EL1.F0 == '1' && PMOVSSET_EL0.F0 == '1' && increment != 0) then SyncCounterOverflowed = TRUE; return;
```

## J1.3.1.105 IsMostSecureAccess

```
// IsMostSecureAccess() // ==================== // Returns TRUE if the security state of an access is the most secure state. boolean IsMostSecureAccess(AddressDescriptor addrdesc) if IsFeatureImplemented(FEAT_RME) then return addrdesc.paddress.paspace == PAS_Root; elsif HaveEL(EL3) || SecureOnlyImplementation() then return addrdesc.paddress.paspace == PAS_Secure; else assert addrdesc.paddress.paspace == PAS_NonSecure; return TRUE;
```

## J1.3.1.106 IsRange3Counter

```
// IsRange3Counter() // ================= // Returns TRUE if the counter is in the third range. boolean IsRange3Counter(integer n) return PMUCounterRange_R3 == GetPMUCounterRange(n);
```

## J1.3.1.107 PMUCaptureEvent

```
// PMUCaptureEvent() // ================= // If permitted and enabled, generate a PMU snapshot Capture event. PMUCaptureEvent() assert HaveEL(EL3) && IsFeatureImplemented(FEAT_PMUv3_SS) && HaveAArch64(); constant boolean debug_state = Halted(); if !PMUCaptureEventAllowed() then // Indicate a Capture event completed, unsuccessfully PMSSCR_EL1.<NC,SS> = '10'; return; constant integer counters = NUM_PMU_COUNTERS; for idx = 0 to counters - 1 PMEVCNTSVR_EL1[idx] = PMEVCNTR_EL0[idx]; PMCCNTSVR_EL1 = PMCCNTR_EL0; if IsFeatureImplemented(FEAT_PMUv3_ICNTR) then PMICNTSVR_EL1 = PMICNTR_EL0; if IsFeatureImplemented(FEAT_PCSRv8p9) && PMPCSCTL.SS == '1' then if pc_sample.valid && !debug_state then SetPCSRActive(); SetPCSample(); else PMPCSR<31:0> = Ones(32); if (IsFeatureImplemented(FEAT_BRBE) && BranchRecordAllowed(PSTATE.EL) && BRBCR_EL1.FZPSS == '1' && (!HaveEL(EL2) || BRBCR_EL2.FZPSS == '1')) then BRBEFreeze(); // Indicate a successful Capture event PMSSCR_EL1.<NC,SS> = '00'; if !debug_state || ConstrainUnpredictableBool(Unpredictable_PMUSNAPSHOTEVENT) then PMUEvent(PMU_EVENT_PMU_SNAPSHOT); return;
```

## J1.3.1.108 PMUCaptureEventAllowed

```
// PMUCaptureEventAllowed() // ======================== // Returns TRUE if PMU Capture events are allowed, and FALSE otherwise. boolean PMUCaptureEventAllowed() if !IsFeatureImplemented(FEAT_PMUv3_SS) || !HaveAArch64() then return FALSE; if !PMUCaptureEventEnabled() || OSLockStatus() then return FALSE; elsif HaveEL(EL3) && MDCR_EL3.PMSSE != '01' then return MDCR_EL3.PMSSE == '11';
```

```
elsif HaveEL(EL2) && MDCR_EL2.PMSSE != '01' then return MDCR_EL2.PMSSE == '11'; else bits(2) pmsse_el1 = PMECR_EL1.SSE; if pmsse_el1 == '01' then // Reserved value Constraint c; (c, pmsse_el1) = assert c IN {Constraint_DISABLED, Constraint_UNKNOWN}; if c == Constraint_DISABLED then pmsse_el1 = '00'; // Otherwise the value returned by ConstrainUnpredictableBits must be // a non-reserved value return pmsse_el1 == '11';
```

```
// PMUCountValue() // =============== // Implements the PMU threshold function, if implemented. // Returns the value to increment event counter 'n' by. // 'Vb' is the base value of the event that event counter 'n' is configured to count. // 'Vm' is the value to increment event counter 'n-1' by if 'n' is odd, zero integer PMUCountValue(integer n, integer Vb, integer Vm) assert (n MOD 2) == 1 || Vm == 0; assert n < NUM_PMU_COUNTERS; if !IsFeatureImplemented(FEAT_PMUv3_TH) || !HaveAArch64() then return Vb; constant integer TH = UInt(PMEVTYPER_EL0[n].TH); // Control register fields bits(3) tc = PMEVTYPER_EL0[n].TC; bit te = '0'; if IsFeatureImplemented(FEAT_PMUv3_EDGE) then
```

```
ConstrainUnpredictableBits(Unpredictable_RESPMSSE, 2); J1.3.1.109 PMUCaptureEventEnabled // PMUCaptureEventEnabled() // ======================== // Returns TRUE if PMU Capture events are enabled, and FALSE otherwise. boolean PMUCaptureEventEnabled() if !IsFeatureImplemented(FEAT_PMUv3_SS) || !HaveAArch64() then return FALSE; if HaveEL(EL3) && MDCR_EL3.PMSSE != '01' then return MDCR_EL3.PMSSE == '1x'; elsif HaveEL(EL2) && ELUsingAArch32(EL2) then return FALSE; elsif HaveEL(EL2) && MDCR_EL2.PMSSE != '01' then return MDCR_EL2.PMSSE == '1x'; elsif ELUsingAArch32(EL1) then return FALSE; else bits(2) pmsse_el1 = PMECR_EL1.SSE; if pmsse_el1 == '01' then // Reserved value Constraint c; (c, pmsse_el1) = ConstrainUnpredictableBits(Unpredictable_RESPMSSE, 2); assert c IN {Constraint_DISABLED, Constraint_UNKNOWN}; if c == Constraint_DISABLED then pmsse_el1 = '00'; // Otherwise the value returned by ConstrainUnpredictableBits must be // a non-reserved value return pmsse_el1 == '1x'; J1.3.1.110 PMUCountValue otherwise.
```

```
te = PMEVTYPER_EL0[n].TE; bits(2) tlc = '00'; if IsFeatureImplemented(FEAT_PMUv3_TH2) && (n MOD 2) == 1 then tlc = PMEVTYPER_EL0[n].TLC; // Check for reserved cases Constraint c; (c, tc, te, tlc) = ReservedPMUThreshold(n, tc, te, tlc); if c == Constraint_DISABLED then return Vb; // Otherwise the values returned by ReservedPMUThreshold must be defined values // Check if disabled. Note that this function will return the value of Vb when // the control register fields are all zero, even without this check. if tc == '000' && TH == 0 && te == '0' && tlc == '00' then return Vb; // Threshold condition boolean Ct; case tc<2:1> of when '00' Ct = (Vb != TH); // Disabled or not-equal when '01' Ct = (Vb == TH); // Equals when '10' Ct = (Vb >= TH); // Greater-than-or-equal when '11' Ct = (Vb < TH); // Less-than integer Vn; if te == '1' then // Edge condition constant boolean Cp = PMULastThresholdValue[n]; boolean Ce; integer Ve; case tc<1:0> of when '10' Ce = (Cp != Ct); // Both edges when 'x1' Ce = (!Cp && Ct); // Single edge otherwise Unreachable(); // Covered by ReservedPMUThreshold case tlc of when '00' Ve = (if Ce then 1 else 0); when '10' Ve = (if Ce then Vm else 0); otherwise Unreachable(); // Covered by ReservedPMUThreshold Vn = Ve; else // Threshold condition integer Vt; case tc<0>:tlc of when '0 00' Vt = (if Ct then Vb else 0); when '0 01' Vt = (if Ct then Vb else Vm); when '0 10' Vt = (if Ct then Vm else 0); when '1 00' Vt = (if Ct then 1 else 0); when '1 01' Vt = (if Ct then 1 else Vm); otherwise Unreachable(); // Covered by ReservedPMUThreshold Vn = Vt; PMULastThresholdValue[n] = Ct; return Vn;
```

## J1.3.1.111 PMUCounterRange

```
// PMUCounterRange // =============== // Enumerates the ranges to which an event counter belongs to. enumeration PMUCounterRange { PMUCounterRange_R1, PMUCounterRange_R2,
```

```
PMUCounterRange_R3 };
```

## J1.3.1.112 PMUEvent

```
// PMUEvent() // ========== // Generate a PMU event. By default, increment by 1. PMUEvent(bits(16) pmuevent) PMUEvent(pmuevent, 1); // PMUEvent() // ========== // Accumulate a PMU Event. PMUEvent(bits(16) pmuevent, integer increment) constant integer counters = NUM_PMU_COUNTERS; if counters != 0 then for idx = 0 to counters - 1 PMUEvent(pmuevent, increment, idx); if (HaveAArch64() && IsFeatureImplemented(FEAT_PMUv3_ICNTR) && pmuevent == PMU_EVENT_INST_RETIRED) then IncrementInstructionCounter(increment); // PMUEvent() // ========== // Accumulate a PMU Event for a specific event counter. PMUEvent(bits(16) pmuevent, integer increment, integer idx) if !IsFeatureImplemented(FEAT_PMUv3) then return; if UsingAArch32() then if PMEVTYPER[idx].evtCount == pmuevent then PMUEventAccumulator[idx] = PMUEventAccumulator[idx] + increment; else if PMEVTYPER_EL0[idx].evtCount == pmuevent then PMUEventAccumulator[idx] = PMUEventAccumulator[idx] + increment;
```

## J1.3.1.113 PMUOverflowCondition

```
// PMUOverflowCondition() // ====================== // Enumerates the reasons for which the PMU overflow condition is evaluated. enumeration PMUOverflowCondition { PMUOverflowCondition_PMUException, PMUOverflowCondition_BRBEFreeze, PMUOverflowCondition_Freeze, PMUOverflowCondition_IRQ, PMUOverflowCondition_EDBGRQ };
```

## J1.3.1.114 PMUSwIncrement

```
// PMUSwIncrement() // ================ // Generate PMU Events on a write to PMSWINC PMUSwIncrement(bits(64) sw_incr_in)
```

```
bits(64) sw_incr = sw_incr_in; bits(31) mask = Zeros(31); constant integer counters = GetNumEventCountersAccessible(); if counters > 0 then mask<counters-1:0> = Ones(counters); if PSTATE.EL == EL0 && PMUSERENR_EL0.<UEN,SW> == '10') then mask = mask AND PMUACR_EL1<30:0>; sw_incr = sw_incr AND ZeroExtend(mask, 64); for idx = 0 to 30 if sw_incr<idx> == '1' then PMUEvent(PMU_EVENT_SW_INCR, 1, idx); return;
```

```
(IsFeatureImplemented(FEAT_PMUv3p9) && !ELUsingAArch32(EL1) && J1.3.1.115 ReservedPMUThreshold
```

```
// ReservedPMUThreshold() // ====================== // Checks if the given PMEVTYPER<n>_EL1.{TH,TE,TLC} values are reserved and will // generate Constrained Unpredictable behavior, otherwise return Constraint_NONE. (Constraint, bits(3), bit, bits(2)) ReservedPMUThreshold(integer n, bits(3) tc_in, bit te_in, bits(2) tlc_in) bits(3) tc = tc_in; bit te = te_in; bits(2) tlc = tlc_in; boolean reserved = FALSE; if IsFeatureImplemented(FEAT_PMUv3_EDGE) then if te == '1' && tc<1:0> == '00' then // Edge condition reserved = TRUE; else te = '0'; // Control is RES0 if IsFeatureImplemented(FEAT_PMUv3_TH2) && (n MOD 2) == 1 then if tlc == '11' then // Reserved value reserved = TRUE; if te == '1' then // Edge condition if tlc == '01' then reserved = TRUE; else // Threshold condition if tc<0> == '1' && tlc == '10' then reserved = TRUE; else tlc = '00'; // Controls are RES0 Constraint c = Constraint_NONE; if reserved then bits(6) unpred_reserved_bits; (c, unpred_reserved_bits) = ConstrainUnpredictableBits(Unpredictable_RESTC, 6); tc = unpred_reserved_bits<5:3>; te = unpred_reserved_bits<2>; tlc = unpred_reserved_bits<1:0>; return (c, tc, te, tlc);
```

## J1.3.1.116 SMEPMUEventPredicate

```
// SMEPMUEventPredicate() // ====================== // Call the relevant PMU predication events based on the SME instruction properties. SMEPMUEventPredicate(bits(N) mask1, bits(N) mask2, integer esize) PMUEvent(PMU_EVENT_SVE_PRED_SPEC); PMUEvent(PMU_EVENT_SME_PRED2_SPEC); if AllElementsActive(mask1, esize) && AllElementsActive(mask2, esize) then PMUEvent(PMU_EVENT_SME_PRED2_FULL_SPEC); else PMUEvent(PMU_EVENT_SME_PRED2_NOT_FULL_SPEC); if !AnyActiveElement(mask1, esize) && !AnyActiveElement(mask2, esize) then PMUEvent(PMU_EVENT_SME_PRED2_EMPTY_SPEC); else PMUEvent(PMU_EVENT_SME_PRED2_PARTIAL_SPEC);
```

## J1.3.1.117 SVEPMUEventPredicate

```
// SVEPMUEventPredicate() // ====================== // Call the relevant PMU predication events based on the SVE instruction properties. SVEPMUEventPredicate(bits(N) mask, integer esize) PMUEvent(PMU_EVENT_SVE_PRED_SPEC); if AllElementsActive(mask, esize) then PMUEvent(PMU_EVENT_SVE_PRED_FULL_SPEC); else PMUEvent(PMU_EVENT_SVE_PRED_NOT_FULL_SPEC); if !AnyActiveElement(mask, esize) then PMUEvent(PMU_EVENT_SVE_PRED_EMPTY_SPEC); else PMUEvent(PMU_EVENT_SVE_PRED_PARTIAL_SPEC);
```

## J1.3.1.118 ShouldPMUFreeze

```
// ShouldPMUFreeze() // ================= boolean ShouldPMUFreeze(PMUCounterRange r) constant boolean include_r1 = (r == PMUCounterRange_R1); constant boolean include_r2 = (r == PMUCounterRange_R2); constant boolean include_r3 = FALSE; if r == PMUCounterRange_R3 then return FALSE; constant boolean overflow = CheckPMUOverflowCondition(PMUOverflowCondition_Freeze, include_r1, include_r2, include_r3); return overflow;
```

## J1.3.1.119 ZeroCycleCounter

```
// ZeroCycleCounter() // ================== // Called on a write to PMCR_EL0 or PMCR that writes '1' to PMCR_EL0.C or PMCR.C. ZeroCycleCounter() bits(64) mask = Zeros(64); mask<CYCLE_COUNTER_ID> = '1'; ZeroPMUCounters(mask);
```

## J1.3.1.120 ZeroPMUCounters

```
// ZeroPMUCounters() // ================= // Zero set of counters specified by the mask in 'val'. // For a System register write to PMZR_EL0, 'val' is the value passed in X<t>. ZeroPMUCounters(bits(64) val) constant bits(64) masked_val = val AND GetPMUWriteMask(TRUE); for idx = 0 to 63 if masked_val<idx> == '1' && !IsRange3Counter(idx) then case idx of when INSTRUCTION_COUNTER_ID PMICNTR_EL0 = Zeros(64); when CYCLE_COUNTER_ID if !HaveAArch64() then PMCCNTR = Zeros(64); else PMCCNTR_EL0 = Zeros(64); otherwise if !HaveAArch64() then PMEVCNTR[idx] = Zeros(32); elsif IsFeatureImplemented(FEAT_PMUv3p5) then PMEVCNTR_EL0[idx] = Zeros(64); else PMEVCNTR_EL0[idx]<31:0> = Zeros(32); return; J1.3.1.121 CreatePCSample
```

```
// CreatePCSample() // ================ CreatePCSample() // In a simple sequential execution of the program, CreatePCSample is executed each time the PE // executes an instruction that can be sampled. An implementation is not constrained such that // reads of EDPCSRlo return the current values of PC, etc. if PCSRSuspended() then return; pc_sample.valid = ExternalNoninvasiveDebugAllowed() && !Halted(); pc_sample.pc = ThisInstrAddr(64); pc_sample.el = PSTATE.EL; pc_sample.rw = if UsingAArch32() then '0' else '1'; pc_sample.ss = CurrentSecurityState(); pc_sample.contextidr = if ELUsingAArch32(EL1) then CONTEXTIDR else CONTEXTIDR_EL1<31:0>; pc_sample.has_el2 = PSTATE.EL != EL3 && EL2Enabled(); if pc_sample.has_el2 then if ELUsingAArch32(EL2) then pc_sample.vmid = ZeroExtend(VTTBR.VMID, 16); elsif !IsFeatureImplemented(FEAT_VMID16) || VTCR_EL2.VS == '0' then pc_sample.vmid = ZeroExtend(VTTBR_EL2.VMID<7:0>, 16); else pc_sample.vmid = VTTBR_EL2.VMID; if ((IsFeatureImplemented(FEAT_VHE) || IsFeatureImplemented(FEAT_Debugv8p2)) && !ELUsingAArch32(EL2)) then pc_sample.contextidr_el2 = CONTEXTIDR_EL2<31:0>; else pc_sample.contextidr_el2 = bits(32) UNKNOWN; pc_sample.el0h = PSTATE.EL == EL0 && IsInHost(); return;
```

## J1.3.1.122 PCSRSuspended

```
// PCSRSuspended() // =============== // Returns TRUE if PC Sample-based Profiling is suspended, and FALSE boolean PCSRSuspended() if IsFeatureImplemented(FEAT_PMUv3_SS) && PMPCSCTL.SS == '1' then return FALSE; if IsFeatureImplemented(FEAT_PCSRv8p9) && PMPCSCTL.IMP == '1' then return PMPCSCTL.EN == '0'; return boolean IMPLEMENTATION_DEFINED "PCSR is suspended";
```

## J1.3.1.123 PCSample

```
contextidr_el2,
```

```
PCSample pc_sample; // PCSample // ======== type PCSample is ( boolean valid, bits(64) pc, bits(2) el, bit rw, SecurityState ss, boolean has_el2, bits(32) contextidr, bits(32) boolean el0h, bits(16) vmid )
```

## J1.3.1.124 Read\_EDPCSRlo

```
// Read_EDPCSRlo() // =============== bits(32) Read_EDPCSRlo(boolean memory_mapped) // The Software lock is OPTIONAL. update = !memory_mapped || EDLSR.SLK == '0'; // Software locked: no side-effects bits(32) sample; if pc_sample.valid then sample = pc_sample.pc<31:0>; if update then if IsFeatureImplemented(FEAT_VHE) && EDSCR.SC2 == '1' then EDPCSRhi.PC = (if pc_sample.rw == '0' then Zeros(24) else pc_sample.pc<55:32>); EDPCSRhi.EL = pc_sample.el; EDPCSRhi.NS = (if pc_sample.ss == SS_Secure then '0' else '1'); else EDPCSRhi = (if pc_sample.rw == '0' then Zeros(32) else pc_sample.pc<63:32>); EDCIDSR = pc_sample.contextidr; if ((IsFeatureImplemented(FEAT_VHE) || IsFeatureImplemented(FEAT_Debugv8p2)) && EDSCR.SC2 == '1') then EDVIDSR = (if pc_sample.has_el2 then pc_sample.contextidr_el2 else bits(32) UNKNOWN); else EDVIDSR.VMID = (if pc_sample.has_el2 && pc_sample.el IN {EL1,EL0} then pc_sample.vmid else Zeros(16)); EDVIDSR.NS = (if pc_sample.ss == SS_Secure then '0' else '1'); EDVIDSR.E2 = (if pc_sample.el == EL2 then '1' else '0'); EDVIDSR.E3 = (if pc_sample.el == EL3 then '1' else '0') AND pc_sample.rw; // The conditions for setting HV are not specified if PCSRhi is zero.
```

```
otherwise.
```

```
// An example implementation may be "pc_sample.rw". EDVIDSR.HV = (if !IsZero(EDPCSRhi) then '1' else bit IMPLEMENTATION_DEFINED "0 or 1"); else sample = Ones(32); if update then EDPCSRhi = bits(32) UNKNOWN; EDCIDSR = bits(32) UNKNOWN; EDVIDSR = bits(32) UNKNOWN; return sample; J1.3.1.125 Read_PMPCSR // Read_PMPCSR() // ============= bits(64) Read_PMPCSR(boolean memory_mapped) // The Software lock is OPTIONAL. update = !memory_mapped || PMLSR.SLK == '0'; // Software locked: no side-effects if IsFeatureImplemented(FEAT_PCSRv8p9) && update then if IsFeatureImplemented(FEAT_PMUv3_SS) && PMPCSCTL.SS == '1' then update = FALSE; elsif PMPCSCTL.<IMP,EN> == '10' || (PMPCSCTL.IMP == '0' && PCSRSuspended()) then pc_sample.valid = FALSE; SetPCSRActive(); if pc_sample.valid then if update then SetPCSample(); return PMPCSR; else if update then SetPCSRUnknown(); return (bits(32) UNKNOWN : Ones(32)); J1.3.1.126 SetPCSRActive // SetPCSRActive() // =============== // Sets PC Sample-based Profiling to active state. SetPCSRActive() if PMPCSCTL.IMP == '1' then PMPCSCTL.EN = '1'; // If PMPCSCTL.IMP reads as `0b0`, then PMPCSCTL.EN is RES0, and it is // IMPLEMENTATION DEFINED whether PSCR is suspended or active at reset. J1.3.1.127 SetPCSRUnknown
```

```
// SetPCSRUnknown() // ================ // Sets the PC sample registers to UNKNOWN values because PC sampling // is prohibited. SetPCSRUnknown() PMPCSR<31:0> = Ones(32); PMPCSR<55:32> = bits(24) UNKNOWN; PMPCSR.EL = bits(2) UNKNOWN; PMPCSR.NS = bit UNKNOWN; if IsFeatureImplemented(FEAT_PMUv3_EXT64) then
```

```
PMCCIDSR = bits(64) UNKNOWN; PMVCIDSR.VMID = bits(16) UNKNOWN; if IsFeatureImplemented(FEAT_PMUv3_EXT32) PMCID1SR = bits(32) UNKNOWN; PMCID2SR = bits(32) UNKNOWN; PMVIDSR.VMID = bits(16) UNKNOWN;
```

```
then return;
```

## J1.3.1.128 SetPCSample

```
// SetPCSample() // ============= // Sets the PC sample registers to the appropriate sample values. SetPCSample() PMPCSR<31:0> = pc_sample.pc<31:0>; PMPCSR<55:32> = (if pc_sample.rw == '0' then Zeros(24) else pc_sample.pc<55:32>); PMPCSR.EL = pc_sample.el; if IsFeatureImplemented(FEAT_RME) then case pc_sample.ss of when SS_Secure PMPCSR.NSE = '0'; PMPCSR.NS = '0'; when SS_NonSecure PMPCSR.NSE = '0'; PMPCSR.NS = '1'; when SS_Root PMPCSR.NSE = '1'; PMPCSR.NS = '0'; when SS_Realm PMPCSR.NSE = '1'; PMPCSR.NS = '1'; else PMPCSR.NS = (if pc_sample.ss == SS_Secure then '0' else '1'); constant bits(32) contextidr_el2 = (if pc_sample.has_el2 then pc_sample.contextidr_el2 else bits(32) UNKNOWN); bits(16) vmid = bits(16) UNKNOWN; if pc_sample.has_el2 && pc_sample.el IN {EL1,EL0} && !pc_sample.el0h then vmid = pc_sample.vmid; if IsFeatureImplemented(FEAT_PMUv3_EXT64) then PMCCIDSR = contextidr_el2:pc_sample.contextidr; PMVCIDSR.VMID = vmid; if IsFeatureImplemented(FEAT_PMUv3_EXT32) then PMCID1SR = pc_sample.contextidr; PMCID2SR = contextidr_el2; PMVIDSR.VMID = vmid; return;
```

## J1.3.1.129 CheckSoftwareStep

```
// CheckSoftwareStep() // =================== // Take a Software Step exception if in the active-pending state CheckSoftwareStep() // Other self-hosted debug functions will call AArch32.GenerateDebugExceptions() if called from // AArch32 state. However, because Software Step is only active when the debug target Exception // level is using AArch64, CheckSoftwareStep only calls AArch64.GenerateDebugExceptions(). step_enabled = (!ELUsingAArch32(DebugTarget()) && AArch64.GenerateDebugExceptions() && MDSCR_EL1.SS == '1'); active_pending = step_enabled && PSTATE.SS == '0'; // active-pending if active_pending then AArch64.SoftwareStepException(); ShouldAdvanceSS = TRUE;
```

return;

## J1.3.1.130 DebugExceptionReturnSS

```
// DebugExceptionReturnSS() // ======================== // Returns value to write to PSTATE.SS on an exception return or Debug state exit. bit DebugExceptionReturnSS(bits(N) spsr) assert Halted() || Restarting() || PSTATE.EL != EL0; boolean enabled_at_source; if Restarting() then enabled_at_source = FALSE; elsif UsingAArch32() then enabled_at_source = AArch32.GenerateDebugExceptions(); else enabled_at_source = AArch64.GenerateDebugExceptions(); boolean valid; bits(2) dest_el; if IllegalExceptionReturn(spsr) then dest_el = PSTATE.EL; else (valid, dest_el) = ELFromSPSR(spsr); assert valid; dest_ss = SecurityStateAtEL(dest_el); boolean enabled_at_dest; dest_using_32 = (if dest_el == EL0 then spsr<4> == '1' else ELUsingAArch32(dest_el)); if dest_using_32 then enabled_at_dest = AArch32.GenerateDebugExceptionsFrom(dest_el, dest_ss); else constant bit mask = spsr<9>; enabled_at_dest = AArch64.GenerateDebugExceptionsFrom(dest_el, dest_ss, mask); ELd = DebugTargetFrom(dest_ss); bit SS_bit; if !ELUsingAArch32(ELd) && MDSCR_EL1.SS == '1' && !enabled_at_source && enabled_at_dest then SS_bit = spsr<21>; else SS_bit = '0'; return SS_bit;
```

```
J1.3.1.131 SSAdvance
```

```
// SSAdvance() // =========== // Advance the Software Step state machine. SSAdvance() // A simpler implementation of this function just clears PSTATE.SS to zero regardless of the // current Software Step state machine. However, this check is made to illustrate that the // PE only needs to consider advancing the state machine from the active-not-pending // state. if !ShouldAdvanceSS then return; target = DebugTarget(); step_enabled = !ELUsingAArch32(target) && MDSCR_EL1.SS == '1'; active_not_pending = step_enabled && PSTATE.SS == '1'; if active_not_pending then PSTATE.SS = '0'; ShouldAdvanceSS = FALSE; return;
```

## J1.3.1.132 SoftwareStepOpEnabled

```
// SoftwareStepOpEnabled() // ======================= // Returns a boolean indicating if execution from MDSTEPOP_EL1 is enabled. boolean SoftwareStepOpEnabled() if !IsFeatureImplemented(FEAT_STEP2) || UsingAArch32() then return FALSE; step_enabled = AArch64.GenerateDebugExceptions() && MDSCR_EL1.SS == '1'; active_not_pending = step_enabled && PSTATE.SS == '1'; stepop = (MDSCR_EL1.EnSTEPOP == '1' && (!HaveEL(EL3) || MDCR_EL3.EnSTEPOP == '1') && (!EL2Enabled() || MDCR_EL2.EnSTEPOP == '1')); return active_not_pending && stepop;
```

## J1.3.1.133 SoftwareStep\_DidNotStep // SoftwareStep\_DidNotStep() // ========================= // Returns TRUE if the previously executed instruction was executed in the // inactive state, that is, if it was not itself stepped. // Might return TRUE or FALSE if the previously executed instruction was an ISB // or ERET executed in the active-not-pending state, or if another exception // was taken before the Software Step exception. Returns FALSE otherwise, // indicating that the previously executed instruction was executed in the // active-not-pending state, that is, the instruction was stepped. boolean SoftwareStep\_DidNotStep(); J1.3.1.134 SoftwareStep\_SteppedEX // SoftwareStep\_SteppedEX() // ======================== // Returns a value that describes the previously executed instruction. The // result is valid only if SoftwareStep\_DidNotStep() returns FALSE. // Might return TRUE or FALSE if the instruction was an AArch32 LDREX or LDAEX // that failed its condition code test. Otherwise returns TRUE if the // instruction was a Load-Exclusive class instruction, and FALSE if the // instruction was not a Load-Exclusive class instruction. boolean SoftwareStep\_SteppedEX(); J1.3.1.135 DataCacheWatchpointSize

```
// DataCacheWatchpointSize() // ========================= // Return the IMPLEMENTATION DEFINED data cache watchpoint size integer DataCacheWatchpointSize() constant integer size = integer IMPLEMENTATION_DEFINED "Data Cache Invalidate Watchpoint Size"; assert IsPow2(size) && size >= 2^(UInt(CTR_EL0.DminLine) + 2) && size <= 2048; return size;
```

## J1.3.1.136 WatchpointInfo

```
// WatchpointInfo // ============== // Watchpoint related fields. type WatchpointInfo is ( WatchpointType wptype, // Type of watchpoint matched boolean maybe_false_match, // Watchpoint matches rounded range integer watchpt_num, // Matching watchpoint number boolean value_match, // Watchpoint match bits(64) vaddress // Matching Virtual Address )
```

## J1.3.1.137 WatchpointType

```
// WatchpointType // ============== enumeration WatchpointType { WatchpointType_Inactive, // Watchpoint inactive or disabled WatchpointType_AddrMatch, // Address Match watchpoint WatchpointType_AddrMismatch // Address Mismatch watchpoint };
```

## J1.3.2 shared/exceptions

This section includes the following pseudocode functions:

- EffectiveHCRX\_EL2\_TMEA
- EffectiveHCR\_AMO
- EffectiveHCR\_TEA
- EffectiveNMEA
- EffectiveSCR\_EL3\_TMEA
- PhysicalSErrorTarget
- SyncExternalAbortTarget
- ConditionSyndrome
- Exception
- ExceptionRecord
- ExceptionSyndrome
- Undefined

## J1.3.2.1 EffectiveHCRX\_EL2\_TMEA

```
EL2Enabled() &&
```

```
// EffectiveHCRX_EL2_TMEA() // ======================== // Return the Effective value of HCRX_EL2.TMEA. bit EffectiveHCRX_EL2_TMEA() if (IsFeatureImplemented(FEAT_DoubleFault2) && !ELUsingAArch32(EL2) && IsHCRXEL2Enabled()) then return HCRX_EL2.TMEA; else return '0';
```

## J1.3.2.2 EffectiveHCR\_AMO

```
// EffectiveHCR_AMO() // ================== // Return the Effective value of HCR_EL2.AMO. bit EffectiveHCR_AMO() if EffectiveTGE() == '1' then return (if ELUsingAArch32(EL2) || EffectiveHCR_EL2_E2H() == '0' then '1' else '0'); elsif EL2Enabled() then return (if ELUsingAArch32(EL2) then HCR.AMO else HCR_EL2.AMO); else return '0';
```

```
J1.3.2.3 EffectiveHCR_TEA // EffectiveHCR_TEA() // ================== // Return the Effective value of HCR_EL2.TEA. bit EffectiveHCR_TEA() if EL2Enabled() && IsFeatureImplemented(FEAT_RAS) then return (if ELUsingAArch32(EL2) then HCR2.TEA else HCR_EL2.TEA); else return '0'; J1.3.2.4 EffectiveNMEA
```

```
// EffectiveNMEA() // =============== // Return the Effective value of SCR_EL3.NMEA or SCTLR2_ELx.NMEA. bit EffectiveNMEA() if IsFeatureImplemented(FEAT_DoubleFault2) then if PSTATE.EL == EL3 && !UsingAArch32() then return SCR_EL3.NMEA; elsif (PSTATE.EL == EL2 || IsInHost()) && !ELUsingAArch32(EL2) then return (if IsSCTLR2EL2Enabled() then SCTLR2_EL2.NMEA else '0'); elsif !ELUsingAArch32(EL1) then return (if IsSCTLR2EL1Enabled() then SCTLR2_EL1.NMEA else '0'); else return '0'; elsif IsFeatureImplemented(FEAT_DoubleFault) && PSTATE.EL == EL3 && !UsingAArch32() then return SCR_EL3.NMEA AND EffectiveEA(); else return '0';
```

## J1.3.2.5 EffectiveSCR\_EL3\_TMEA

```
// EffectiveSCR_EL3_TMEA() // ======================= // Return the Effective value of SCR_EL3.TMEA. bit EffectiveSCR_EL3_TMEA() if (IsFeatureImplemented(FEAT_DoubleFault2) && HaveEL(EL3) && !ELUsingAArch32(EL3)) then return SCR_EL3.TMEA; else return '0';
```

## J1.3.2.6 PhysicalSErrorTarget

```
// PhysicalSErrorTarget() // ====================== // Returns a tuple of whether SError exception can be taken and, if so, the // target Exception level. // If EL3 is implemented and using AArch32, then a target Exception level of // EL1 means Abort mode, and EL3 means Monitor mode, including in Secure // state when Abort mode is part of EL3. (boolean, bits(2)) PhysicalSErrorTarget() if Halted() then return (TRUE, bits(2) UNKNOWN); constant bit effective_ea = EffectiveEA(); constant bit effective_amo = EffectiveHCR_AMO(); constant bit effective_tge = EffectiveTGE(); constant bit effective_nmea = EffectiveNMEA(); // When EL3 is implemented and using AArch32, the SCR.AW bit can allow PSTATE.A // to mask SError exceptions in Non-secure state when SCR.EA is 1 and the Effective // value of HCR.AMO is 0. bit effective_aw; if (ELUsingAArch32(EL3) && effective_ea == '1' && CurrentSecurityState() == SS_NonSecure && effective_amo == '0') then effective_aw = SCR.AW; else effective_aw = '0'; // The exception is masked by software. boolean masked; case PSTATE.EL of when EL3 masked = (!UsingAArch32() && effective_ea == '0') || PSTATE.A == '1'; when EL2 masked = ((effective_ea == '0' || effective_aw == '1') && ((!UsingAArch32() && effective_tge == '0' && effective_amo == '0') || PSTATE.A == '1')); when EL1, EL0 masked = ((effective_ea == '0' || effective_aw == '1') && effective_amo == '0' && PSTATE.A == '1'); // When FEAT_DoubleFault or FEAT_DoubleFault2 is implemented, the mask might be overridden. masked = (masked && effective_nmea == '0'); // External debug might disable the exception in the current Security state. // This is not relevant at EL3. constant boolean intdis = PSTATE.EL != EL3 && ExternalDebugInterruptsDisabled(EL1); bits(2) target_el = bits(2) UNKNOWN; if effective_ea == '1' || (PSTATE.EL == EL3 && !ELUsingAArch32(EL3)) then if !masked then target_el = EL3; elsif EL2Enabled() && effective_amo == '1' && !intdis && PSTATE.EL IN {EL0, EL1} then target_el = EL2; masked = FALSE; elsif (EffectiveHCRX_EL2_TMEA() == '1' && !intdis && ((PSTATE.EL == EL1 && PSTATE.A == '1') || (PSTATE.EL == EL0 && masked && !IsInHost()))) then target_el = EL2; masked = FALSE; elsif (EffectiveSCR_EL3_TMEA() == '1' && ((PSTATE.EL IN {EL2, EL1} && PSTATE.A == '1') || (PSTATE.EL IN {EL2, EL0} && masked) || intdis)) then
```

```
target_el = EL3; masked = FALSE; elsif PSTATE.EL == EL2 || IsInHost() then if !masked then target_el = EL2; else assert (PSTATE.EL == EL1 || (PSTATE.EL == EL3 && ELUsingAArch32(EL3)) || (PSTATE.EL == EL0 && !IsInHost())); if !masked then target_el = EL1; // External debug might disable the exception for the target Exception if !masked && ExternalDebugInterruptsDisabled(target_el) then masked = TRUE; target_el = bits(2) UNKNOWN; return (masked, target_el);
```

## J1.3.2.7 SyncExternalAbortTarget

```
// SyncExternalAbortTarget() // ========================= // Returns the target Exception level for a Synchronous External Data or // Instruction or Prefetch Abort. // If EL3 is implemented and using AArch32, then a target Exception level of // EL1 means Abort mode, and EL3 means Monitor mode, including in Secure // state when Abort mode is part of EL3. bits(2) SyncExternalAbortTarget(FaultRecord fault) constant bit effective_ea = EffectiveEA(); constant bit effective_tea = EffectiveHCR_TEA(); constant bit effective_tge = EffectiveTGE(); bits(2) target_el; if effective_ea == '1' || (PSTATE.EL == EL3 && !ELUsingAArch32(EL3)) then target_el = EL3; elsif (EL2Enabled() && PSTATE.EL IN {EL1, EL0} && (effective_tea == '1' || IsSecondStage(fault) || fault.accessdesc.acctype == AccessType_NV2 || (PSTATE.EL == EL0 && effective_tge == '1'))) then target_el = EL2; elsif EffectiveHCRX_EL2_TMEA() == '1' && PSTATE.A == '1' && PSTATE.EL == EL1 then target_el = EL2; elsif EffectiveSCR_EL3_TMEA() == '1' && PSTATE.A == '1' && PSTATE.EL IN {EL1, EL2} then target_el = EL3; else assert PSTATE.EL != EL3 || ELUsingAArch32(EL3); target_el = (if PSTATE.EL == EL2 then EL2 else EL1); return target_el;
```

## J1.3.2.8

```
// ConditionSyndrome() // =================== // Return CV and COND fields of instruction bits(5) ConditionSyndrome()
```

```
ConditionSyndrome syndrome
```

```
level.
```

```
bits(5) syndrome; if UsingAArch32() then cond = CurrentCond(); if PSTATE.T == '0' then // A32 syndrome<4> = '1'; // A conditional A32 instruction that is known to pass its condition code check // can be presented either with COND set to 0xE, the value for unconditional, or // the COND value held in the instruction. if ConditionHolds(cond) && ConstrainUnpredictableBool(Unpredictable_ESRCONDPASS) then syndrome<3:0> = '1110'; else syndrome<3:0> = cond; else // T32 // When a T32 instruction is trapped, it is IMPLEMENTATION DEFINED whether: // * CV set to 0 and COND is set to an UNKNOWN value // * CV set to 1 and COND is set to the condition code for the condition that // applied to the instruction. if boolean IMPLEMENTATION_DEFINED "Condition valid for trapped T32" then syndrome<4> = '1'; syndrome<3:0> = cond; else syndrome<4> = '0'; syndrome<3:0> = bits(4) UNKNOWN; else syndrome<4> = '1'; syndrome<3:0> = '1110'; return syndrome;
```

## J1.3.2.9

```
Exception
```

```
// Exception // ========= // Classes of exception. enumeration Exception { Exception_Uncategorized, // Uncategorized or unknown reason Exception_WFxTrap, // Trapped WFI or WFE instruction Exception_CP15RTTrap, // Trapped AArch32 MCR or MRC access, coproc=0b111 Exception_CP15RRTTrap, // Trapped AArch32 MCRR or MRRC access, coproc=0b1111 Exception_CP14RTTrap, // Trapped AArch32 MCR or MRC access, coproc=0b1110 Exception_CP14DTTrap, // Trapped AArch32 LDC or STC access, coproc=0b1110 Exception_CP14RRTTrap, // Trapped AArch32 MRRC access, coproc=0b1110 Exception_AdvSIMDFPAccessTrap, // HCPTR-trapped access to SIMD or FP Exception_FPIDTrap, // Trapped access to SIMD or FP ID register Exception_LDST64BTrap, // Trapped access to ST64BV, ST64BV0, ST64B and LD64B // Trapped BXJ instruction not supported in Armv8 Exception_PACTrap, // Trapped invalid PAC use Exception_IllegalState, // Illegal Execution state Exception_SupervisorCall, // Supervisor Call Exception_HypervisorCall, // Hypervisor Call Exception_MonitorCall, // Monitor Call or Trapped SMC instruction Exception_SystemRegisterTrap, // Trapped MRS or MSR System register access Exception_ERetTrap, // Trapped invalid ERET use Exception_InstructionAbort, // Instruction Abort or Prefetch Abort Exception_PCAlignment, // PC alignment fault Exception_DataAbort, // Data Abort Exception_NV2DataAbort, // Data abort at EL1 reported as being from EL2 Exception_PACFail, // PAC Authentication failure Exception_SPAlignment, // SP alignment fault Exception_FPTrappedException, // IEEE trapped FP exception Exception_SError, // SError interrupt Exception_Breakpoint, // (Hardware) Breakpoint Exception_SoftwareStep, // Software Step
```

```
Exception_Watchpoint, // Watchpoint Exception_NV2Watchpoint, // Watchpoint at EL1 reported as being from EL2 Exception_SoftwareBreakpoint, // Software Breakpoint Instruction Exception_VectorCatch, // AArch32 Vector Catch Exception_IRQ, // IRQ interrupt Exception_SVEAccessTrap, // HCPTR trapped access to SVE Exception_SMEAccessTrap, // HCPTR trapped access to SME Exception_GPC, // Granule protection check Exception_BranchTarget, // Branch Target Identification Exception_MemCpyMemSet, // Exception from a CPY* or SET* instruction Exception_GCSFail, // GCS Exceptions Exception_Profiling, // Profiling exception Exception_SystemRegister128Trap, // Trapped MRRS or MSRR System register or SYSP access Exception_FIQ}; // FIQ interrupt
```

## J1.3.2.10 ExceptionRecord

```
// ExceptionRecord // =============== type ExceptionRecord is ( Exception exceptype, // Exception class IssType syndrome, // Syndrome record FullAddress paddress, // Physical fault address bits(64) vaddress, // Virtual fault address boolean ipavalid, // Validity of Intermediate Physical fault address boolean pavalid, // Validity of Physical fault address bit NS, // Intermediate Physical fault address space bits(56) ipaddress, // Intermediate Physical fault address boolean trappedsyscallinst) // Trapped SVC or SMC instruction
```

## J1.3.2.11 ExceptionSyndrome

```
// ExceptionSyndrome() // =================== // Return a blank exception syndrome record for an exception of the given ExceptionRecord ExceptionSyndrome(Exception exceptype) ExceptionRecord r; r.exceptype = exceptype; // Initialize all other fields r.syndrome.iss = Zeros(25); r.syndrome.iss2 = Zeros(24); r.vaddress = Zeros(64); r.ipavalid = FALSE; r.pavalid = FALSE; r.NS = '0'; r.ipaddress = Zeros(56); r.paddress.paspace = PASpace UNKNOWN; r.paddress.address = bits(56) UNKNOWN; r.trappedsyscallinst = FALSE; return r;
```

## J1.3.2.12 Undefined

```
// Undefined() // ===========
```

```
type.
```

```
Undefined() if UsingAArch32() then AArch32.Undefined(); else AArch64.Undefined();
```

## J1.3.3 shared/functions

This section includes the following pseudocode functions:

- EncodeLDFSC
- IPAValid
- IsAsyncAbort
- IsDebugException
- IsExternalAbort
- IsExternalAbortOnWalk
- IsExternalSyncAbort
- IsFault
- IsSErrorInterrupt
- IsSecondStage
- LSInstructionSyndrome
- ReportAsGPCException
- CACHE\_OP
- CPASAtPAS
- CPASAtSecurityState
- CacheRecord
- DecodeSW
- GetCacheInfo
- ASR
- ASR\_C
- Abs
- Align
- BitCount
- CeilLog2
- CeilPow2
- CountLeadingSignBits
- CountLeadingZeroBits
- Elem
- Extend
- FloorPow2
- HighestSetBit
- HighestSetBitNZ
- IsAligned
- IsAlignedP2
- IsEven
- IsOdd
- IsOnes
- IsPow2

- IsZero
- IsZeroBit
- LSL
- LSL\_C
- LSR
- LSR\_C
- LowestSetBit
- LowestSetBitNZ
- Max
- Min
- NormalizeReal
- Ones
- ROL
- ROR
- ROR\_C
- RShr
- Replicate
- Reverse
- RoundDown
- RoundTowardsZero
- RoundUp
- SInt
- SignExtend
- Signal
- UInt
- ZeroExtend
- Zeros
- AArch32.CheckTimerConditions
- AArch64.CheckTimerConditions
- CNTHCTL\_EL2\_VHE
- GenericCounterTick
- IsLocalTimeoutEventPending
- IsTimerConditionMet
- LocalTimeoutVal
- PhysicalCount
- SetEventRegister
- TestEventCNTP
- TestEventCNTV
- VirtualCounterTimer
- BitReverse
- Poly32Mod2
- AESInvMixColumns
- AESInvShiftRows
- AESInvSubBytes
- AESMixColumns
- AESShiftRows
- AESSubBytes

- FFmul02
- FFmul03
- FFmul09
- FFmul0B
- FFmul0D
- FFmul0E
- SHA256hash
- SHAchoose
- SHAhashSIGMA0
- SHAhashSIGMA1
- SHAmajority
- SHAparity
- Sbox
- DecodeType
- EndOfDecode
- ClearExclusiveByAddress
- ClearExclusiveLocal
- ExclusiveMonitorsStatus
- IsExclusiveGlobal
- IsExclusiveLocal
- MarkExclusiveGlobal
- MarkExclusiveLocal
- ProcessorID
- HaveSoftwareLock
- HaveTraceExt
- InsertIESBBeforeException
- ActionRequired
- ClearPendingDelegatedSError
- ClearPendingPhysicalSError
- ClearPendingVirtualSError
- ErrorIsContained
- ErrorIsSynchronized
- ExtAbortToAArch64
- ExternalAbort
- ExternalFault
- FaultIsCorrected
- GetPendingPhysicalSError
- HandleExternalAbort
- HandleExternalReadAbort
- HandleExternalTTWAbort
- HandleExternalWriteAbort
- IsDelegatedSErrorPending
- IsExternalAbortTakenSynchronously
- IsPhysicalSErrorPending
- IsSErrorEdgeTriggered
- IsSynchronizablePhysicalSErrorPending
- IsVirtualSErrorPending

- PEErrorState
- PendSErrorInterrupt
- ReportErrorAsIMPDEF
- ReportErrorAsUC
- ReportErrorAsUER
- ReportErrorAsUEU
- ReportErrorAsUncategorized
- StateIsRecoverable
- BFAdd
- BFAdd\_ZA
- BFDotAdd
- BFInfinity
- BFMatMulAddH
- BFMax
- BFMaxNum
- BFMin
- BFMinNum
- BFMul
- BFMulAdd
- BFMulAddH
- BFMulAddH\_ZA
- BFMulAdd\_ZA
- BFMulH
- BFNeg
- BFRound
- BFScale
- BFSub
- BFSub\_ZA
- BFUnpack
- BFZero
- FPAdd\_BF16
- FPConvertBF
- FPRoundBF
- FixedToFP

•

BFConvertFP8

- FP8Bits
- FP8ConvertBF
- FP8ConvertFP
- FP8DecodeType
- FP8DefaultNaN
- FP8DotAddFP
- FP8Infinity
- FP8MatMulAddFP
- FP8MaxNormal
- FP8MulAddFP
- FP8Round
- FP8Type

- FP8Unpack
- FP8Zero
- FPConvertFP8
- FPAbs
- FPAbsMax
- FPAbsMin

•

FPAdd

- FPAdd\_ZA
- FPBits
- FPBitsType
- FPFracBits
- FPCompare
- FPCompareEQ
- FPCompareGE
- FPCompareGT
- FPConvert
- FPConvertNaN
- FPDecodeRM
- FPDecodeRounding
- FPDefaultNaN
- FPDiv
- FPDot
- FPDotAdd
- FPDotAdd\_ZA
- FPExc
- FPInfinity
- FPMatMulAdd
- FPMatMulAddH
- FPMax
- FPMaxNormal
- FPMaxNum
- IsMerging
- FPMin
- FPMinNum
- FPMul
- FPMulAdd
- FPMulAdd\_ZA
- FPMulAddH
- FPMulAddH\_ZA
- FPProcessNaNs3H
- FPMulX
- FPNeg
- FPOnePointFive
- FPProcessDenorm
- FPProcessDenorms
- FPProcessDenorms3
- FPProcessDenorms4

- FPProcessException
- FPProcessNaN
- FPProcessNaNs
- FPProcessNaNs3
- FPProcessNaNs4
- FPRecipEstimate
- RecipEstimate
- FPRecpX
- FPRound
- FPRoundBase
- FPRoundCV
- FPRound\_FP8
- FPRounding
- FPRoundingMode
- FPRoundInt
- FPRoundIntN
- FPRSqrtEstimate
- RecipSqrtEstimate
- FPSqrt
- FPSub
- FPSub\_ZA
- FPThree
- FPToFixed
- FPToFixedJS
- FPTwo
- FPType
- FPUnpack
- FPUnpackBase
- FPUnpackCV
- FPZero
- VFPExpandImm
- AddWithCarry
- InterruptID
- SetInterruptRequestLevel
- AArch64.BranchAddr
- AccessDescriptor
- AccessType
- AddrTop
- AddressSize
- AlignmentEnforced
- Allocation
- BigEndian
- BigEndianReverse
- CacheOp
- CacheOpScope
- CachePASpace
- CacheType

- Cacheability
- CreateAccDescA32LSMD
- CreateAccDescASIMD
- CreateAccDescASIMDAcqRel
- CreateAccDescAT
- CreateAccDescAcqRel
- CreateAccDescAtomicOp
- CreateAccDescDC
- CreateAccDescDCZero
- CreateAccDescExLDST
- CreateAccDescFPAtomicOp
- CreateAccDescGCS
- CreateAccDescGCSSS1
- CreateAccDescGPR
- CreateAccDescGPTW
- CreateAccDescHACDBS
- CreateAccDescHDBSS
- CreateAccDescIC
- CreateAccDescIFetch
- CreateAccDescLDAcqPC
- CreateAccDescLDGSTG
- CreateAccDescLOR
- CreateAccDescLS64
- CreateAccDescMOPS
- CreateAccDescNV2
- CreateAccDescRCW
- CreateAccDescS1TTW
- CreateAccDescS2TTW
- CreateAccDescSME
- CreateAccDescSPE
- CreateAccDescSTGMOPS
- CreateAccDescSVE
- CreateAccDescSVEFF
- CreateAccDescSVENF
- CreateAccDescTRBE
- CreateAccDescTTEUpdate
- DataMemoryBarrier
- DataSynchronizationBarrier
- DeviceType
- EffectiveMTX
- EffectiveTBI
- EffectiveTCMA
- ErrorState
- Fault
- FaultRecord
- FullAddress
- GPCF

- GPCFRecord
- Hint\_Prefetch
- Hint\_RangePrefetch
- IsContiguousSVEAccess
- IsRelaxedWatchpointAccess
- IsSIMDFPAccess
- IsSMEAccess
- IsWatchpointableAccess
- MBReqDomain
- MBReqTypes
- MemAtomicOp
- MemAttrHints
- MemOp
- MemType
- Memory
- MemoryAttributes
- NewAccDesc
- PASpace
- Permissions
- PhysMemRead
- PhysMemRetStatus
- PhysMemWrite
- PrefetchHint
- S1AccessControls
- S2AccessControls
- Shareability
- SpeculativeStoreBypassBarrierToPA
- SpeculativeStoreBypassBarrierToVA
- Tag
- VARange
- AltPARTIDSpace
- AltPIDRealm
- AltPIDSecure
- DefaultMPAMInfo
- GenMPAM
- GenMPAMAtEL
- GenMPAMCurEL
- GenNewMPAMData
- GenPARTID
- GenPMG
- GetMPAM\_PARTID
- GetMPAM\_PMG
- MAP\_vPARTID
- MPAM
- MPAMIsEnabled
- MPAMIsVirtual
- PARTIDSpaceFromSS

- UsePrimarySpaceEL10
- UsePrimarySpaceEL2
- mapvpmw
- ASID

•

ExecutionCntxt

- RESTRICT\_PREDICTIONS
- RestrictType
- TargetSecurityState
- BranchTo
- BranchToAddr
- BranchType
- ESize
- EffectiveFPCR
- FPCR\_Type
- FPMR\_Type
- Hint\_Branch
- NextInstrAddr
- ResetExternalDebugRegisters
- ThisInstrAddr
- UnimplementedIDRegister
- V
- Vpart
- \_PC
- \_R
- SPSR\_ELx
- SPSR\_curr
- AArch64.ChkFeat
- AddressAdd
- AddressInNaturallyAlignedBlock
- AddressIncrement
- BranchTargetCheck
- ClearEventRegister
- ConditionHolds
- ConsumptionOfSpeculativeDataBarrier
- CurrentInstrSet
- CurrentSecurityState
- DSBAlias
- EL0
- EL2Enabled
- EL3SDDUndef
- EL3SDDUndefPriority
- ELFromM32
- ELFromSPSR
- ELIsInHost
- ELStateUsingAArch32
- ELStateUsingAArch32K
- ELUsingAArch32

- ELUsingAArch32K
- EffectiveEA
- EffectiveHCR\_EL2\_E2H
- EffectiveHCR\_EL2\_NVx
- EffectiveSCR\_EL3\_NS
- EffectiveSCR\_EL3\_NSE
- EffectiveSCR\_EL3\_RW
- EffectiveTGE
- EndOfInstruction
- EnterLowPowerState
- EventRegister
- ExceptionalOccurrenceTargetState
- ExecuteAsNOP
- FIQPending
- GetAccumulatedFPExceptions

•

GetLoadStoreType

- GetPSRFromPSTATE
- HaveAArch32
- HaveAArch32EL
- HaveAArch64
- HaveEL
- HaveELUsingSecurityState
- HaveSecureState

•

HighestEL

- Hint\_CLRBHB
- Hint\_DGH
- Hint\_StoreShared
- Hint\_WFE
- Hint\_WFET
- Hint\_WFI
- Hint\_WFIT
- Hint\_Yield
- IRQPending
- IllegalExceptionReturn
- InstrSet
- InstructionFetchBarrier
- InstructionSynchronizationBarrier
- IsASEInstruction
- IsCurrentSecurityState
- IsEventRegisterSet
- IsHighestEL
- IsInHost
- IsSecureBelowEL3
- IsSecureEL2Enabled
- LocalTimeoutEvent
- Mode
- NonSecureOnlyImplementation

- PLOfEL
- PSTATE
- PhysicalCountInt
- PrivilegeLevel
- ProcState
- RestoredITBits
- SecureOnlyImplementation
- SecurityState
- SecurityStateAtEL
- SendEvent
- SendEventLocal
- SetAccumulatedFPExceptions
- SetPSTATEFromPSR
- ShouldAdvanceHS
- ShouldAdvanceIT
- ShouldAdvanceSS
- ShouldSetPPEND
- SmallestTranslationGranule
- SpeculationBarrier
- SyncCounterOverflowed
- SynchronizeContext
- SynchronizeErrors
- TakeUnmaskedPhysicalSErrorInterrupts
- TakeUnmaskedSErrorInterrupts
- ThisInstr
- ThisInstrLength
- UndefinedInjectionCheck
- UsingAArch32
- ValidSecurityStateAtEL
- VirtualFIQPending
- VirtualIRQPending
- WFxType
- WaitForEvent
- WaitForInterrupt
- WatchpointRelatedSyndrome
- ASID\_NONE
- Broadcast
- BroadcastTLBI
- TLBI
- TLBILevel
- TLBIMemAttr
- TLBIOp
- TLBIRecord
- VMID
- VMID\_NONE
- ConstrainUnpredictable
- ConstrainUnpredictableBits

- ConstrainUnpredictableBool
- ConstrainUnpredictableInteger
- ConstrainUnpredictableProcedure
- Constraint
- Unpredictable
- AdvSIMDExpandImm
- MatMulAdd
- PolynomialMult
- SatQ
- ShiftSat
- SignedSat
- SignedSatQ
- UnsignedRSqrtEstimate
- UnsignedRecipEstimate
- UnsignedSat
- UnsignedSatQ

## J1.3.3.1 EncodeLDFSC

```
// EncodeLDFSC() // ============= // Function that gives the Long-descriptor FSC code for types of Fault bits(6) EncodeLDFSC(Fault statuscode, integer level) bits(6) result; // 128-bit descriptors will start from level -2 for 4KB to resolve bits IA[55:51] if level == -2 then assert IsFeatureImplemented(FEAT_D128); case statuscode of when Fault_AddressSize result = '101100'; when Fault_Translation result = '101010'; when Fault_SyncExternalOnWalk result = '010010'; when Fault_SyncParityOnWalk result = '011010'; assert !IsFeatureImplemented(FEAT_RAS); when Fault_GPCFOnWalk result = '100010'; otherwise Unreachable(); return result; if level == -1 then assert IsFeatureImplemented(FEAT_LPA2); case statuscode of when Fault_AddressSize result = '101001'; when Fault_Translation result = '101011'; when Fault_SyncExternalOnWalk result = '010011'; when Fault_SyncParityOnWalk result = '011011'; assert !IsFeatureImplemented(FEAT_RAS); when Fault_GPCFOnWalk result = '100011'; otherwise Unreachable(); return result; case statuscode of when Fault_AddressSize result = '0000':level<1:0>; assert level IN {0,1,2,3}; when Fault_AccessFlag result = '0010':level<1:0>; assert level IN {0,1,2,3}; when Fault_Permission result = '0011':level<1:0>; assert level IN {0,1,2,3}; when Fault_Translation result = '0001':level<1:0>; assert level IN {0,1,2,3}; when Fault_SyncExternal result = '010000';
```

```
when Fault_SyncExternalOnWalk result = '0101':level<1:0>; assert level IN {0,1,2,3}; when Fault_SyncParity result = '011000'; when Fault_SyncParityOnWalk result = '0111':level<1:0>; assert level IN {0,1,2,3}; when Fault_AsyncParity result = '011001'; when Fault_AsyncExternal result = '010001'; assert UsingAArch32(); when Fault_TagCheck result = '010001'; assert IsFeatureImplemented(FEAT_MTE2); when Fault_Alignment result = '100001'; when Fault_Debug result = '100010'; when Fault_GPCFOnWalk result = '1001':level<1:0>; assert level IN {0,1,2,3}; when Fault_GPCFOnOutput result = '101000'; when Fault_TLBConflict result = '110000'; when Fault_HWUpdateAccessFlag result = '110001'; when Fault_Lockdown result = '110100'; // IMPLEMENTATION DEFINED when Fault_Exclusive result = '110101'; // IMPLEMENTATION DEFINED otherwise Unreachable(); return result;
```

## J1.3.3.2 IPAValid

```
// IPAValid() // ========== // Return TRUE if the IPA is reported for the abort boolean IPAValid(FaultRecord fault) assert fault.statuscode != Fault_None; if fault.gpcf.gpf != GPCF_None then return fault.secondstage; elsif fault.s2fs1walk then return fault.statuscode IN { Fault_AccessFlag, Fault_Permission, Fault_Translation, Fault_AddressSize }; elsif fault.secondstage then return fault.statuscode IN { Fault_AccessFlag, Fault_Translation, Fault_AddressSize }; else return FALSE;
```

## J1.3.3.3 IsAsyncAbort

```
// IsAsyncAbort() // ============== // Returns TRUE if the abort currently being processed is an asynchronous abort, and FALSE // otherwise. boolean IsAsyncAbort(Fault statuscode) assert statuscode != Fault_None; return (statuscode IN {Fault_AsyncExternal, Fault_AsyncParity}); // IsAsyncAbort() // ============== boolean IsAsyncAbort(FaultRecord fault) return IsAsyncAbort(fault.statuscode);
```

## J1.3.3.4 IsDebugException

```
// IsDebugException() // ================== boolean IsDebugException(FaultRecord fault) assert fault.statuscode != Fault_None; return fault.statuscode == Fault_Debug;
```

## J1.3.3.5 IsExternalAbort // IsExternalAbort() // ================= // Returns TRUE if the abort currently being processed is an External abort and FALSE otherwise. boolean IsExternalAbort(Fault statuscode) assert statuscode != Fault\_None; return (statuscode IN { Fault\_SyncExternal, Fault\_SyncParity, Fault\_SyncExternalOnWalk, Fault\_SyncParityOnWalk, Fault\_AsyncExternal, Fault\_AsyncParity }); // IsExternalAbort() // ================= boolean IsExternalAbort(FaultRecord fault) return IsExternalAbort(fault.statuscode) || fault.gpcf.gpf == GPCF\_EABT; J1.3.3.6 IsExternalAbortOnWalk // IsExternalAbortOnWalk() // ======================= boolean IsExternalAbortOnWalk(FaultRecord fault) assert fault.statuscode != Fault\_None; return fault.statuscode IN {Fault\_SyncExternalOnWalk, Fault\_SyncParityOnWalk}; J1.3.3.7 IsExternalSyncAbort IN {Fault\_SyncParity, Fault\_SyncParityOnWalk};

```
// IsExternalSyncAbort() // ===================== // Returns TRUE if the abort currently being processed is an external // synchronous abort and FALSE otherwise. boolean IsExternalSyncAbort(Fault statuscode) assert statuscode != Fault_None; if IsFeatureImplemented(FEAT_RAS) then assert ! statuscode return (statuscode IN { Fault_SyncExternal, Fault_SyncParity, Fault_SyncExternalOnWalk, Fault_SyncParityOnWalk });
```

```
// IsExternalSyncAbort() // ===================== boolean IsExternalSyncAbort(FaultRecord fault) return IsExternalSyncAbort(fault.statuscode) || fault.gpcf.gpf == GPCF_EABT;
```

## J1.3.3.8 IsFault

```
// IsFault() // ========= // Return TRUE if a fault is associated with an address descriptor boolean IsFault(AddressDescriptor addrdesc) return addrdesc.fault.statuscode != Fault_None; // IsFault() // ========= // Return TRUE if a fault is associated with a memory access. boolean IsFault(Fault fault) return fault != Fault_None; // IsFault() // ========= // Return TRUE if a fault is associated with status returned by memory. boolean IsFault(PhysMemRetStatus retstatus) return retstatus.statuscode != Fault_None;
```

## J1.3.3.9 IsSErrorInterrupt

```
// IsSErrorInterrupt() // =================== // Returns TRUE if the abort currently being processed is an SError interrupt, and FALSE // otherwise. boolean IsSErrorInterrupt(Fault statuscode) assert statuscode != Fault_None; return (statuscode IN {Fault_AsyncExternal, Fault_AsyncParity}); // IsSErrorInterrupt() // =================== boolean IsSErrorInterrupt(FaultRecord fault) return IsSErrorInterrupt(fault.statuscode); // Add a specific type of return value for FaultSyndrome type IssType is ( bits(25) iss, bits(24) iss2 )
```

## J1.3.3.10 IsSecondStage

```
// IsSecondStage() // =============== boolean IsSecondStage(FaultRecord fault) assert fault.statuscode != Fault_None; return fault.secondstage;
```

## J1.3.3.11 LSInstructionSyndrome

```
// LSInstructionSyndrome() // ======================= // Returns the extended syndrome information for a second stage fault. // <10> -Syndrome valid bit. The syndrome is valid only for certain types of access instruction. // <9:8> -Access size. // <7> -Sign extended (for loads). // <6:2> -Transfer register. // <1> -Transfer register is 64-bit. // <0> -Instruction has acquire/release semantics.
```

bits(11) LSInstructionSyndrome();

## J1.3.3.12 ReportAsGPCException

```
// ReportAsGPCException() // ====================== // Determine whether the given GPCF is reported as a Granule Protection Check Exception // rather than a Data or Instruction Abort boolean ReportAsGPCException(FaultRecord fault) assert IsFeatureImplemented(FEAT_RME); assert fault.statuscode IN {Fault_GPCFOnWalk, Fault_GPCFOnOutput}; assert fault.gpcf.gpf != GPCF_None; if Halted() && EDSCR.SDD == '1' then return FALSE; case fault.gpcf.gpf of when GPCF_Walk return TRUE; when GPCF_AddressSize return TRUE; when GPCF_EABT return TRUE; when GPCF_Fail return SCR_EL3.GPF == '1' && PSTATE.EL != EL3;
```

## J1.3.3.13 CACHE\_OP

```
// CACHE_OP() // ========== // Performs Cache maintenance operations as per CacheRecord. CACHE_OP(CacheRecord cache) IMPLEMENTATION_DEFINED;
```

## J1.3.3.14 CPASAtPAS

```
// CPASAtPAS() // =========== // Get cache PA space for given PA space. CachePASpace CPASAtPAS(PASpace pas) case pas of when PAS_NonSecure return CPAS_NonSecure; when PAS_Secure return CPAS_Secure; when PAS_Root return CPAS_Root; when PAS_Realm return CPAS_Realm; when PAS_SystemAgent
```

```
return CPAS_SystemAgent; when PAS_NonSecureProtected return CPAS_NonSecureProtected; when PAS_NA6 return CPAS_NA6; when PAS_NA7 return CPAS_NA7; otherwise Unreachable();
```

## J1.3.3.15 CPASAtSecurityState

```
// CPASAtSecurityState() // ===================== // Get cache PA space for given security state. CachePASpace CPASAtSecurityState(SecurityState ss) case ss of when SS_NonSecure return CPAS_NonSecure; when SS_Secure return CPAS_SecureNonSecure; when SS_Root return CPAS_Any; when SS_Realm return CPAS_RealmNonSecure;
```

## J1.3.3.16 CacheRecord

```
// CacheRecord // =========== // Details related to a cache operation. type CacheRecord is ( AccessType acctype, // Access type CacheOp cacheop, // Cache operation CacheOpScope opscope, // Cache operation type CacheType cachetype, // Cache type bits(64) regval, FullAddress paddress, bits(64) vaddress, // For VA operations integer setnum, // For SW operations integer waynum, // For SW operations integer level, // For SW operations Shareability shareability, boolean is_vmid_valid, // is vmid valid for current context bits(16) vmid, boolean is_asid_valid, // is asid valid for current context bits(16) asid, SecurityState security, // For cache operations to full cache or by setnum/waynum // For operations by address, PA space in paddress CachePASpace cpas )
```

## J1.3.3.17 DecodeSW

```
// DecodeSW() // ========== // Decode input value into setnum, waynum and level for SW instructions.
```

```
(integer, integer, integer) DecodeSW(bits(64) regval, CacheType cachetype) constant integer level = UInt(regval<3:1>); (numsets, associativity, linesize) = GetCacheInfo(level, cachetype); // For the given level and cachetype, get the number of sets, associativity and // cache line size in terms of actual bytes. constant integer waybits = CeilLog2(associativity); constant integer setbits = CeilLog2(numsets); constant integer linebits = Log2(linesize); constant integer waynum = if associativity == 1 then 0 else UInt(regval<31:32-waybits>); constant integer setnum = if numsets == 1 then 0 else UInt(regval<linebits +: setbits>); return (setnum, waynum, level); J1.3.3.18 GetCacheInfo // GetCacheInfo() // ============== // Returns numsets, assosciativity & linesize in terms of actual bytes. (integer, integer, integer) GetCacheInfo(integer level, CacheType cachetype); J1.3.3.19 ASR // ASR() // ===== bits(N) ASR(bits(N) x, integer shift) assert shift >= 0; bits(N) result; if shift == 0 then result = x; else (result, -) = ASR_C(x, shift); return result; J1.3.3.20 ASR_C // ASR_C() // ======= (bits(N), bit) ASR_C(bits(N) x, integer shift) assert shift > 0 && shift < 256; extended_x = SignExtend(x, shift+N); result = extended_x<(shift+N)-1:shift>; carry_out = extended_x<shift-1>; return (result, carry_out); J1.3.3.21 Abs -x;
```

```
// Abs() // ===== integer Abs(integer x) return if x >= 0 then x else // Abs() // =====
```

```
real Abs(real x) return if x >= 0.0 then x else -x;
```

## J1.3.3.22 Align

```
// Align() // ======= integer Align(integer x, integer y) return y * (x DIV y); // Align() // ======= bits(N) Align(bits(N) x, integer y) return Align(UInt(x), y)<N-1:0>;
```

## J1.3.3.23 BitCount

```
// BitCount() // ========== integer BitCount(bits(N) x) integer result = 0; for i = 0 to N-1 if x<i> == '1' then result = result + 1; return result;
```

## J1.3.3.24 CeilLog2

```
// CeilLog2() // ========== // For a positive integer X, return the Log2() of X, rounded up to the next integer integer CeilLog2(integer x) assert x != 0; return Log2(CeilPow2(x));
```

## J1.3.3.25 CeilPow2

```
// CeilPow2() // ========== // For a positive integer X, return the smallest power of 2 >= X integer CeilPow2(integer x) if x == 0 then return 0; if x == 1 then return 1; return FloorPow2(x - 1) * 2;
```

## J1.3.3.26 CountLeadingSignBits

```
// CountLeadingSignBits() // ====================== integer CountLeadingSignBits(bits(N) x) return CountLeadingZeroBits(x<N-1:1> EOR x<N-2:0>);
```

## J1.3.3.27 CountLeadingZeroBits

```
// CountLeadingZeroBits() // ====================== integer CountLeadingZeroBits(bits(N) x) return N - (HighestSetBit(x) + 1);
```

## J1.3.3.28 Elem

```
// Elem -getter // ============= bits(size) Elem[bits(N) vector, integer e, integer size] assert e >= 0 && (e+1)*size <= N; constant integer ebase = e * size; return vector<ebase + size - 1 : ebase>; // Elem -setter // ============= Elem[bits(N) &vector, integer e, integer size] = bits(size) value assert e >= 0 && (e+1)*size <= N; constant integer ebase = e * size; vector<ebase + size - 1 : ebase> = value; return;
```

## J1.3.3.29 Extend

```
// Extend() // ======== bits(N) Extend(bits(M) x, integer N, boolean unsigned) return if unsigned then ZeroExtend(x, N) else SignExtend(x, N);
```

## J1.3.3.30 FloorPow2

```
// FloorPow2() // =========== // For a positive integer X, return the largest power of 2 <= X integer FloorPow2(integer x) assert x >= 0; integer n = 1; if x == 0 then return 0; while x >= 2^n do n = n + 1; return 2^(n - 1);
```

## J1.3.3.31 HighestSetBit

```
// HighestSetBit() // =============== integer HighestSetBit(bits(N) x) for i = N-1 downto 0 if x<i> == '1' then return i; return -1;
```

## J1.3.3.32 HighestSetBitNZ

```
// HighestSetBitNZ // =============== // Position of the highest 1 bit in a bitvector. // Asserts if the bitvector is entirely zero. integer HighestSetBitNZ(bits(N) x) assert !IsZero(x); return HighestSetBit(x);
```

## J1.3.3.33 IsAligned

```
// IsAligned() // =========== boolean IsAligned(bits(N) x, integer y) return x == Align(x, y);
```

## J1.3.3.34 IsAlignedP2

```
// IsAlignedP2() // ============= boolean IsAlignedP2(bits(N) x, integer p2) if N == 0 || p2 == 0 then return TRUE; return IsZero(x<p2-1:0>);
```

## J1.3.3.35 IsEven

```
// IsEven() // ======== boolean IsEven(integer val) return val MOD 2 == 0;
```

## J1.3.3.36 IsOdd

```
// IsOdd() // ======= boolean IsOdd(integer val) return val MOD 2 == 1;
```

## J1.3.3.37 IsOnes

```
// IsOnes() // ======== boolean IsOnes(bits(N) x) return x == Ones(N);
```

## J1.3.3.38 IsPow2

```
// IsPow2() // ======== // Return TRUE if integer X is positive and a power of 2. Otherwise, // return FALSE. boolean IsPow2(integer x) if x <= 0 then return FALSE; return FloorPow2(x) == CeilPow2(x);
```

## J1.3.3.39 IsZero

```
// IsZero() // ======== boolean IsZero(bits(N) x) return x == Zeros(N);
```

## J1.3.3.40 IsZeroBit

```
// IsZeroBit() // =========== bit IsZeroBit(bits(N) x) return if IsZero(x) then '1' else '0';
```

## J1.3.3.41 LSL

```
// LSL() // ===== bits(N) LSL(bits(N) x, integer shift) assert shift >= 0; bits(N) result; if shift == 0 then result = x; else (result, -) = LSL_C(x, shift); return result;
```

## J1.3.3.42 LSL\_C

```
// LSL_C() // ======= (bits(N), bit) LSL_C(bits(N) x, integer shift) assert shift > 0 && shift < 256; extended_x = x : Zeros(shift); result = extended_x<N-1:0>; carry_out = extended_x<N>; return (result, carry_out);
```

## J1.3.3.43 LSR

```
// LSR() // ===== bits(N) LSR(bits(N) x, integer shift) assert shift >= 0; bits(N) result; if shift == 0 then result = x; else (result, -) = LSR_C(x, shift); return result;
```

## J1.3.3.44 LSR\_C

```
// LSR_C() // ======= (bits(N), bit) LSR_C(bits(N) x, integer shift) assert shift > 0 && shift < 256; extended_x = ZeroExtend(x, shift+N); result = extended_x<(shift+N)-1:shift>; carry_out = extended_x<shift-1>; return (result, carry_out);
```

## J1.3.3.45 LowestSetBit

```
// LowestSetBit() // ============== integer LowestSetBit(bits(N) x) for i = 0 to N-1 if x<i> == '1' then return i; return N;
```

## J1.3.3.46 LowestSetBitNZ

```
// LowestSetBitNZ // ============== // Position of the lowest 1 bit in a bitvector. // Asserts if the bit-vector is entirely zero. integer LowestSetBitNZ(bits(N) x) assert !IsZero(x); return LowestSetBit(x);
```

## J1.3.3.47 Max

```
// Max() // ===== integer Max(integer a, integer b) return if a >= b then a else b; // Max() // ===== real Max(real a, real b) return if a >= b then a else b;
```

## J1.3.3.48 Min

```
// Min() // ===== integer Min(integer a, integer b) return if a <= b then a else b; // Min() // ===== real Min(real a, real b) return if a <= b then a else b;
```

## J1.3.3.49 NormalizeReal

```
// NormalizeReal // ============= // Normalizes x to the form 1.xxx... x 2^y and returns (mantissa, exponent) (real, integer) NormalizeReal(real x) real mantissa = x; integer exponent = 0; while mantissa < 1.0 do mantissa = mantissa * 2.0; exponent = exponent - 1; while mantissa >= 2.0 do mantissa = mantissa / 2.0; exponent = exponent + 1; return (mantissa, exponent);
```

## J1.3.3.50 Ones

```
// Ones() // ====== bits(N) Ones(integer N) return Replicate('1',N);
```

## J1.3.3.51 ROL

```
// ROL() // ===== bits(N) ROL(bits(N) x, integer shift) assert shift >= 0 && shift <= N; if (shift == 0) then return x; return ROR(x, N-shift);
```

## J1.3.3.52 ROR

```
// ROR() // ===== bits(N) ROR(bits(N) x, integer shift) assert shift >= 0; bits(N) result; if shift == 0 then result = x; else
```

```
(result, -) = ROR_C(x, shift); return result;
```

## J1.3.3.53 ROR\_C

```
// ROR_C() // ======= (bits(N), bit) ROR_C(bits(N) x, integer shift) assert shift != 0 && shift < 256; m = shift MOD N; result = LSR(x,m) OR LSL(x,N-m); carry_out = result<N-1>; return (result, carry_out);
```

## J1.3.3.54 RShr

```
// RShr() // ====== // Shift integer value right with rounding integer RShr(integer value, integer shift, boolean round) assert shift > 0; if round then return (value + (1 << (shift - 1))) >> shift; else return value >> shift;
```

## J1.3.3.55 Replicate

```
// Replicate() // =========== bits(M*N) Replicate(bits(M) x, integer N);
```

## J1.3.3.56 Reverse

```
// Reverse() // ========= // Reverse subwords of M bits in an N-bit word bits(N) Reverse(bits(N) word, integer M) assert M > 0; assert N MOD M == 0; bits(N) result; constant integer swsize = M; constant integer sw = N DIV swsize; for s = 0 to sw-1 Elem[result, (sw - 1) -s, swsize] = Elem[word, s, swsize]; return result;
```

## J1.3.3.57 RoundDown

```
// RoundDown() // =========== integer RoundDown(real x);
```

## J1.3.3.58 RoundTowardsZero

```
// RoundTowardsZero() // ================== integer RoundTowardsZero(real x) return if x == 0.0 then 0 else if x >= 0.0 then RoundDown(x) else RoundUp(x);
```

## J1.3.3.59 RoundUp

```
// RoundUp() // ========= integer RoundUp(real x);
```

## J1.3.3.60 SInt

```
// SInt() // ====== integer SInt(bits(N) x) result = 0; for i = 0 to N-1 if x<i> == '1' then result = result + 2^i; if x<N-1> == '1' then result = result - 2^N; return result;
```

## J1.3.3.61 SignExtend

```
// SignExtend() // ============ bits(N) SignExtend(bits(M) x, integer N) assert N >= M; return Replicate(x<M-1>, N-M) : x;
```

## J1.3.3.62 Signal

```
// Signal // ====== // Available signal types enumeration Signal {LOW, HIGH};
```

## J1.3.3.63 UInt

```
// UInt() // ====== integer UInt(bits(N) x) result = 0; for i = 0 to N-1 if x<i> == '1' then result = result + 2^i; return result;
```

## J1.3.3.64 ZeroExtend

```
// ZeroExtend() // ============ bits(N) ZeroExtend(bits(M) x, integer N) assert N >= M; return Zeros(N-M) : x;
```

## J1.3.3.65 Zeros

```
// Zeros() // ======= bits(N) Zeros(integer N) return Replicate('0',N);
```

## J1.3.3.66 AArch32.CheckTimerConditions

```
// AArch32.CheckTimerConditions() // ============================== // Checking timer conditions for all A32 timer registers AArch32.CheckTimerConditions() boolean status; bits(64) offset; offset = Zeros(64); assert !HaveAArch64(); if HaveEL(EL3) then if CNTP_CTL_S.ENABLE == '1' then status = IsTimerConditionMet(offset, CNTP_CVAL_S, CNTP_CTL_S.IMASK, InterruptID_CNTPS); CNTP_CTL_S.ISTATUS = if status then '1' else '0'; if CNTP_CTL_NS.ENABLE == '1' then status = IsTimerConditionMet(offset, CNTP_CVAL_NS, CNTP_CTL_NS.IMASK, InterruptID_CNTP); CNTP_CTL_NS.ISTATUS = if status then '1' else '0'; else if CNTP_CTL.ENABLE == '1' then status = IsTimerConditionMet(offset, CNTP_CVAL, CNTP_CTL.IMASK, InterruptID_CNTP); CNTP_CTL.ISTATUS = if status then '1' else '0'; if HaveEL(EL2) && CNTHP_CTL.ENABLE == '1' then status = IsTimerConditionMet(offset, CNTHP_CVAL, CNTHP_CTL.IMASK, InterruptID_CNTHP); CNTHP_CTL.ISTATUS = if status then '1' else '0'; if CNTV_CTL_EL0.ENABLE == '1' then status = IsTimerConditionMet(CNTVOFF_EL2, CNTV_CVAL_EL0, CNTV_CTL_EL0.IMASK, InterruptID_CNTV); CNTV_CTL_EL0.ISTATUS = if status then '1' else '0'; return;
```

## J1.3.3.67 AArch64.CheckTimerConditions

```
// AArch64.CheckTimerConditions() // ============================== // Checking timer conditions for all A64 timer registers
```

```
AArch64.CheckTimerConditions() boolean status; bits(64) offset; bit imask; constant SecurityState ss = CurrentSecurityState(); if (IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && !ELIsInHost(EL0) && CNTHCTL_EL2.ECV == '1' && SCR_EL3.ECVEn == '1') then offset = CNTPOFF_EL2; else offset = Zeros(64); if CNTP_CTL_EL0.ENABLE == '1' then imask = CNTP_CTL_EL0.IMASK; if (IsFeatureImplemented(FEAT_RME) && ss IN {SS_Root, SS_Realm} && CNTHCTL_EL2.CNTPMASK == '1') then imask = '1'; status = IsTimerConditionMet(offset, CNTP_CVAL_EL0, imask, InterruptID_CNTP); CNTP_CTL_EL0.ISTATUS = if status then '1' else '0'; if ((HaveEL(EL3) || (HaveEL(EL2) && !IsFeatureImplemented(FEAT_SEL2))) && CNTHP_CTL_EL2.ENABLE == '1') then status = IsTimerConditionMet(Zeros(64), CNTHP_CVAL_EL2, CNTHP_CTL_EL2.IMASK, InterruptID_CNTHP); CNTHP_CTL_EL2.ISTATUS = if status then '1' else '0'; if HaveEL(EL2) && IsFeatureImplemented(FEAT_SEL2) && CNTHPS_CTL_EL2.ENABLE == '1' then status = IsTimerConditionMet(Zeros(64), CNTHPS_CVAL_EL2, CNTHPS_CTL_EL2.IMASK, InterruptID_CNTHPS); CNTHPS_CTL_EL2.ISTATUS = if status then '1' else '0'; if CNTPS_CTL_EL1.ENABLE == '1' then status = IsTimerConditionMet(Zeros(64), CNTPS_CVAL_EL1, CNTPS_CTL_EL1.IMASK, InterruptID_CNTPS); CNTPS_CTL_EL1.ISTATUS = if status then '1' else '0'; if CNTV_CTL_EL0.ENABLE == '1' then imask = CNTV_CTL_EL0.IMASK; if (IsFeatureImplemented(FEAT_RME) && ss IN {SS_Root, SS_Realm} && CNTHCTL_EL2.CNTVMASK == '1') then imask = '1'; status = IsTimerConditionMet(CNTVOFF_EL2, CNTV_CVAL_EL0, imask, InterruptID_CNTV); CNTV_CTL_EL0.ISTATUS = if status then '1' else '0'; if ((IsFeatureImplemented(FEAT_VHE) && (HaveEL(EL3) || !IsFeatureImplemented(FEAT_SEL2))) && CNTHV_CTL_EL2.ENABLE == '1') then status = IsTimerConditionMet(Zeros(64), CNTHV_CVAL_EL2, CNTHV_CTL_EL2.IMASK, InterruptID_CNTHV); CNTHV_CTL_EL2.ISTATUS = if status then '1' else '0'; if ((IsFeatureImplemented(FEAT_SEL2) && IsFeatureImplemented(FEAT_VHE)) && CNTHVS_CTL_EL2.ENABLE == '1') then status = IsTimerConditionMet(Zeros(64), CNTHVS_CVAL_EL2, CNTHVS_CTL_EL2.IMASK, InterruptID_CNTHVS); CNTHVS_CTL_EL2.ISTATUS = if status then '1' else '0'; return;
```

## J1.3.3.68 CNTHCTL\_EL2\_VHE

```
// CNTHCTL_EL2_VHE() // ================= // In the case where EL2 accesses the CNTKCTL_EL1 register, and the // is redirected to CNTHCTL_EL2 as a result of HCR_EL2.E2H being 1, // then the bits of CNTHCTL_EL2 that are RES0 in CNTKCTL_EL1 are // treated as being UNKNOWN. This function applies the UNKNOWN behavior.
```

bits(64) CNTHCTL\_EL2\_VHE(bits(64)

```
access original_value)
```

```
assert PSTATE.EL == EL2; assert HCR_EL2.E2H == '1'; bits(64) return_value = original_value; if !IsFeatureImplemented(FEAT_NV2p1) then return_value<19:18> = bits(2) UNKNOWN; return_value<16:10> = bits(7) UNKNOWN; return return_value;
```

## J1.3.3.69 GenericCounterTick

```
// GenericCounterTick() // ==================== // Increments PhysicalCount value for every clock tick. GenericCounterTick() bits(64) prev_physical_count; if CNTCR.EN == '0' then if !HaveAArch64() then AArch32.CheckTimerConditions(); else AArch64.CheckTimerConditions(); return; prev_physical_count = PhysicalCountInt(); if IsFeatureImplemented(FEAT_CNTSC) && CNTCR.SCEN == '1' then PhysicalCount = PhysicalCount + ZeroExtend(CNTSCR, 88); else PhysicalCount<87:24> = PhysicalCount<87:24> + 1; if !HaveAArch64() then AArch32.CheckTimerConditions(); else AArch64.CheckTimerConditions(); TestEventCNTP(prev_physical_count, PhysicalCountInt()); TestEventCNTV(prev_physical_count, PhysicalCountInt()); return;
```

## J1.3.3.70 IsLocalTimeoutEventPending

boolean IsLocalTimeoutEventPending;

## J1.3.3.71 IsTimerConditionMet

```
// IsTimerConditionMet() // ===================== boolean IsTimerConditionMet(bits(64) offset, bits(64) compare_value, bits(1) imask, InterruptID intid) boolean condition_met; Signal level; condition_met = (UInt(PhysicalCountInt() offset) UInt(compare_value)) >= 0; level = if condition_met && imask == '0' then HIGH else LOW; SetInterruptRequestLevel(intid, level); return condition_met;
```

## J1.3.3.72 LocalTimeoutVal

bits(64) LocalTimeoutVal;

// Value to compare against the Virtual Counter Timer

## J1.3.3.73 PhysicalCount

bits(88) PhysicalCount;

## J1.3.3.74 SetEventRegister

```
// SetEventRegister() // ================== // Sets the Event Register of this PE SetEventRegister() EventRegister = '1'; return;
```

## J1.3.3.75 TestEventCNTP

```
// TestEventCNTP() // =============== // Generate Event stream from the physical counter TestEventCNTP(bits(64) prev_physical_count, bits(64) current_physical_count) bits(64) offset; bits(1) samplebit, previousbit; integer n; if CNTHCTL_EL2.EVNTEN == '1' then n = UInt(CNTHCTL_EL2.EVNTI); if IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EVNTIS == '1' then n = n + 8; if (IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && !ELIsInHost(EL0) && CNTHCTL_EL2.ECV == '1' && SCR_EL3.ECVEn == '1') then offset = CNTPOFF_EL2; else offset = Zeros(64); samplebit = (current_physical_count - offset)<n>; previousbit = (prev_physical_count -offset)<n>; if CNTHCTL_EL2.EVNTDIR == '0' then if previousbit == '0' && samplebit == '1' then SetEventRegister(); else if previousbit == '1' && samplebit == '0' then SetEventRegister(); return;
```

## J1.3.3.76 TestEventCNTV

```
// TestEventCNTV() // =============== // Generate Event stream from the virtual counter TestEventCNTV(bits(64) prev_physical_count, bits(64) current_physical_count) bits(64) offset; bits(1) samplebit, previousbit; integer n; if (EffectiveHCR_EL2_E2H():EffectiveTGE() != '11' && CNTKCTL_EL1.EVNTEN == '1') then n = UInt(CNTKCTL_EL1.EVNTI); if IsFeatureImplemented(FEAT_ECV) && CNTKCTL_EL1.EVNTIS == '1' then n = n + 8; offset = if HaveEL(EL2) then CNTVOFF_EL2 else Zeros(64); samplebit = (current_physical_count - offset)<n>; previousbit = (prev_physical_count -offset)<n>; if CNTKCTL_EL1.EVNTDIR == '0' then
```

```
if previousbit == '0' && samplebit == '1' then SetEventRegister(); else if previousbit == '1' && samplebit == '0' then SetEventRegister(); return;
```

## J1.3.3.77 VirtualCounterTimer

```
// VirtualCounterTimer() // ===================== // Returns the Counter-Timer Virtual Count value, the value is as read by CurrentEL to CNTVCT_EL0. bits(64) VirtualCounterTimer() bits(64) cntvct; if PSTATE.EL != EL3 then if HaveEL(EL2) && !ELIsInHost(PSTATE.EL) then cntvct = PhysicalCountInt() -CNTVOFF_EL2; else cntvct = PhysicalCountInt(); else if HaveEL(EL2) && !ELUsingAArch32(EL2) then cntvct = PhysicalCountInt() -CNTVOFF_EL2; elsif HaveEL(EL2) && ELUsingAArch32(EL2) then cntvct = PhysicalCountInt() CNTVOFF; else cntvct = PhysicalCountInt(); return cntvct;
```

## J1.3.3.78 BitReverse

```
// BitReverse() // ============ bits(N) BitReverse(bits(N) data) bits(N) result; for i = 0 to N-1 result<(N-i)-1> = data<i>; return result;
```

## J1.3.3.79 Poly32Mod2

```
// Poly32Mod2() // ============ // Poly32Mod2 on a bitstring does a polynomial Modulus over {0,1} operation bits(32) Poly32Mod2(bits(N) data_in, bits(32) poly) assert N > 32; bits(N) data = data_in; for i = N-1 downto 32 if data<i> == '1' then data<i-1:0> = data<i-1:0> EOR (poly:Zeros(i-32)); return data<31:0>;
```

## J1.3.3.80 AESInvMixColumns

```
// AESInvMixColumns() // ================== // Transformation in the Inverse Cipher that is the inverse of AESMixColumns. bits(128) AESInvMixColumns(bits (128) op) constant bits(4*8) in0 = op< 96+:8> : op< 64+:8> : op< 32+:8> : op< 0+:8>; constant bits(4*8) in1 = op<104+:8> : op< 72+:8> : op< 40+:8> : op< 8+:8>; constant bits(4*8) in2 = op<112+:8> : op< 80+:8> : op< 48+:8> : op< 16+:8>; constant bits(4*8) in3 = op<120+:8> : op< 88+:8> : op< 56+:8> : op< 24+:8>; bits(4*8) out0; bits(4*8) out1; bits(4*8) out2; bits(4*8) out3; for c = 0 to 3 out0<c*8+:8> = (FFmul0E(in0<c*8+:8>) EOR FFmul0B(in1<c*8+:8>) EOR FFmul0D(in2<c*8+:8>) EOR FFmul09(in3<c*8+:8>)); out1<c*8+:8> = (FFmul09(in0<c*8+:8>) EOR FFmul0E(in1<c*8+:8>) EOR FFmul0B(in2<c*8+:8>) EOR FFmul0D(in3<c*8+:8>)); out2<c*8+:8> = (FFmul0D(in0<c*8+:8>) EOR FFmul09(in1<c*8+:8>) EOR FFmul0E(in2<c*8+:8>) EOR FFmul0B(in3<c*8+:8>)); out3<c*8+:8> = (FFmul0B(in0<c*8+:8>) EOR FFmul0D(in1<c*8+:8>) EOR FFmul09(in2<c*8+:8>) EOR FFmul0E(in3<c*8+:8>)); return ( out3<3*8+:8> : out2<3*8+:8> : out1<3*8+:8> : out0<3*8+:8> : out3<2*8+:8> : out2<2*8+:8> : out1<2*8+:8> : out0<2*8+:8> : out3<1*8+:8> : out2<1*8+:8> : out1<1*8+:8> : out0<1*8+:8> : out3<0*8+:8> : out2<0*8+:8> : out1<0*8+:8> : out0<0*8+:8> );
```

```
J1.3.3.81 AESInvShiftRows // AESInvShiftRows() // ================= // Transformation in the Inverse Cipher that is inverse of AESShiftRows. bits(128) AESInvShiftRows(bits(128) op) return ( op< 31: 24> : op< 55: 48> : op< 79: 72> : op<103: 96> : op<127:120> : op< 23: 16> : op< 47: 40> : op< 71: 64> : op< 95: 88> : op<119:112> : op< 15: 8> : op< 39: 32> : op< 63: 56> : op< 87: 80> : op<111:104> : op< 7: 0> ); J1.3.3.82 AESInvSubBytes of AESSubBytes.
```

```
// AESInvSubBytes() // ================ // Transformation in the Inverse Cipher that is the inverse bits(128) AESInvSubBytes(bits(128) op) // Inverse S-box values constant bits(16*16*8) GF2_inv = ( /* F E D C B A 9 8 7 6 5 4 3 2 1 0 */ /*F*/ 0x7d0c2155631469e126d677ba7e042b17<127:0> : /*E*/ 0x619953833cbbebc8b0f52aae4d3be0a0<127:0> : /*D*/ 0xef9cc9939f7ae52d0d4ab519a97f5160<127:0> : /*C*/ 0x5fec8027591012b131c7078833a8dd1f<127:0> : /*B*/ 0xf45acd78fec0db9a2079d2c64b3e56fc<127:0> :
```

```
/*A*/ 0x1bbe18aa0e62b76f89c5291d711af147<127:0> : /*9*/ 0x6edf751ce837f9e28535ade72274ac96<127:0> : /*8*/ 0x73e6b4f0cecff297eadc674f4111913a<127:0> : /*7*/ 0x6b8a130103bdafc1020f3fca8f1e2cd0<127:0> : /*6*/ 0x0645b3b80558e4f70ad3bc8c00abd890<127:0> : /*5*/ 0x849d8da75746155edab9edfd5048706c<127:0> : /*4*/ 0x92b6655dcc5ca4d41698688664f6f872<127:0> : /*3*/ 0x25d18b6d49a25b76b224d92866a12e08<127:0> : /*2*/ 0x4ec3fa420b954cee3d23c2a632947b54<127:0> : /*1*/ 0xcbe9dec444438e3487ff2f9b8239e37c<127:0> : /*0*/ 0xfbd7f3819ea340bf38a53630d56a0952<127:0> ); bits(128) out; for i = 0 to 15 out<i*8+:8> = GF2_inv<UInt(op<i*8+:8>)*8+:8>; return out; J1.3.3.83 AESMixColumns // AESMixColumns() // =============== // Transformation in the Cipher that takes all of the columns of the // State and mixes their data (independently of one another) to // produce new columns. bits(128) AESMixColumns(bits (128) op) constant bits(4*8) in0 = op< 96+:8> : op< 64+:8> : op< 32+:8> : op< 0+:8>; constant bits(4*8) in1 = op<104+:8> : op< 72+:8> : op< 40+:8> : op< 8+:8>; constant bits(4*8) in2 = op<112+:8> : op< 80+:8> : op< 48+:8> : op< 16+:8>; constant bits(4*8) in3 = op<120+:8> : op< 88+:8> : op< 56+:8> : op< 24+:8>; bits(4*8) out0; bits(4*8) out1; bits(4*8) out2; bits(4*8) out3; for c = 0 to 3 out0<c*8+:8> = (FFmul02(in0<c*8+:8>) EOR FFmul03(in1<c*8+:8>) EOR in2<c*8+:8> EOR in3<c*8+:8>); out1<c*8+:8> = (FFmul02(in1<c*8+:8>) EOR FFmul03(in2<c*8+:8>) EOR in3<c*8+:8> EOR in0<c*8+:8>); out2<c*8+:8> = (FFmul02(in2<c*8+:8>) EOR FFmul03(in3<c*8+:8>) EOR in0<c*8+:8> EOR in1<c*8+:8>); out3<c*8+:8> = (FFmul02(in3<c*8+:8>) EOR FFmul03(in0<c*8+:8>) EOR in1<c*8+:8> EOR in2<c*8+:8>); return ( out3<3*8+:8> : out2<3*8+:8> : out1<3*8+:8> : out0<3*8+:8> : out3<2*8+:8> : out2<2*8+:8> : out1<2*8+:8> : out0<2*8+:8> : out3<1*8+:8> : out2<1*8+:8> : out1<1*8+:8> : out0<1*8+:8> : out3<0*8+:8> : out2<0*8+:8> : out1<0*8+:8> : out0<0*8+:8> ); J1.3.3.84 AESShiftRows by cyclically
```

```
// AESShiftRows() // ============== // Transformation in the Cipher that processes the State // shifting the last three rows of the State by different offsets. bits(128) AESShiftRows(bits(128) op) return ( op< 95: 88> : op< 55: 48> : op< 15: 8> : op<103: 96> :
```

```
op< 63: 56> : op< 23: 16> : op<111:104> : op< 71: 64> : op< 31: 24> : op<119:112> : op< 79: 72> : op< 39: 32> : op<127:120> : op< 87: 80> : op< 47: 40> : op< 7: 0> );
```

## J1.3.3.85 AESSubBytes

```
// AESSubBytes() // ============= // Transformation in the Cipher that processes the State using a nonlinear // byte substitution table (S-box) that operates on each of the State bytes // independently. bits(128) AESSubBytes(bits(128) op) // S-box values constant bits(16*16*8) GF2 = ( /* F E D C B A 9 8 7 6 5 4 3 2 1 0 */ /*F*/ 0x16bb54b00f2d99416842e6bf0d89a18c<127:0> : /*E*/ 0xdf2855cee9871e9b948ed9691198f8e1<127:0> : /*D*/ 0x9e1dc186b95735610ef6034866b53e70<127:0> : /*C*/ 0x8a8bbd4b1f74dde8c6b4a61c2e2578ba<127:0> : /*B*/ 0x08ae7a65eaf4566ca94ed58d6d37c8e7<127:0> : /*A*/ 0x79e4959162acd3c25c2406490a3a32e0<127:0> : /*9*/ 0xdb0b5ede14b8ee4688902a22dc4f8160<127:0> : /*8*/ 0x73195d643d7ea7c41744975fec130ccd<127:0> : /*7*/ 0xd2f3ff1021dab6bcf5389d928f40a351<127:0> : /*6*/ 0xa89f3c507f02f94585334d43fbaaefd0<127:0> : /*5*/ 0xcf584c4a39becb6a5bb1fc20ed00d153<127:0> : /*4*/ 0x842fe329b3d63b52a05a6e1b1a2c8309<127:0> : /*3*/ 0x75b227ebe28012079a059618c323c704<127:0> : /*2*/ 0x1531d871f1e5a534ccf73f362693fdb7<127:0> : /*1*/ 0xc072a49cafa2d4adf04759fa7dc982ca<127:0> : /*0*/ 0x76abd7fe2b670130c56f6bf27b777c63<127:0> ); bits(128) out; for i = 0 to 15 out<i*8+:8> = GF2<UInt(op<i*8+:8>)*8+:8>; return out;
```

## J1.3.3.86 FFmul02

```
// FFmul02() // ========= bits(8) FFmul02(bits(8) b) constant bits(256*8) FFmul_02 = ( /* F E D C B A 9 8 7 6 5 4 3 2 1 0 */ /*F*/ 0xE5E7E1E3EDEFE9EBF5F7F1F3FDFFF9FB<127:0> : /*E*/ 0xC5C7C1C3CDCFC9CBD5D7D1D3DDDFD9DB<127:0> : /*D*/ 0xA5A7A1A3ADAFA9ABB5B7B1B3BDBFB9BB<127:0> : /*C*/ 0x858781838D8F898B959791939D9F999B<127:0> : /*B*/ 0x656761636D6F696B757771737D7F797B<127:0> : /*A*/ 0x454741434D4F494B555751535D5F595B<127:0> : /*9*/ 0x252721232D2F292B353731333D3F393B<127:0> : /*8*/ 0x050701030D0F090B151711131D1F191B<127:0> : /*7*/ 0xFEFCFAF8F6F4F2F0EEECEAE8E6E4E2E0<127:0> : /*6*/ 0xDEDCDAD8D6D4D2D0CECCCAC8C6C4C2C0<127:0> : /*5*/ 0xBEBCBAB8B6B4B2B0AEACAAA8A6A4A2A0<127:0> : /*4*/ 0x9E9C9A98969492908E8C8A8886848280<127:0> : /*3*/ 0x7E7C7A78767472706E6C6A6866646260<127:0> : /*2*/ 0x5E5C5A58565452504E4C4A4846444240<127:0> : /*1*/ 0x3E3C3A38363432302E2C2A2826242220<127:0> : /*0*/ 0x1E1C1A18161412100E0C0A0806040200<127:0>
```

```
); return FFmul_02<UInt(b)*8+:8>;
```

## J1.3.3.87 FFmul03

```
// FFmul03() // ========= bits(8) FFmul03(bits(8) b) constant bits(256*8) FFmul_03 = ( /* F E D C B A 9 8 7 6 5 4 3 2 1 0 */ /*F*/ 0x1A191C1F16151013020104070E0D080B<127:0> : /*E*/ 0x2A292C2F26252023323134373E3D383B<127:0> : /*D*/ 0x7A797C7F76757073626164676E6D686B<127:0> : /*C*/ 0x4A494C4F46454043525154575E5D585B<127:0> : /*B*/ 0xDAD9DCDFD6D5D0D3C2C1C4C7CECDC8CB<127:0> : /*A*/ 0xEAE9ECEFE6E5E0E3F2F1F4F7FEFDF8FB<127:0> : /*9*/ 0xBAB9BCBFB6B5B0B3A2A1A4A7AEADA8AB<127:0> : /*8*/ 0x8A898C8F86858083929194979E9D989B<127:0> : /*7*/ 0x818287848D8E8B88999A9F9C95969390<127:0> : /*6*/ 0xB1B2B7B4BDBEBBB8A9AAAFACA5A6A3A0<127:0> : /*5*/ 0xE1E2E7E4EDEEEBE8F9FAFFFCF5F6F3F0<127:0> : /*4*/ 0xD1D2D7D4DDDEDBD8C9CACFCCC5C6C3C0<127:0> : /*3*/ 0x414247444D4E4B48595A5F5C55565350<127:0> : /*2*/ 0x717277747D7E7B78696A6F6C65666360<127:0> : /*1*/ 0x212227242D2E2B28393A3F3C35363330<127:0> : /*0*/ 0x111217141D1E1B18090A0F0C05060300<127:0> ); return FFmul_03<UInt(b)*8+:8>;
```

## J1.3.3.88 FFmul09

```
// FFmul09() // ========= bits(8) FFmul09(bits(8) b) constant bits(256*8) FFmul_09 = ( /* F E D C B A 9 8 7 6 5 4 3 2 1 0 */ /*F*/ 0x464F545D626B70790E071C152A233831<127:0> : /*E*/ 0xD6DFC4CDF2FBE0E99E978C85BAB3A8A1<127:0> : /*D*/ 0x7D746F6659504B42353C272E1118030A<127:0> : /*C*/ 0xEDE4FFF6C9C0DBD2A5ACB7BE8188939A<127:0> : /*B*/ 0x3039222B141D060F78716A635C554E47<127:0> : /*A*/ 0xA0A9B2BB848D969FE8E1FAF3CCC5DED7<127:0> : /*9*/ 0x0B0219102F263D34434A5158676E757C<127:0> : /*8*/ 0x9B928980BFB6ADA4D3DAC1C8F7FEE5EC<127:0> : /*7*/ 0xAAA3B8B18E879C95E2EBF0F9C6CFD4DD<127:0> : /*6*/ 0x3A3328211E170C05727B6069565F444D<127:0> : /*5*/ 0x9198838AB5BCA7AED9D0CBC2FDF4EFE6<127:0> : /*4*/ 0x0108131A252C373E49405B526D647F76<127:0> : /*3*/ 0xDCD5CEC7F8F1EAE3949D868FB0B9A2AB<127:0> : /*2*/ 0x4C455E5768617A73040D161F2029323B<127:0> : /*1*/ 0xE7EEF5FCC3CAD1D8AFA6BDB48B829990<127:0> : /*0*/ 0x777E656C535A41483F362D241B120900<127:0> ); return FFmul_09<UInt(b)*8+:8>;
```

## J1.3.3.89 FFmul0B

```
// FFmul0B() // ========= bits(8) FFmul0B(bits(8) b) constant bits(256*8) FFmul_0B = ( /* F E D C B A 9 8 7 6 5 4 3 2 1 0 */ /*F*/ 0xA3A8B5BE8F849992FBF0EDE6D7DCC1CA<127:0> : /*E*/ 0x1318050E3F3429224B405D56676C717A<127:0> : /*D*/ 0xD8D3CEC5F4FFE2E9808B969DACA7BAB1<127:0> : /*C*/ 0x68637E75444F5259303B262D1C170A01<127:0> : /*B*/ 0x555E434879726F640D061B10212A373C<127:0> : /*A*/ 0xE5EEF3F8C9C2DFD4BDB6ABA0919A878C<127:0> : /*9*/ 0x2E2538330209141F767D606B5A514C47<127:0> : /*8*/ 0x9E958883B2B9A4AFC6CDD0DBEAE1FCF7<127:0> : /*7*/ 0x545F424978736E650C071A11202B363D<127:0> : /*6*/ 0xE4EFF2F9C8C3DED5BCB7AAA1909B868D<127:0> : /*5*/ 0x2F2439320308151E777C616A5B504D46<127:0> : /*4*/ 0x9F948982B3B8A5AEC7CCD1DAEBE0FDF6<127:0> : /*3*/ 0xA2A9B4BF8E859893FAF1ECE7D6DDC0CB<127:0> : /*2*/ 0x1219040F3E3528234A415C57666D707B<127:0> : /*1*/ 0xD9D2CFC4F5FEE3E8818A979CADA6BBB0<127:0> : /*0*/ 0x69627F74454E5358313A272C1D160B00<127:0> ); return FFmul_0B<UInt(b)*8+:8>;
```

```
J1.3.3.90 FFmul0D // FFmul0D() // ========= bits(8) FFmul0D(bits(8) b) constant bits(256*8) FFmul_0D = ( /* F E D C B A 9 8 7 6 5 4 3 2 1 0 */ /*F*/ 0x979A8D80A3AEB9B4FFF2E5E8CBC6D1DC<127:0> : /*E*/ 0x474A5D50737E69642F2235381B16010C<127:0> : /*D*/ 0x2C21363B1815020F44495E53707D6A67<127:0> : /*C*/ 0xFCF1E6EBC8C5D2DF94998E83A0ADBAB7<127:0> : /*B*/ 0xFAF7E0EDCEC3D4D9929F8885A6ABBCB1<127:0> : /*A*/ 0x2A27303D1E130409424F5855767B6C61<127:0> : /*9*/ 0x414C5B5675786F622924333E1D10070A<127:0> : /*8*/ 0x919C8B86A5A8BFB2F9F4E3EECDC0D7DA<127:0> : /*7*/ 0x4D40575A7974636E25283F32111C0B06<127:0> : /*6*/ 0x9D90878AA9A4B3BEF5F8EFE2C1CCDBD6<127:0> : /*5*/ 0xF6FBECE1C2CFD8D59E938489AAA7B0BD<127:0> : /*4*/ 0x262B3C31121F08054E4354597A77606D<127:0> : /*3*/ 0x202D3A3714190E034845525F7C71666B<127:0> : /*2*/ 0xF0FDEAE7C4C9DED39895828FACA1B6BB<127:0> : /*1*/ 0x9B96818CAFA2B5B8F3FEE9E4C7CADDD0<127:0> : /*0*/ 0x4B46515C7F726568232E3934171A0D00<127:0> ); return FFmul_0D<UInt(b)*8+:8>; J1.3.3.91 FFmul0E // FFmul0E() // ========= bits(8) FFmul0E(bits(8) b) constant bits(256*8) FFmul_0E = ( /* F E D C B A 9 8 7 6 5 4 3 2 1 0 */ /*F*/ 0x8D83919FB5BBA9A7FDF3E1EFC5CBD9D7<127:0> :
```

```
/*E*/ 0x6D63717F555B49471D13010F252B3937<127:0> : /*D*/ 0x56584A446E60727C26283A341E10020C<127:0> : /*C*/ 0xB6B8AAA48E80929CC6C8DAD4FEF0E2EC<127:0> : /*B*/ 0x202E3C321816040A505E4C426866747A<127:0> : /*A*/ 0xC0CEDCD2F8F6E4EAB0BEACA28886949A<127:0> : /*9*/ 0xFBF5E7E9C3CDDFD18B859799B3BDAFA1<127:0> : /*8*/ 0x1B150709232D3F316B657779535D4F41<127:0> : /*7*/ 0xCCC2D0DEF4FAE8E6BCB2A0AE848A9896<127:0> : /*6*/ 0x2C22303E141A08065C52404E646A7876<127:0> : /*5*/ 0x17190B052F21333D67697B755F51434D<127:0> : /*4*/ 0xF7F9EBE5CFC1D3DD87899B95BFB1A3AD<127:0> : /*3*/ 0x616F7D735957454B111F0D032927353B<127:0> : /*2*/ 0x818F9D93B9B7A5ABF1FFEDE3C9C7D5DB<127:0> : /*1*/ 0xBAB4A6A8828C9E90CAC4D6D8F2FCEEE0<127:0> : /*0*/ 0x5A544648626C7E702A243638121C0E00<127:0> ); return FFmul_0E<UInt(b)*8+:8>; J1.3.3.92 SHA256hash // SHA256hash() // ============ bits(128) SHA256hash(bits (128) x_in, bits(128) y_in, bits(128) w, boolean part1) bits(32) chs, maj, t; bits(128) x = x_in; bits(128) y = y_in; for e = 0 to 3 chs = SHAchoose(y<31:0>, y<63:32>, y<95:64>); maj = SHAmajority(x<31:0>, x<63:32>, x<95:64>); t = y<127:96> + SHAhashSIGMA1(y<31:0>) + chs + Elem[w, e, 32]; x<127:96> = t + x<127:96>; y<127:96> = t + SHAhashSIGMA0(x<31:0>) + maj; constant bits(256) yx = ROL(y : x, 32); (y, x) = (yx<128+:128>, yx<0+:128>); return (if part1 then x else y); J1.3.3.93 SHAchoose // SHAchoose() // =========== bits(32) SHAchoose(bits(32) x, bits(32) y, bits(32) z) return (((y EOR z) AND x) EOR z); J1.3.3.94 SHAhashSIGMA0 // SHAhashSIGMA0() // =============== bits(32) SHAhashSIGMA0(bits(32) x) return ROR(x, 2) EOR ROR(x, 13) EOR ROR(x, 22);
```

## J1.3.3.95 SHAhashSIGMA1

```
// SHAhashSIGMA1() // =============== bits(32) SHAhashSIGMA1(bits(32) x) return ROR(x, 6) EOR ROR(x, 11) EOR
```

```
ROR(x, 25);
```

## J1.3.3.96 SHAmajority

```
// SHAmajority() // ============= bits(N) SHAmajority(bits(N) x, bits(N) y, bits(N) assert N IN {32, 64}; return ((x AND y) OR ((x OR y) AND z));
```

## J1.3.3.97 SHAparity

```
// SHAparity() // =========== bits(32) SHAparity(bits(32) x, bits(32) y, bits(32) return (x EOR y EOR z);
```

## J1.3.3.98 Sbox

```
// Sbox() // ====== // Used in SM4E crypto instruction bits(8) Sbox(bits(8) sboxin) bits(8) sboxout; constant bits(2048) sboxstring = ( /* F E D C B A 9 8 7 6 5 4 3 2 1 0 */ /*F*/ 0xd690e9fecce13db716b614c228fb2c05<127:0> : /*E*/ 0x2b679a762abe04c3aa44132649860699<127:0> : /*D*/ 0x9c4250f491ef987a33540b43edcfac62<127:0> : /*C*/ 0xe4b31ca9c908e89580df94fa758f3fa6<127:0> : /*B*/ 0x4707a7fcf37317ba83593c19e6854fa8<127:0> : /*A*/ 0x686b81b27164da8bf8eb0f4b70569d35<127:0> : /*9*/ 0x1e240e5e6358d1a225227c3b01217887<127:0> : /*8*/ 0xd40046579fd327524c3602e7a0c4c89e<127:0> : /*7*/ 0xeabf8ad240c738b5a3f7f2cef96115a1<127:0> : /*6*/ 0xe0ae5da49b341a55ad933230f58cb1e3<127:0> : /*5*/ 0x1df6e22e8266ca60c02923ab0d534e6f<127:0> : /*4*/ 0xd5db3745defd8e2f03ff6a726d6c5b51<127:0> : /*3*/ 0x8d1baf92bbddbc7f11d95c411f105ad8<127:0> : /*2*/ 0x0ac13188a5cd7bbd2d74d012b8e5b4b0<127:0> : /*1*/ 0x8969974a0c96777e65b9f109c56ec684<127:0> : /*0*/ 0x18f07dec3adc4d2079ee5f3ed7cb3948<127:0> ); constant integer sboxindex = 255 -UInt(sboxin); sboxout = Elem[sboxstring, sboxindex, 8]; return sboxout;
```

```
z)
```

```
z)
```

## J1.3.3.99 DecodeType

```
// DecodeType // ========== enumeration DecodeType Decode_UNDEF, Decode_NOP, Decode_OK };
```

```
{
```

## J1.3.3.100 EndOfDecode // EndOfDecode() // ============= // This function is invoked to end the Decode phase and performs Branch target Checks // before taking any UNDEFINED exceptions, NOPs, or continuing to execute. EndOfDecode(DecodeType reason) if IsFeatureImplemented(FEAT\_BTI) &amp;&amp; !UsingAArch32() then BranchTargetCheck(); case reason of when Decode\_NOP ExecuteAsNOP(); when Decode\_UNDEF Undefined(); when Decode\_OK // Continue to execute. return; J1.3.3.101 ClearExclusiveByAddress // ClearExclusiveByAddress() // ========================= // Clear the global Exclusives monitors for all PEs EXCEPT processorid if they // record any part of the physical address region of size bytes starting at paddress. // It is IMPLEMENTATION DEFINED whether the global Exclusives monitor for processorid // is also cleared if it records any part of the address region. ClearExclusiveByAddress(FullAddress paddress, integer processorid, integer size); J1.3.3.102 ClearExclusiveLocal // ClearExclusiveLocal() // ===================== // Clear the local Exclusives monitor for the specified processorid. ClearExclusiveLocal(integer processorid); J1.3.3.103 ExclusiveMonitorsStatus

```
different
```

```
// ExclusiveMonitorsStatus() // ========================= // Returns '0' to indicate success if the last memory write by this PE was to // the same physical address region endorsed by ExclusiveMonitorsPass(). // Returns '1' to indicate failure if address translation resulted in a // physical address. bit ExclusiveMonitorsStatus();
```

## J1.3.3.104 IsExclusiveGlobal

```
// IsExclusiveGlobal() // =================== // Return TRUE if the global Exclusives monitor for processorid includes all of // the physical address region of size bytes starting at paddress. boolean IsExclusiveGlobal(FullAddress paddress, integer processorid, integer size);
```

## J1.3.3.105 IsExclusiveLocal

```
// IsExclusiveLocal() // ================== // Return TRUE if the local Exclusives monitor for processorid includes all of // the physical address region of size bytes starting at paddress. boolean IsExclusiveLocal(FullAddress paddress, integer processorid, integer size);
```

## J1.3.3.106 MarkExclusiveGlobal

```
// MarkExclusiveGlobal() // ===================== // Record the physical address region of size bytes starting at paddress in // the global Exclusives monitor for processorid. MarkExclusiveGlobal(FullAddress paddress, integer processorid, integer
```

## J1.3.3.107 MarkExclusiveLocal

```
// MarkExclusiveLocal() // ==================== // Record the physical address region of size bytes starting at paddress in // the local Exclusives monitor for processorid. MarkExclusiveLocal(FullAddress paddress, integer processorid, integer size);
```

## J1.3.3.108 ProcessorID

```
// ProcessorID() // ============= // Return the ID of the currently executing integer ProcessorID();
```

## J1.3.3.109 HaveSoftwareLock

```
// HaveSoftwareLock() // ================== // Returns TRUE if Software Lock is implemented. boolean HaveSoftwareLock(Component component) if IsFeatureImplemented(FEAT_Debugv8p4) then return FALSE; if IsFeatureImplemented(FEAT_DoPD) && component != Component_CTI then return FALSE; case component of when Component_ETE return boolean IMPLEMENTATION_DEFINED "ETE has Software Lock";
```

```
PE.
```

```
size);
```

```
when Component_Debug return boolean IMPLEMENTATION_DEFINED "Debug has Software Lock"; when Component_PMU return boolean IMPLEMENTATION_DEFINED "PMU has Software Lock"; when Component_CTI return boolean IMPLEMENTATION_DEFINED "CTI has Software Lock"; otherwise Unreachable();
```

## J1.3.3.110 HaveTraceExt

```
// HaveTraceExt() // ============== // Returns TRUE if Trace functionality as described by the Trace Architecture // is implemented. boolean HaveTraceExt() return IsFeatureImplemented(FEAT_ETE) || IsFeatureImplemented(FEAT_ETMv4);
```

## J1.3.3.111 InsertIESBBeforeException

```
// InsertIESBBeforeException() // =========================== // Returns an implementation defined choice whether to insert an implicit error synchronization // barrier before exception. // If SCTLR_ELx.IESB is 1 when an exception is generated to ELx, any pending Unrecoverable // SError interrupt must be taken before executing any instructions in the exception handler. // However, this can be before the branch to the exception handler is made. boolean InsertIESBBeforeException(bits(2) el) return (IsFeatureImplemented(FEAT_IESB) && boolean IMPLEMENTATION_DEFINED "Has Implicit Error Synchronization Barrier before Exception");
```

## J1.3.3.112 ActionRequired

```
// ActionRequired() // ================ // Return an implementation specific value: // returns TRUE if action is required, FALSE otherwise. boolean ActionRequired();
```

## J1.3.3.113 ClearPendingDelegatedSError

```
// ClearPendingDelegatedSError() // ============================= // Clear a pending delegated SError interrupt. ClearPendingDelegatedSError() assert IsFeatureImplemented(FEAT_E3DSE); SCR_EL3.DSE = '0';
```

## J1.3.3.114 ClearPendingPhysicalSError

```
// ClearPendingPhysicalSError() // ============================ // Clear a pending physical SError interrupt. ClearPendingPhysicalSError();
```

## J1.3.3.115 ClearPendingVirtualSError

```
// ClearPendingVirtualSError() // =========================== // Clear a pending virtual SError interrupt. ClearPendingVirtualSError() if ELUsingAArch32(EL2) then HCR.VA = '0'; else HCR_EL2.VSE = '0';
```

## J1.3.3.116 ErrorIsContained

```
// ErrorIsContained() // ================== // Return an implementation specific value: // TRUE if Error is contained by the PE, FALSE otherwise. boolean ErrorIsContained();
```

## J1.3.3.117 ErrorIsSynchronized

```
// ErrorIsSynchronized() // ===================== // Return an implementation specific value: // returns TRUE if Error is synchronized by any synchronization event // FALSE otherwise. boolean ErrorIsSynchronized();
```

## J1.3.3.118 ExtAbortToAArch64

```
// ExtAbortToAArch64() // =================== // Returns TRUE if synchronous exception is being taken to an Exception level using AArch64. boolean ExtAbortToAArch64(FaultRecord fault) assert IsExternalSyncAbort(fault.statuscode); return !ELUsingAArch32(SyncExternalAbortTarget(fault));
```

## J1.3.3.119 ExternalAbort

```
// ExternalAbort() // =============== ExternalAbort(FaultRecord fault) if IsExternalSyncAbort(fault) then if UsingAArch32() then AArch32.Abort(fault); else AArch64.Abort(fault); else PendSErrorInterrupt(fault);
```

## J1.3.3.120 ExternalFault

```
// ExternalFault() // =============== // Return a fault recording indicating a fault for a Synchronous/Asynchronous External abort. FaultRecord ExternalFault(PhysMemRetStatus memretstatus, boolean iswrite, AddressDescriptor memaddrdesc, integer size, AccessDescriptor accdesc) assert (memretstatus.statuscode IN {Fault_SyncExternal, Fault_AsyncExternal} || (!IsFeatureImplemented(FEAT_RAS) && memretstatus.statuscode IN {Fault_SyncParity, Fault_AsyncParity})); fault = NoFault(accdesc, memaddrdesc.vaddress); fault.statuscode = memretstatus.statuscode; fault.write = iswrite; fault.extflag = memretstatus.extflag; // It is implementation specific whether External aborts signaled // in-band synchronously are taken synchronously or asynchronously if (IsExternalSyncAbort(fault) && ((IsFeatureImplemented(FEAT_RASv2) && ExtAbortToAArch64(fault) && PEErrorState(fault) IN {ErrorState_UC, ErrorState_UEU}) || !IsExternalAbortTakenSynchronously(memretstatus, iswrite, memaddrdesc, size, accdesc))) then if fault.statuscode == Fault_SyncParity then fault.statuscode = Fault_AsyncParity; else fault.statuscode = Fault_AsyncExternal; if IsFeatureImplemented(FEAT_RAS) then fault.merrorstate = memretstatus.merrorstate; fault.paddress = memaddrdesc.paddress; return fault;
```

## J1.3.3.121 FaultIsCorrected // FaultIsCorrected() // ================== // Return an implementation specific value: // TRUE if fault is corrected by the PE, FALSE otherwise. boolean FaultIsCorrected(); J1.3.3.122 GetPendingPhysicalSError // GetPendingPhysicalSError() // ========================== // Returns the FaultRecord containing details of pending Physical SError // interrupt. FaultRecord GetPendingPhysicalSError(); J1.3.3.123 HandleExternalAbort // HandleExternalAbort() // ===================== // Takes a Synchronous/Asynchronous abort based on fault. HandleExternalAbort(PhysMemRetStatus memretstatus, boolean iswrite, AddressDescriptor memaddrdesc, integer size, AccessDescriptor accdesc)

```
assert (memretstatus.statuscode IN {Fault_SyncExternal, Fault_AsyncExternal} || (!IsFeatureImplemented(FEAT_RAS) && memretstatus.statuscode IN {Fault_SyncParity, Fault_AsyncParity})); constant FaultRecord fault = ExternalFault(memretstatus, iswrite, memaddrdesc, size, accdesc); ExternalAbort(fault);
```

## J1.3.3.124 HandleExternalReadAbort

```
// HandleExternalReadAbort() // ========================= // Wrapper function for HandleExternalAbort function in case of an External // Abort on memory read. HandleExternalReadAbort(PhysMemRetStatus memstatus, AddressDescriptor memaddrdesc, integer size, AccessDescriptor accdesc) iswrite = FALSE; HandleExternalAbort(memstatus, iswrite, memaddrdesc, size, accdesc);
```

## J1.3.3.125 HandleExternalTTWAbort

```
// HandleExternalTTWAbort() // ======================== // Take Asynchronous abort or update FaultRecord for Translation Table Walk // based on PhysMemRetStatus. FaultRecord HandleExternalTTWAbort(PhysMemRetStatus memretstatus, boolean iswrite, AddressDescriptor memaddrdesc, AccessDescriptor accdesc, integer size, FaultRecord input_fault) output_fault = input_fault; output_fault.extflag = memretstatus.extflag; output_fault.statuscode = memretstatus.statuscode; if (IsExternalSyncAbort(output_fault) && ((IsFeatureImplemented(FEAT_RASv2) && ExtAbortToAArch64(output_fault) && PEErrorState(output_fault) IN {ErrorState_UC, ErrorState_UEU}) || !IsExternalAbortTakenSynchronously(memretstatus, iswrite, memaddrdesc, size, accdesc))) then if output_fault.statuscode == Fault_SyncParity then output_fault.statuscode = Fault_AsyncParity; else output_fault.statuscode = Fault_AsyncExternal; // If a synchronous fault is on a translation table walk, then update the fault type. if IsExternalSyncAbort(output_fault) then if output_fault.statuscode == Fault_SyncParity then output_fault.statuscode = Fault_SyncParityOnWalk; else output_fault.statuscode = Fault_SyncExternalOnWalk; if IsFeatureImplemented(FEAT_RAS) then output_fault.merrorstate = memretstatus.merrorstate; if !IsExternalSyncAbort(output_fault) then PendSErrorInterrupt(output_fault); output_fault.statuscode = Fault_None; output_fault.paddress = memaddrdesc.paddress; return output_fault;
```

## J1.3.3.126 HandleExternalWriteAbort

```
memaddrdesc,
```

```
// HandleExternalWriteAbort() // ========================== // Wrapper function for HandleExternalAbort function in case of an External // Abort on memory write. HandleExternalWriteAbort(PhysMemRetStatus memstatus, AddressDescriptor integer size, AccessDescriptor accdesc) iswrite = TRUE; HandleExternalAbort(memstatus, iswrite, memaddrdesc, size, accdesc);
```

## J1.3.3.127 IsDelegatedSErrorPending

```
// IsDelegatedSErrorPending() // ========================== // Return TRUE if a delegated SError interrupt is pending. boolean IsDelegatedSErrorPending() return SCR_EL3.DSE == '1';
```

## J1.3.3.128 IsExternalAbortTakenSynchronously

```
// IsExternalAbortTakenSynchronously() // =================================== // Return an implementation specific value: // TRUE if the fault returned for the access can be taken synchronously, // FALSE otherwise. // // This might vary between accesses, for example depending on the error type // or memory type being accessed. // External aborts on data accesses and translation table walks on data accesses // can be either synchronous or asynchronous. // // When FEAT_DoubleFault is not implemented, External aborts on instruction // fetches and translation table walks on instruction fetches can be either // synchronous or asynchronous. // When FEAT_DoubleFault is implemented, all External abort exceptions on // instruction fetches and translation table walks on instruction fetches // must be synchronous. boolean IsExternalAbortTakenSynchronously(PhysMemRetStatus memstatus, boolean iswrite, AddressDescriptor desc, integer size, AccessDescriptor accdesc);
```

## J1.3.3.129 IsPhysicalSErrorPending

```
// IsPhysicalSErrorPending() // ========================= // Returns TRUE if a physical SError interrupt is
```

```
pending. boolean IsPhysicalSErrorPending();
```

## J1.3.3.130 IsSErrorEdgeTriggered

```
// IsSErrorEdgeTriggered() // ======================= // Returns TRUE if the physical SError interrupt is edge-triggered // and FALSE otherwise.
```

```
boolean IsSErrorEdgeTriggered() if IsFeatureImplemented(FEAT_DoubleFault) then return TRUE; else return boolean IMPLEMENTATION_DEFINED "Edge-triggered SError";
```

## J1.3.3.131 IsSynchronizablePhysicalSErrorPending

```
// IsSynchronizablePhysicalSErrorPending() // ======================================= // Returns TRUE if a synchronizable physical SError interrupt is pending. boolean IsSynchronizablePhysicalSErrorPending();
```

## J1.3.3.132 IsVirtualSErrorPending

```
// IsVirtualSErrorPending() // ======================== // Return TRUE if a virtual SError interrupt is pending. boolean IsVirtualSErrorPending() if ELUsingAArch32(EL2) then return HCR.VA == '1'; else return HCR_EL2.VSE == '1';
```

## J1.3.3.133 PEErrorState

```
// PEErrorState() // ============== // Returns the error state of the PE on taking an error exception: // The PE error state reported to software through the exception syndrome also // depends on how the exception is taken, and so might differ from the value // returned from this function. ErrorState PEErrorState(FaultRecord fault) assert !FaultIsCorrected(); if (!ErrorIsContained() || (!ErrorIsSynchronized() && !StateIsRecoverable()) || ReportErrorAsUC()) then return ErrorState_UC; if !StateIsRecoverable() || ReportErrorAsUEU() then return ErrorState_UEU; if ActionRequired() || ReportErrorAsUER() then return ErrorState_UER; return ErrorState_UEO;
```

## J1.3.3.134 PendSErrorInterrupt

```
// PendSErrorInterrupt() // ===================== // Pend the SError Interrupt. PendSErrorInterrupt(FaultRecord fault);
```

## J1.3.3.135 ReportErrorAsIMPDEF

```
// ReportErrorAsIMPDEF() // ===================== // Return an implementation specific value: // returns TRUE if Error is IMPDEF, FALSE otherwise. boolean ReportErrorAsIMPDEF();
```

## J1.3.3.136 ReportErrorAsUC

```
// ReportErrorAsUC() // ================= // Return an implementation specific value: // returns TRUE if Error is Uncontainable, FALSE otherwise. boolean ReportErrorAsUC();
```

## J1.3.3.137 ReportErrorAsUER

```
// ReportErrorAsUER() // ================== // Return an implementation specific value: // returns TRUE if Error is Recoverable, FALSE otherwise. boolean ReportErrorAsUER();
```

## J1.3.3.138 ReportErrorAsUEU

```
// ReportErrorAsUEU() // ================== // Return an implementation specific value: // returns TRUE if Error is Unrecoverable, FALSE otherwise. boolean ReportErrorAsUEU();
```

## J1.3.3.139 ReportErrorAsUncategorized

```
// ReportErrorAsUncategorized() // =========================== // Return an implementation specific value: // returns TRUE if Error is uncategorized, FALSE otherwise.
```

boolean ReportErrorAsUncategorized();

## J1.3.3.140 StateIsRecoverable

```
// StateIsRecoverable() // ===================== // Return an implementation specific value: // returns TRUE is PE State is unrecoverable else FALSE. boolean StateIsRecoverable();
```

## J1.3.3.141 BFAdd

```
// BFAdd() // ======= // Non-widening BFloat16 addition used by SVE2 instructions. bits(N) BFAdd(bits(N) op1, bits(N) op2, FPCR_Type fpcr) constant boolean fpexc = TRUE; return BFAdd(op1, op2, fpcr, fpexc); // BFAdd() // ======= // Non-widening BFloat16 addition following computational behaviors // corresponding to instructions that read and write BFloat16 values. // Calculates op1 + op2. // The 'fpcr' argument supplies the FPCR control bits. bits(N) BFAdd(bits(N) op1, bits(N) op2, FPCR_Type fpcr, boolean fpexc) assert N == 16; constant FPRounding rounding = FPRoundingMode(fpcr); boolean done; bits(2*N) result; constant bits(2*N) op1_s = op1 : Zeros(N); constant bits(2*N) op2_s = op2 : Zeros(N); (type1,sign1,value1) = FPUnpack(op1_s, fpcr, fpexc); (type2,sign2,value2) = FPUnpack(op2_s, fpcr, fpexc); (done,result) = FPProcessNaNs(type1, type2, op1_s, op2_s, fpcr, fpexc); if !done then inf1 = (type1 == FPType_Infinity); inf2 = (type2 == FPType_Infinity); zero1 = (type1 == FPType_Zero); zero2 = (type2 == FPType_Zero); if inf1 && inf2 && sign1 == NOT(sign2) then result = FPDefaultNaN(fpcr, 2*N); if fpexc then FPProcessException(FPExc_InvalidOp, fpcr); elsif (inf1 && sign1 == '0') || (inf2 && sign2 == '0') then result = FPInfinity('0', 2*N); elsif (inf1 && sign1 == '1') || (inf2 && sign2 == '1') then result = FPInfinity('1', 2*N); elsif zero1 && zero2 && sign1 == sign2 then result = FPZero(sign1, 2*N); else result_value = value1 + value2; if result_value == 0.0 then // Sign of exact zero result depends on rounding mode result_sign = if rounding == FPRounding_NEGINF then '1' else '0'; result = FPZero(result_sign, 2*N); else result = FPRoundBF(result_value, fpcr, rounding, fpexc, 2*N); if fpexc then FPProcessDenorms(type1, type2, 2*N, fpcr); return result<2*N-1:N>;
```

## J1.3.3.142 BFAdd\_ZA

```
// BFAdd_ZA() // ========== // Non-widening BFloat16 addition used by SME2 ZA-targeting instructions. bits(16) BFAdd_ZA(bits(16) op1, bits(16) op2, FPCR_Type fpcr_in)
```

```
constant boolean fpexc = FALSE; FPCR_Type fpcr = fpcr_in; fpcr.DN = '1'; // Generate default NaN values return BFAdd(op1, op2, fpcr, fpexc);
```

## J1.3.3.143 BFDotAdd

```
// BFDotAdd() // ========== // BFloat16 2-way dot-product and add to single-precision // result = addend + op1_a*op2_a + op1_b*op2_b bits(32) BFDotAdd(bits(32) addend, bits(16) op1_a, bits(16) op1_b, bits(16) op2_a, bits(16) op2_b, FPCR_Type fpcr_in) FPCR_Type fpcr = fpcr_in; bits(32) prod; bits(32) result; if !IsFeatureImplemented(FEAT_EBF16) || fpcr.EBF == '0' then // Standard BFloat16 behaviors prod = FPAdd_BF16(BFMulH(op1_a, op2_a, fpcr), BFMulH(op1_b, op2_b, fpcr), fpcr); result = FPAdd_BF16(addend, prod, fpcr); else // Extended BFloat16 behaviors constant boolean isbfloat16 = TRUE; constant boolean fpexc = FALSE; // Do not generate floating-point exceptions fpcr.DN = '1'; // Generate default NaN values prod = FPDot(op1_a, op1_b, op2_a, op2_b, fpcr, isbfloat16, fpexc); result = FPAdd(addend, prod, fpcr, fpexc); return result;
```

## J1.3.3.144 BFInfinity

```
// BFInfinity() // ============ bits(N) BFInfinity(bit sign, integer N) assert N == 16; constant integer E = 8; constant integer F = N - (E + 1); return sign : Ones(E) : Zeros(F);
```

## J1.3.3.145 BFMatMulAddH

```
// BFMatMulAddH() // ============== // BFloat16 matrix multiply and add to single-precision matrix // result[2, 2] = addend[2, 2] + (op1[2, 4] * op2[4, 2]) bits(128) BFMatMulAddH(bits(128) addend, bits(128) op1, bits(128) op2, FPCR_Type fpcr) bits(128) result; bits(32) sum; for i = 0 to 1 for j = 0 to 1 sum = Elem[addend, 2*i + j, 32]; for k = 0 to 1 constant bits(16) elt1_a = Elem[op1, 4*i + 2*k + 0, 16]; constant bits(16) elt1_b = Elem[op1, 4*i + 2*k + 1, 16]; constant bits(16) elt2_a = Elem[op2, 4*j + 2*k + 0, 16]; constant bits(16) elt2_b = Elem[op2, 4*j + 2*k + 1, 16];
```

```
sum = BFDotAdd(sum, elt1_a, elt1_b, elt2_a, elt2_b, fpcr); Elem[result, 2*i + j, 32] = sum;
```

return result;

## J1.3.3.146 BFMax

```
// BFMax() // ======= // BFloat16 maximum. bits(N) BFMax(bits(N) op1, bits(N) op2, FPCR_Type fpcr) constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1'; constant boolean fpexc = TRUE; return BFMax(op1, op2, fpcr, altfp, fpexc); // BFMax() // ======= // BFloat16 maximum. bits(N) BFMax(bits(N) op1, bits(N) op2, FPCR_Type fpcr, boolean altfp) constant boolean fpexc = TRUE; return BFMax(op1, op2, fpcr, altfp, fpexc); // BFMax() // ======= // BFloat16 maximum following computational behaviors // corresponding to instructions that read and write BFloat16 values. // Compare op1 and op2 and return the larger value after rounding. // The 'fpcr' argument supplies the FPCR control bits and 'altfp' determines // if the function should use alternative floating-point behavior. bits(N) BFMax(bits(N) op1, bits(N) op2, FPCR_Type fpcr_in, boolean altfp, boolean fpexc) assert N == 16; FPCR_Type fpcr = fpcr_in; constant FPRounding rounding = FPRoundingMode(fpcr); boolean done; bits(2*N) result; constant bits(2*N) op1_s = op1 : Zeros(N); constant bits(2*N) op2_s = op2 : Zeros(N); (type1,sign1,value1) = FPUnpack(op1_s, fpcr, fpexc); (type2,sign2,value2) = FPUnpack(op2_s, fpcr, fpexc); if altfp && type1 == FPType_Zero && type2 == FPType_Zero && sign1 != sign2 then // Alternate handling of zeros with differing sign return BFZero(sign2, N); elsif altfp && (type1 IN {FPType_SNaN, FPType_QNaN} || type2 IN {FPType_SNaN, FPType_QNaN}) then // Alternate handling of NaN inputs if fpexc then FPProcessException(FPExc_InvalidOp, fpcr); return (if type2 == FPType_Zero then BFZero(sign2, N) else op2); (done,result) = FPProcessNaNs(type1, type2, op1_s, op2_s, fpcr, fpexc); if !done then FPType fptype; bit sign; real value; if value1 > value2 then (fptype,sign,value) = (type1,sign1,value1); else (fptype,sign,value) = (type2,sign2,value2); if fptype == FPType_Infinity then result = FPInfinity(sign, 2*N); elsif fptype == FPType_Zero then sign = sign1 AND sign2; // Use most positive sign
```

```
result = FPZero(sign, 2*N); else if altfp then // Denormal output is not flushed fpcr.FZ = '0'; result = FPRoundBF(value, fpcr, rounding, fpexc, 2*N); if fpexc then FPProcessDenorms(type1, type2, 2*N, fpcr); result<2*N-1:N>;
```

```
// BFMin() // ======= // BFloat16 minimum. bits(N) BFMin(bits(N) op1, bits(N) op2, FPCR_Type fpcr) constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == constant boolean fpexc = TRUE; return BFMin(op1, op2, fpcr, altfp, fpexc);
```

## to zero return J1.3.3.147 BFMaxNum // BFMaxNum() // ========== bits(N) BFMaxNum(bits(N) op1, bits(N) op2, FPCR\_Type fpcr) constant boolean fpexc = TRUE; return BFMaxNum(op1, op2, fpcr, fpexc); // BFMaxNum() // ========== // BFloat16 maximum number following computational behaviors corresponding // to instructions that read and write BFloat16 values. // Compare op1 and op2 and return the larger number operand after rounding. // The 'fpcr' argument supplies the FPCR control bits. bits(N) BFMaxNum(bits(N) op1\_in, bits(N) op2\_in, FPCR\_Type fpcr, boolean fpexc) assert N == 16; constant boolean isbfloat16 = TRUE; bits(N) op1 = op1\_in; bits(N) op2 = op2\_in; constant boolean altfp = IsFeatureImplemented(FEAT\_AFP) &amp;&amp; !UsingAArch32() &amp;&amp; fpcr.AH == '1'; bits(N) result; (type1,-,-) = FPUnpackBase(op1, fpcr, fpexc, isbfloat16); (type2,-,-) = FPUnpackBase(op2, fpcr, fpexc, isbfloat16); constant boolean type1\_nan = type1 IN {FPType\_QNaN, FPType\_SNaN}; constant boolean type2\_nan = type2 IN {FPType\_QNaN, FPType\_SNaN}; if !(altfp &amp;&amp; type1\_nan &amp;&amp; type2\_nan) then // Treat a single quiet-NaN as -Infinity. if type1 == FPType\_QNaN &amp;&amp; type2 != FPType\_QNaN then op1 = BFInfinity('1', N); elsif type1 != FPType\_QNaN &amp;&amp; type2 == FPType\_QNaN then op2 = BFInfinity('1', N); constant boolean altfmaxfmin = FALSE; // Do not use alternate NaN handling result = BFMax(op1, op2, fpcr, altfmaxfmin, fpexc); return result; J1.3.3.148 BFMin '1';

```
// BFMin() // ======= // BFloat16 minimum. bits(N) BFMin(bits(N) op1, bits(N) op2, FPCR_Type fpcr, boolean altfp) constant boolean fpexc = TRUE; return BFMin(op1, op2, fpcr, altfp, fpexc); // BFMin() // ======= // BFloat16 minimum following computational behaviors // corresponding to instructions that read and write BFloat16 values. // Compare op1 and op2 and return the smaller value after rounding. // The 'fpcr' argument supplies the FPCR control bits and 'altfp' determines // if the function should use alternative floating-point behavior. bits(N) BFMin(bits(N) op1, bits(N) op2, FPCR_Type fpcr_in, boolean altfp, boolean fpexc) assert N == 16; FPCR_Type fpcr = fpcr_in; constant FPRounding rounding = FPRoundingMode(fpcr); boolean done; bits(2*N) result; constant bits(2*N) op1_s = op1 : Zeros(N); constant bits(2*N) op2_s = op2 : Zeros(N); (type1,sign1,value1) = FPUnpack(op1_s, fpcr, fpexc); (type2,sign2,value2) = FPUnpack(op2_s, fpcr, fpexc); if altfp && type1 == FPType_Zero && type2 == FPType_Zero && sign1 != sign2 then // Alternate handling of zeros with differing sign return BFZero(sign2, N); elsif altfp && (type1 IN {FPType_SNaN, FPType_QNaN} || type2 IN {FPType_SNaN, FPType_QNaN}) then // Alternate handling of NaN inputs if fpexc then FPProcessException(FPExc_InvalidOp, fpcr); return (if type2 == FPType_Zero then BFZero(sign2, N) else op2); (done,result) = FPProcessNaNs(type1, type2, op1_s, op2_s, fpcr, fpexc); if !done then FPType fptype; bit sign; real value; if value1 < value2 then (fptype,sign,value) = (type1,sign1,value1); else (fptype,sign,value) = (type2,sign2,value2); if fptype == FPType_Infinity then result = FPInfinity(sign, 2*N); elsif fptype == FPType_Zero then sign = sign1 OR sign2; // Use most negative sign result = FPZero(sign, 2*N); else if altfp then // Denormal output is not flushed to zero fpcr.FZ = '0'; result = FPRoundBF(value, fpcr, rounding, fpexc, 2*N); if fpexc then FPProcessDenorms(type1, type2, 2*N, fpcr); return result<2*N-1:N>;
```

## J1.3.3.149 BFMinNum

```
// BFMinNum() // ========== bits(N) BFMinNum(bits(N) op1, bits(N) op2, FPCR_Type fpcr)
```

```
constant boolean fpexc = TRUE; return BFMinNum(op1, op2, fpcr, fpexc); // BFMinNum() // ========== // BFloat16 minimum number following computational behaviors corresponding // to instructions that read and write BFloat16 values. // Compare op1 and op2 and return the smaller number operand after rounding. // The 'fpcr' argument supplies the FPCR control bits. bits(N) BFMinNum(bits(N) op1_in, bits(N) op2_in, FPCR_Type fpcr, boolean fpexc) assert N == 16; constant boolean isbfloat16 = TRUE; bits(N) op1 = op1_in; bits(N) op2 = op2_in; constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1'; bits(N) result; (type1,-,-) = FPUnpackBase(op1, fpcr, fpexc, isbfloat16); (type2,-,-) = FPUnpackBase(op2, fpcr, fpexc, isbfloat16); constant boolean type1_nan = type1 IN {FPType_QNaN, FPType_SNaN}; constant boolean type2_nan = type2 IN {FPType_QNaN, FPType_SNaN}; if !(altfp && type1_nan && type2_nan) then // Treat a single quiet-NaN as +Infinity. if type1 == FPType_QNaN && type2 != FPType_QNaN then op1 = BFInfinity('0', N); elsif type1 != FPType_QNaN && type2 == FPType_QNaN then op2 = BFInfinity('0', N); constant boolean altfmaxfmin = FALSE; // Do not use alternate NaN handling result = BFMin(op1, op2, fpcr, altfmaxfmin, fpexc); return result;
```

```
J1.3.3.150 BFMul // BFMul() // ======= // Non-widening BFloat16 multiply used by SVE2 instructions. bits(16) BFMul(bits(16) op1, bits(16) op2, FPCR_Type fpcr) constant boolean fpexc = TRUE; return BFMul(op1, op2, fpcr, fpexc); // BFMul() // ======= // Non-widening BFloat16 multiply following computational behaviors // corresponding to instructions that read and write BFloat16 values. // Calculates op1 * op2. // The 'fpcr' argument supplies the FPCR control bits. bits(16) BFMul(bits(16) op1, bits(16) op2, FPCR_Type fpcr, boolean fpexc) constant FPRounding rounding = FPRoundingMode(fpcr); boolean done; bits(32) result; constant bits(32) op1_s = op1 : Zeros(16); constant bits(32) op2_s = op2 : Zeros(16); (type1,sign1,value1) = FPUnpack(op1_s, fpcr, fpexc); (type2,sign2,value2) = FPUnpack(op2_s, fpcr, fpexc); (done,result) = FPProcessNaNs(type1, type2, op1_s, op2_s, fpcr, fpexc);
```

```
if !done then inf1 = (type1 == FPType_Infinity); inf2 = (type2 == FPType_Infinity); zero1 = (type1 == FPType_Zero); zero2 = (type2 == FPType_Zero); if (inf1 && zero2) || (zero1 && inf2) then result = FPDefaultNaN(fpcr, 32); if fpexc then FPProcessException(FPExc_InvalidOp, fpcr); elsif inf1 || inf2 then result = FPInfinity(sign1 EOR sign2, 32); elsif zero1 || zero2 then result = FPZero(sign1 EOR sign2, 32); else result = FPRoundBF(value1*value2, fpcr, rounding, fpexc, 32); if fpexc then FPProcessDenorms(type1, type2, 32, fpcr); return result<31:16>;
```

## J1.3.3.151 BFMulAdd

```
// BFMulAdd() // ========== // Non-widening BFloat16 fused multiply-add used by SVE2 instructions. bits(16) BFMulAdd(bits(16) addend, bits(16) op1, bits(16) op2, FPCR_Type fpcr) constant boolean fpexc = TRUE; return BFMulAdd(addend, op1, op2, fpcr, fpexc); // BFMulAdd() // ========== // Non-widening BFloat16 fused multiply-add following computational behaviors // corresponding to instructions that read and write BFloat16 values. // Calculates addend + op1*op2 with a single rounding. // The 'fpcr' argument supplies the FPCR control bits. bits(16) BFMulAdd(bits(16) addend, bits(16) op1, bits(16) op2, FPCR_Type fpcr, boolean fpexc) constant FPRounding rounding = FPRoundingMode(fpcr); boolean done; bits(32) result; constant bits(32) addend_s = addend : Zeros(16); constant bits(32) op1_s = op1 : Zeros(16); constant bits(32) op2_s = op2 : Zeros(16); (typeA,signA,valueA) = FPUnpack(addend_s, fpcr, fpexc); (type1,sign1,value1) = FPUnpack(op1_s, fpcr, fpexc); (type2,sign2,value2) = FPUnpack(op2_s, fpcr, fpexc); inf1 = (type1 == FPType_Infinity); inf2 = (type2 == FPType_Infinity); zero1 = (type1 == FPType_Zero); zero2 = (type2 == FPType_Zero); (done,result) = FPProcessNaNs3(typeA, type1, type2, addend_s, op1_s, op2_s, fpcr, fpexc); if !(IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1') then if typeA == FPType_QNaN && ((inf1 && zero2) || (zero1 && inf2)) then result = FPDefaultNaN(fpcr, 32); if fpexc then FPProcessException(FPExc_InvalidOp, fpcr); if !done then infA = (typeA == FPType_Infinity); zeroA = (typeA == FPType_Zero);
```

```
// Determine sign and type product will have if it does not cause an // Invalid Operation. signP = sign1 EOR sign2; infP = inf1 || inf2; zeroP = zero1 || zero2; // Non SNaN-generated Invalid Operation cases are multiplies of zero // by infinity and additions of opposite-signed infinities. invalidop = (inf1 && zero2) || (zero1 && inf2) || (infA && infP && signA != signP); if invalidop then result = FPDefaultNaN(fpcr, 32); if fpexc then FPProcessException(FPExc_InvalidOp, fpcr); // Other cases involving infinities produce an infinity of the same sign. elsif (infA && signA == '0') || (infP && signP == '0') then result = FPInfinity('0', 32); elsif (infA && signA == '1') || (infP && signP == '1') then result = FPInfinity('1', 32); // Cases where the result is exactly zero and its sign is not determined by the // rounding mode are additions of same-signed zeros. elsif zeroA && zeroP && signA == signP then result = FPZero(signA, 32); // Otherwise calculate numerical result and round it. else result_value = valueA + (value1 * value2); if result_value == 0.0 then // Sign of exact zero result depends on rounding mode result_sign = if rounding == FPRounding_NEGINF then '1' else '0'; result = FPZero(result_sign, 32); else result = FPRoundBF(result_value, fpcr, rounding, fpexc, 32); if !invalidop && fpexc then FPProcessDenorms3(typeA, type1, type2, 32, fpcr);
```

return result&lt;31:16&gt;;

## J1.3.3.152 BFMulAddH

```
// BFMulAddH() // =========== // Used by BFMLALB, BFMLALT, BFMLSLB and BFMLSLT instructions. bits(32) BFMulAddH(bits(32) addend, bits(16) op1, bits(16) op2, FPCR_Type fpcr_in) constant bits(32) value1 = op1 : Zeros(16); constant bits(32) value2 = op2 : Zeros(16); FPCR_Type fpcr = fpcr_in; constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && fpcr.AH == '1'; // When using alternative floating-point behaviour, do not generate floating-point exceptions constant boolean fpexc = !altfp; if altfp then fpcr.<FIZ,FZ> = '11'; // Flush denormal input and // output to zero if altfp then fpcr.RMode = '00'; // Use RNE rounding mode return FPMulAdd(addend, value1, value2, fpcr, fpexc);
```

## J1.3.3.153 BFMulAddH\_ZA

```
// BFMulAddH_ZA() // ============== // Used by SME2 ZA-targeting BFMLAL and BFMLSL instructions.
```

```
bits(32) BFMulAddH_ZA(bits(32) addend, bits(16) op1, bits(16) op2, FPCR_Type fpcr) constant bits(32) value1 = op1 : Zeros(16); constant bits(32) value2 = op2 : Zeros(16); return FPMulAdd_ZA(addend, value1, value2, fpcr);
```

## J1.3.3.154 BFMulAdd\_ZA

```
// BFMulAdd_ZA() // ============= // Non-widening BFloat16 fused multiply-add used by SME2 ZA-targeting instructions. bits(16) BFMulAdd_ZA(bits(16) addend, bits(16) op1, bits(16) op2, FPCR_Type fpcr_in) constant boolean fpexc = FALSE; FPCR_Type fpcr = fpcr_in; fpcr.DN = '1'; // Generate default NaN values return BFMulAdd(addend, op1, op2, fpcr, fpexc);
```

## J1.3.3.155 BFMulH

```
// BFMulH() // ======== // BFloat16 widening multiply to single-precision following BFloat16 // computation behaviors. bits(32) BFMulH(bits(16) op1, bits(16) op2, FPCR_Type fpcr) bits(32) result; (type1,sign1,value1) = BFUnpack(op1); (type2,sign2,value2) = BFUnpack(op2); if type1 == FPType_QNaN || type2 == FPType_QNaN then result = FPDefaultNaN(fpcr, 32); else inf1 = (type1 == FPType_Infinity); inf2 = (type2 == FPType_Infinity); zero1 = (type1 == FPType_Zero); zero2 = (type2 == FPType_Zero); if (inf1 && zero2) || (zero1 && inf2) then result = FPDefaultNaN(fpcr, 32); elsif inf1 || inf2 then result = FPInfinity(sign1 EOR sign2, 32); elsif zero1 || zero2 then result = FPZero(sign1 EOR sign2, 32); else result = BFRound(value1*value2); return result;
```

## J1.3.3.156 BFNeg

```
// BFNeg() // ======= bits(16) BFNeg(bits(16) op) constant boolean honor_altfp = TRUE; // Honor alternate handling return BFNeg(op, honor_altfp); // BFNeg() // ======= bits(16) BFNeg(bits(16) op, boolean honor_altfp) if honor_altfp && !UsingAArch32() && IsFeatureImplemented(FEAT_AFP) then
```

```
if FPCR.AH == '1' then constant boolean fpexc = FALSE; constant boolean isbfloat16 = TRUE; (fptype, -, -) = FPUnpackBase(op, FPCR, fpexc, isbfloat16); if fptype IN {FPType_SNaN, FPType_QNaN} then return op; // When FPCR.AH=1, sign of NaN has no consequence return NOT(op<15>) : op<14:0>;
```

## J1.3.3.157 BFRound

```
// BFRound() // ========= // Converts a real number OP into a single-precision value using the // Round to Odd rounding mode and following BFloat16 computation behaviors. bits(32) BFRound(real op) assert op != 0.0; bits(32) result; // Format parameters -minimum exponent, numbers of exponent and fraction bits. constant integer minimum_exp = -126; constant integer E = 8; constant integer F = 23; // Split value into sign, unrounded mantissa and exponent. bit sign; integer exponent; real mantissa; if op < 0.0 then sign = '1'; mantissa = -op; else sign = '0'; mantissa = op; (mantissa, exponent) = NormalizeReal(mantissa); // Fixed Flush-to-zero. if exponent < minimum_exp then return FPZero(sign, 32); // Start creating the exponent value for the result. Start by biasing the actual exponent // so that the minimum exponent becomes 1, lower values 0 (indicating possible underflow). biased_exp = Max((exponent -minimum_exp) + 1, 0); if biased_exp == 0 then mantissa = mantissa / 2.0^(minimum_exp - exponent); // Get the unrounded mantissa as an integer, and the "units in last place" rounding error. int_mant = RoundDown(mantissa * 2.0^F); // < 2.0^F if biased_exp == 0, >= 2.0^F if not error = mantissa * 2.0^F - Real(int_mant); // Round to Odd if error != 0.0 && int_mant<0> == '0' then int_mant = int_mant + 1; // Deal with overflow and generate result. if biased_exp >= 2^E - 1 then result = FPInfinity(sign, 32); // Overflows generate appropriately-signed Infinity else result = sign : biased_exp<E-1:0> : int_mant<F-1:0>; return result;
```

## J1.3.3.158 BFScale

```
// BFScale() // ========= // Scales BFloat16 operand by 2.0 to the power of the signed integer value.
```

```
rounding, fpexc, 32);
```

```
bits(16) BFScale(bits(16) op, integer scale, FPCR_Type fpcr) bits(32) result; constant bits(32) op_s = op : Zeros(16); (fptype,sign,value) = FPUnpack(op_s, fpcr); if fptype == FPType_SNaN || fptype == FPType_QNaN then result = FPProcessNaN(fptype, op_s, fpcr); elsif fptype == FPType_Zero then result = FPZero(sign, 32); elsif fptype == FPType_Infinity then result = FPInfinity(sign, 32); else constant FPRounding rounding = FPRoundingMode(fpcr); constant boolean fpexc = TRUE; result = FPRoundBF(value * (2.0^scale), fpcr, if fpexc then FPProcessDenorm(fptype, 32, fpcr); return result<31:16>;
```

```
J1.3.3.159 BFSub // BFSub() // ======= // Non-widening BFloat16 subtraction used by SVE2 instructions. bits(16) BFSub(bits(16) op1, bits(16) op2, FPCR_Type fpcr) constant boolean fpexc = TRUE; return BFSub(op1, op2, fpcr, fpexc); // BFSub() // ======= // Non-widening BFloat16 subtraction following computational behaviors // corresponding to instructions that read and write BFloat16 values. // Calculates op1 - op2. // The 'fpcr' argument supplies the FPCR control bits. bits(16) BFSub(bits(16) op1, bits(16) op2, FPCR_Type fpcr, boolean fpexc) constant FPRounding rounding = FPRoundingMode(fpcr); boolean done; bits(32) result; constant bits(32) op1_s = op1 : Zeros(16); constant bits(32) op2_s = op2 : Zeros(16); (type1,sign1,value1) = FPUnpack(op1_s, fpcr, fpexc); (type2,sign2,value2) = FPUnpack(op2_s, fpcr, fpexc); (done,result) = FPProcessNaNs(type1, type2, op1_s, op2_s, fpcr, fpexc); if !done then inf1 = (type1 == FPType_Infinity); inf2 = (type2 == FPType_Infinity); zero1 = (type1 == FPType_Zero); zero2 = (type2 == FPType_Zero); if inf1 && inf2 && sign1 == sign2 then result = FPDefaultNaN(fpcr, 32); if fpexc then FPProcessException(FPExc_InvalidOp, fpcr); elsif (inf1 && sign1 == '0') || (inf2 && sign2 == '1') then result = FPInfinity('0', 32); elsif (inf1 && sign1 == '1') || (inf2 && sign2 == '0') then result = FPInfinity('1', 32); elsif zero1 && zero2 && sign1 == NOT(sign2) then result = FPZero(sign1, 32); else
```

```
result_value = value1 - value2; if result_value == 0.0 then // Sign of exact zero result depends on rounding mode result_sign = if rounding == FPRounding_NEGINF then '1' else '0'; result = FPZero(result_sign, 32); else result = FPRoundBF(result_value, fpcr, rounding, fpexc, 32); if fpexc then FPProcessDenorms(type1, type2, 32, fpcr); return result<31:16>;
```

## J1.3.3.160 BFSub\_ZA

```
// BFSub_ZA() // ========== // Non-widening BFloat16 subtraction used by SME2 ZA-targeting instructions. bits(16) BFSub_ZA(bits(16) op1, bits(16) op2, FPCR_Type fpcr_in) constant boolean fpexc = FALSE; FPCR_Type fpcr = fpcr_in; fpcr.DN = '1'; // Generate default NaN values return BFSub(op1, op2, fpcr, fpexc);
```

## J1.3.3.161 BFUnpack

```
// BFUnpack() // ========== // Unpacks a BFloat16 or single-precision value into its type, // sign bit and real number that it represents. // The real number result has the correct sign for numbers and infinities, // is very large in magnitude for infinities, and is 0.0 for NaNs. // (These values are chosen to simplify the description of // comparisons and conversions.) (FPType, bit, real) BFUnpack(bits(N) fpval) assert N IN {16,32}; bit sign; bits(8) exp; bits(23) frac; if N == 16 then sign = fpval<15>; exp = fpval<14:7>; frac = fpval<6:0> : Zeros(16); else // N == 32 sign = fpval<31>; exp = fpval<30:23>; frac = fpval<22:0>; FPType fptype; real value; if IsZero(exp) then fptype = FPType_Zero; value = 0.0; // Fixed Flush to Zero elsif IsOnes(exp) then if IsZero(frac) then fptype = FPType_Infinity; value = 2.0^1000000; else // no SNaN for BF16 arithmetic fptype = FPType_QNaN; value = 0.0; else fptype = FPType_Nonzero; value = 2.0^(UInt(exp)-127) * (1.0 + Real(UInt(frac)) * 2.0^-23); if sign == '1' then value = -value;
```

```
return (fptype, sign, value);
```

## J1.3.3.162 BFZero

```
// BFZero() // ======== bits(N) BFZero(bit sign, integer N) assert N == 16; constant integer E = 8; constant integer F = N - (E + 1); return sign : Zeros(E) : Zeros(F);
```

## J1.3.3.163 FPAdd\_BF16

```
// FPAdd_BF16() // ============ // Single-precision add following BFloat16 computation behaviors. bits(32) FPAdd_BF16(bits(32) op1, bits(32) op2, FPCR_Type fpcr) bits(32) result; (type1,sign1,value1) = BFUnpack(op1); (type2,sign2,value2) = BFUnpack(op2); if type1 == FPType_QNaN || type2 == FPType_QNaN then result = FPDefaultNaN(fpcr, 32); else inf1 = (type1 == FPType_Infinity); inf2 = (type2 == FPType_Infinity); zero1 = (type1 == FPType_Zero); zero2 = (type2 == FPType_Zero); if inf1 && inf2 && sign1 == NOT(sign2) then result = FPDefaultNaN(fpcr, 32); elsif (inf1 && sign1 == '0') || (inf2 && sign2 == '0') then result = FPInfinity('0', 32); elsif (inf1 && sign1 == '1') || (inf2 && sign2 == '1') then result = FPInfinity('1', 32); elsif zero1 && zero2 && sign1 == sign2 then result = FPZero(sign1, 32); else result_value = value1 + value2; if result_value == 0.0 then result = FPZero('0', 32); // Positive sign when Round to Odd else result = BFRound(result_value); return result;
```

## J1.3.3.164 FPConvertBF

```
// FPConvertBF() // ============= // Converts a single-precision OP to BFloat16 value using the // Round to Nearest Even rounding mode when executed from AArch64 state and // FPCR.AH == '1', otherwise rounding is controlled by FPCR/FPSCR. bits(16) FPConvertBF(bits(32) op, FPCR_Type fpcr_in, FPRounding rounding_in) constant integer halfsize = 16; FPCR_Type fpcr = fpcr_in; FPRounding rounding = rounding_in;
```

```
bits(32) result; // BF16 value in top 16 bits constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1'; constant boolean fpexc = !altfp; // Generate no floating-point exceptions if altfp then fpcr.<FIZ,FZ> = '11'; // Flush denormal input and output to zero if altfp then rounding = FPRounding_TIEEVEN; // Use RNE rounding mode // Unpack floating-point operand, with always flush-to-zero if fpcr.AH == '1'. (fptype,sign,value) = FPUnpack(op, fpcr, fpexc); if fptype == FPType_SNaN || fptype == FPType_QNaN then if fpcr.DN == '1' then result = FPDefaultNaN(fpcr, 32); else result = FPConvertNaN(op, 32); if fptype == FPType_SNaN then if fpexc then FPProcessException(FPExc_InvalidOp, fpcr); elsif fptype == FPType_Infinity then result = FPInfinity(sign, 32); elsif fptype == FPType_Zero then result = FPZero(sign, 32); else result = FPRoundBF(value, fpcr, rounding, fpexc, 32); // Returns correctly rounded BF16 value from top 16 bits return result<(2*halfsize)-1:halfsize>; // FPConvertBF() // ============= // Converts a single-precision operand to BFloat16 value. bits(16) FPConvertBF(bits(32) op, FPCR_Type fpcr) return FPConvertBF(op, fpcr, FPRoundingMode(fpcr));
```

```
J1.3.3.165 FPRoundBF // FPRoundBF() // =========== // Converts a real number OP into a BFloat16 value using the supplied // rounding mode RMODE. The 'fpexc' argument controls the generation of // floating-point exceptions. bits(N) FPRoundBF(real op, FPCR_Type fpcr, FPRounding rounding, boolean fpexc, integer N) assert N == 32; constant boolean isbfloat16 = TRUE; return FPRoundBase(op, fpcr, rounding, isbfloat16, fpexc, N); J1.3.3.166 FixedToFP // FixedToFP() // =========== // Convert M-bit fixed point 'op' with FBITS fractional bits to // N-bit precision floating point, controlled by UNSIGNED and ROUNDING. bits(N) FixedToFP(bits(M) op, integer fbits, boolean unsigned, FPCR_Type fpcr, FPRounding rounding, integer N) assert N IN {16,32,64}; assert M IN {16,32,64}; bits(N) result; assert fbits >= 0; assert rounding != FPRounding_ODD; // Correct signed-ness
```

```
int_operand = if unsigned then UInt(op) else SInt(op); // Scale by fractional bits and generate a real value real_operand = Real(int_operand) / 2.0^fbits; if real_operand == 0.0 then result = FPZero('0', N); else result = FPRound(real_operand, fpcr, rounding, N); return result; J1.3.3.167 BFConvertFP8 // BFConvertFP8() // ============== // Converts a BFloat16 OP to FP8 value. bits(8) BFConvertFP8(bits(16) op_in, FPCR_Type fpcr, FPMR_Type fpmr) constant bits(32) op = op_in : Zeros(16); return FPConvertFP8(op, fpcr, fpmr, 8); J1.3.3.168 FP8Bits // FP8Bits() // ========= // Returns the minimum exponent, numbers of exponent and fraction bits. FPBitsType FP8Bits(FP8Type fp8type) integer minimum_exp; integer F; if fp8type == FP8Type_OFP8_E4M3 then minimum_exp = -6; F = 3; else // fp8type == FP8Type_OFP8_E5M2 minimum_exp = -14; F = 2; return (F, minimum_exp); J1.3.3.169 FP8ConvertBF // FP8ConvertBF() // ============== // Converts an FP8 operand to BFloat16 value. bits(16) FP8ConvertBF(bits(8) op, boolean issrc2, FPCR_Type fpcr, FPMR_Type fpmr) constant boolean isbfloat16 = TRUE; constant bits(32) result = FP8ConvertFP(op, issrc2, fpcr, fpmr, isbfloat16, 32); return result<16+:16>; J1.3.3.170 FP8ConvertFP fpmr)
```

```
// FP8ConvertFP() // ============== // Converts an FP8 operand to half-precision value. bits(16) FP8ConvertFP(bits(8) op, boolean issrc2, FPCR_Type fpcr, FPMR_Type constant boolean isbfloat16 = FALSE; return FP8ConvertFP(op, issrc2, fpcr, fpmr, isbfloat16, 16); // FP8ConvertFP()
```

```
// ============== // Converts an FP8 operand to half-precision or BFloat16 value. // The downscaling factor in FPMR.LSCALE or FPMR.LSCALE2 is applied to // the value before rounding. bits(M) FP8ConvertFP(bits(8) op, boolean issrc2, FPCR_Type fpcr_in, FPMR_Type fpmr, boolean isbfloat16, integer M) assert M IN {16,32}; bits(M) result; constant boolean fpexc = TRUE; FPCR_Type fpcr = fpcr_in; // Do not flush denormal inputs and outputs to zero. // Do not support alternative half-precision format. fpcr.<FIZ,FZ,FZ16,AHP> = '0000'; rounding = FPRounding_TIEEVEN; constant FP8Type fp8type = (if issrc2 then FP8DecodeType(fpmr.F8S2) else FP8DecodeType(fpmr.F8S1)); (fptype,sign,value) = FP8Unpack(op, fp8type); if fptype == FPType_SNaN || fptype == FPType_QNaN then result = FPDefaultNaN(fpcr, M); if fptype == FPType_SNaN then FPProcessException(FPExc_InvalidOp, fpcr); elsif fptype == FPType_Infinity then result = FPInfinity(sign, M); elsif fptype == FPType_Zero then result = FPZero(sign, M); else integer dscale; if issrc2 then dscale = (if M == 16 then UInt(fpmr.LSCALE2<3:0>) else UInt(fpmr.LSCALE2<5:0>)); else dscale = (if M == 16 then UInt(fpmr.LSCALE<3:0>) else UInt(fpmr.LSCALE<5:0>)); constant real result_value = value * (2.0^-dscale); result = FPRoundBase(result_value, fpcr, rounding, isbfloat16, fpexc, M); return result; J1.3.3.171 FP8DecodeType // FP8DecodeType() // =============== // Decode the FP8 format encoded in F8S1, F8S2 or F8D field in FPMR FP8Type FP8DecodeType(bits(3) f8format) case f8format of when '000' return FP8Type_OFP8_E5M2; when '001' return FP8Type_OFP8_E4M3; otherwise return FP8Type_UNSUPPORTED; J1.3.3.172 FP8DefaultNaN // FP8DefaultNaN() // =============== bits(N) FP8DefaultNaN(FP8Type fp8type, FPCR_Type fpcr, integer N) assert N == 8; assert fp8type IN {FP8Type_OFP8_E5M2, FP8Type_OFP8_E4M3}; constant bit sign = if IsFeatureImplemented(FEAT_AFP) then fpcr.AH else '0';
```

```
constant integer E = if fp8type == FP8Type_OFP8_E4M3 then 4 else 5; constant integer F = N - (E + 1); bits(E) exp; bits(F) frac; case fp8type of when FP8Type_OFP8_E4M3 exp = Ones(E); frac = Ones(F); when FP8Type_OFP8_E5M2 exp = Ones(E); frac = '1':Zeros(F-1); return sign : exp : frac;
```

## J1.3.3.173 FP8DotAddFP

```
// FP8DotAddFP() // ============= bits(M) FP8DotAddFP(bits(M) addend, bits(N) op1, bits(N) op2, FPCR_Type fpcr, FPMR_Type fpmr) constant integer E = N DIV 8; return FP8DotAddFP(addend, op1, op2, E, fpcr, fpmr); // FP8DotAddFP() // ============= // Calculates result of "E"-way 8-bit floating-point dot-product with scaling // and addition to half-precision or single-precision value without // intermediate rounding. // c = round(c + 2^-S*(a1*b1+..+aE*bE)) // The 8-bit floating-point format for op1 is determined by FPMR.F8S1 // and the one for op2 by FPMR.F8S2. The scaling factor in FPMR.LSCALE // is applied to the sum-of-products before adding to the addend and rounding. bits(M) FP8DotAddFP(bits(M) addend, bits(N) op1, bits(N) op2, integer E, FPCR_Type fpcr_in, FPMR_Type fpmr) assert M IN {16,32}; assert N IN {2*M, M, M DIV 2, M DIV 4}; FPCR_Type fpcr = fpcr_in; bits(M) result; fpcr.<FIZ,FZ,FZ16> = '000'; // Do not flush denormal inputs and outputs to zero fpcr.DN = '1'; rounding = FPRounding_TIEEVEN; constant FP8Type fp8type1 = FP8DecodeType(fpmr.F8S1); constant FP8Type fp8type2 = FP8DecodeType(fpmr.F8S2); array[0..(E-1)] of FPType type1; array[0..(E-1)] of FPType type2; array[0..(E-1)] of bit sign1; array[0..(E-1)] of bit sign2; array[0..(E-1)] of real value1; array[0..(E-1)] of real value2; array[0..(E-1)] of boolean inf1; array[0..(E-1)] of boolean inf2; array[0..(E-1)] of boolean zero1; array[0..(E-1)] of boolean zero2; constant boolean fpexc = FALSE; (typeA,signA,valueA) = FPUnpack(addend, fpcr, fpexc); infA = (typeA == FPType_Infinity); zeroA = (typeA == FPType_Zero); boolean any_nan = typeA IN {FPType_SNaN, FPType_QNaN}; for i = 0 to E-1 (type1[i], sign1[i], value1[i]) = FP8Unpack(Elem[op1, i, N DIV E], fp8type1);
```

```
(type2[i], sign2[i], value2[i]) = FP8Unpack(Elem[op2, i, N DIV E], fp8type2); inf1[i] = (type1[i] == FPType_Infinity); zero1[i] = (type1[i] == FPType_Zero); inf2[i] = (type2[i] == FPType_Infinity); zero2[i] = (type2[i] == FPType_Zero); any_nan = (any_nan || type1[i] IN {FPType_SNaN, FPType_QNaN} || type2[i] IN {FPType_SNaN, FPType_QNaN}); if any_nan then result = FPDefaultNaN(fpcr, M); else // Determine sign and type products will have if it does not cause an Invalid // Operation. array [0..(E-1)] of bit signP; array [0..(E-1)] of boolean infP; array [0..(E-1)] of boolean zeroP; for i = 0 to E-1 signP[i] = sign1[i] EOR sign2[i]; infP[i] = inf1[i] || inf2[i]; zeroP[i] = zero1[i] || zero2[i]; // Detect non-numeric results of dot product and accumulate boolean posInfR = (infA && signA == '0'); boolean negInfR = (infA && signA == '1'); boolean zeroR = zeroA; boolean invalidop = FALSE; for i = 0 to E-1 // Result is infinity if any input is infinity posInfR = posInfR || (infP[i] && signP[i] == '0'); negInfR = negInfR || (infP[i] && signP[i] == '1'); // Result is zero if the addend and the products are zeroes of the same sign zeroR = zeroR && zeroP[i] && (signA == signP[i]); // Non SNaN-generated Invalid Operation cases are multiplies of zero // by infinity and additions of opposite-signed infinities. invalidop = (invalidop || (inf1[i] && zero2[i]) || (zero1[i] && inf2[i]) || (infA && infP[i] && (signA != signP[i]))); for j = i+1 to E-1 invalidop = invalidop || (infP[i] && infP[j] && (signP[i] != signP[j])); if invalidop then result = FPDefaultNaN(fpcr, M); // Other cases involving infinities produce an infinity of the same sign. elsif posInfR then result = FPInfinity('0', M); elsif negInfR then result = FPInfinity('1', M); // Cases where the result is exactly zero and its sign is not determined by the // rounding mode are additions of same-signed zeros. elsif zeroR then result = FPZero(signA, M); // Otherwise calculate numerical value and round it. else // Apply scaling to sum-of-product constant integer dscale = if M == 32 then UInt(fpmr.LSCALE) else UInt(fpmr.LSCALE<3:0>); real dp_value = value1[0] * value2[0]; for i = 1 to E-1 dp_value = dp_value + value1[i] * value2[i]; constant real result_value = valueA + dp_value * (2.0^-dscale); if result_value == 0.0 then // Sign of exact zero result is '0' for RNE rounding mode result = FPZero('0', M); else constant boolean satoflo = (fpmr.OSM == '1'); result = FPRound_FP8(result_value, fpcr, rounding, satoflo, M);
```

```
return result;
```

## J1.3.3.174 FP8Infinity

```
// FP8Infinity() // ============= bits(N) FP8Infinity(FP8Type fp8type, bit sign, integer N) assert N == 8; assert fp8type IN {FP8Type_OFP8_E5M2, FP8Type_OFP8_E4M3}; constant integer E = if fp8type == FP8Type_OFP8_E4M3 then 4 else 5; constant integer F = N - (E + 1); bits(E) exp; bits(F) frac; case fp8type of when FP8Type_OFP8_E4M3 exp = Ones(E); frac = Ones(F); when FP8Type_OFP8_E5M2 exp = Ones(E); frac = Zeros(F); return sign : exp : frac;
```

## J1.3.3.175 FP8MatMulAddFP

```
// FP8MatMulAddFP() // ================ // 8-bit floating-point matrix multiply with scaling and add to half-precision // or single-precision matrix. // result[2, 2] = addend[2, 2] + (op1[2, E] * op2[E, 2]) bits(N) FP8MatMulAddFP(bits(N) addend, bits(N) op1, bits(N) op2, integer E, FPCR_Type fpcr, FPMR_Type fpmr) assert N IN {64, 128}; assert N == E*16; constant integer M = N DIV 4; bits(N) result; for i = 0 to 1 for j = 0 to 1 constant bits(2*M) elt1 = Elem[op1, i, 2*M]; constant bits(2*M) elt2 = Elem[op2, j, 2*M]; constant bits(M) sum = Elem[addend, 2*i + j, M]; Elem[result, 2*i + j, M] = FP8DotAddFP(sum, elt1, elt2, E, fpcr, fpmr); return result;
```

## J1.3.3.176 FP8MaxNormal

```
// FP8MaxNormal() // ============== bits(N) FP8MaxNormal(FP8Type fp8type, bit sign, integer N) assert N == 8; assert fp8type IN {FP8Type_OFP8_E5M2, FP8Type_OFP8_E4M3}; constant integer E = if fp8type == FP8Type_OFP8_E4M3 then 4 else 5; constant integer F = N - (E + 1); bits(E) exp;
```

```
bits(F) frac; case fp8type of when FP8Type_OFP8_E4M3 exp = Ones(E); frac = when FP8Type_OFP8_E5M2 exp = frac = Ones(F); return sign : exp : frac;
```

```
Ones(F-1):'0'; Ones(E-1):'0'; J1.3.3.177 FP8MulAddFP // FP8MulAddFP() // ============= bits(M) FP8MulAddFP(bits(M) addend, bits(8) op1, bits(8) op2, FPCR_Type fpcr, FPMR_Type fpmr) assert M IN {16,32}; constant integer E = 1; return FP8DotAddFP(addend, op1, op2, E, fpcr, fpmr); J1.3.3.178 FP8Round // FP8Round() // ========== // Used by FP8 downconvert instructions which observe FPMR.OSC // to convert a real number OP into an FP8 value. bits(N) FP8Round(real op, FP8Type fp8type, FPCR_Type fpcr, FPMR_Type fpmr, integer N) assert N == 8; assert fp8type IN {FP8Type_OFP8_E5M2, FP8Type_OFP8_E4M3}; assert op != 0.0; bits(N) result; // Format parameters -minimum exponent, numbers of exponent and fraction bits. constant (F, minimum_exp) = FP8Bits(fp8type); constant E = (N F) 1; // Split value into sign, unrounded mantissa and exponent. bit sign; integer exponent; real mantissa; if op < 0.0 then sign = '1'; mantissa = -op; else sign = '0'; mantissa = op; (mantissa, exponent) = NormalizeReal(mantissa); // When TRUE, detection of underflow occurs after rounding. altfp = IsFeatureImplemented(FEAT_AFP) && fpcr.AH == '1'; biased_exp_unconstrained = (exponent - minimum_exp) + 1; int_mant_unconstrained = RoundDown(mantissa * 2.0^F); error_unconstrained = mantissa * 2.0^F Real(int_mant_unconstrained); // Start creating the exponent value for the result. Start by biasing the actual exponent // so that the minimum exponent becomes 1, lower values 0 (indicating possible underflow). biased_exp = Max((exponent -minimum_exp) + 1, 0); if biased_exp == 0 then mantissa = mantissa / 2.0^(minimum_exp - exponent); // Get the unrounded mantissa as an integer, and the "units in last place" rounding error.
```

```
int_mant = RoundDown(mantissa * 2.0^F); // < 2.0^F if biased_exp == 0, >= 2.0^F if not error = mantissa * 2.0^F - Real(int_mant); constant boolean trapped_UF = fpcr.UFE == '1' && (!InStreamingMode() || IsFullA64Enabled()); boolean round_up_unconstrained; boolean round_up; if altfp then // Round to Nearest Even round_up_unconstrained = (error_unconstrained > 0.5 || (error_unconstrained == 0.5 && int_mant_unconstrained<0> == '1')); round_up = (error > 0.5 || (error == 0.5 && int_mant<0> == '1')); if round_up_unconstrained then int_mant_unconstrained = int_mant_unconstrained + 1; if int_mant_unconstrained == 2^(F+1) then // Rounded up to next exponent biased_exp_unconstrained = biased_exp_unconstrained + 1; int_mant_unconstrained = int_mant_unconstrained DIV 2; // Follow alternate floating-point behavior of underflow after rounding if (biased_exp_unconstrained < 1 && int_mant_unconstrained != 0 && (error != 0.0 || trapped_UF)) then FPProcessException(FPExc_Underflow, fpcr); else // altfp == FALSE // Underflow occurs if exponent is too small before rounding, and result is inexact or // the Underflow exception is trapped. This applies before rounding if FPCR.AH != '1'. if biased_exp == 0 && (error != 0.0 || trapped_UF) then FPProcessException(FPExc_Underflow, fpcr); // Round to Nearest Even round_up = (error > 0.5 || (error == 0.5 && int_mant<0> == '1')); if round_up then int_mant = int_mant + 1; if int_mant == 2^F then // Rounded up from denormalized to normalized biased_exp = 1; if int_mant == 2^(F+1) then // Rounded up to next exponent biased_exp = biased_exp + 1; int_mant = int_mant DIV 2; // Deal with overflow and generate result. boolean overflow; case fp8type of when FP8Type_OFP8_E4M3 overflow = biased_exp >= 2^E || (biased_exp == 2^E - 1 && int_mant == 2^(F+1) 1); when FP8Type_OFP8_E5M2 overflow = biased_exp >= 2^E - 1; if overflow then result = (if fpmr.OSC == '0' then FP8Infinity(fp8type, sign, N) else FP8MaxNormal(fp8type, sign, N)); // Flag Overflow exception regardless of FPMR.OSC FPProcessException(FPExc_Overflow, fpcr); error = 1.0; // Ensure that an Inexact exception occurs else result = sign : biased_exp<E-1:0> : int_mant<F-1:0>; // Deal with Inexact exception. if error != 0.0 then FPProcessException(FPExc_Inexact, fpcr); return result;
```

## J1.3.3.179

FP8Type

```
// FP8Type // ======= enumeration FP8Type {FP8Type_OFP8_E5M2, FP8Type_OFP8_E4M3, FP8Type_UNSUPPORTED};
```

## J1.3.3.180 FP8Unpack

```
// FP8Unpack() // =========== // Unpacks an FP8 value into its type, sign bit and real number that // it represents. (FPType, bit, real) FP8Unpack(bits(N) fpval, FP8Type fp8type) assert N == 8; constant integer E = if fp8type == FP8Type_OFP8_E4M3 then 4 else 5; constant integer F = N - (E + 1); constant bit sign = fpval<N-1>; constant bits(E) exp = fpval<(E+F)-1:F>; constant bits(F) frac = fpval<F-1:0>; real value; FPType fptype; if fp8type == FP8Type_OFP8_E4M3 then if IsZero(exp) then if IsZero(frac) then fptype = FPType_Zero; value = 0.0; else fptype = FPType_Denormal; value = 2.0^-6 * (Real(UInt(frac)) * 2.0^-3); elsif IsOnes(exp) && IsOnes(frac) then fptype = FPType_SNaN; value = 0.0; else fptype = FPType_Nonzero; value = 2.0^(UInt(exp)-7) * (1.0 + Real(UInt(frac)) * 2.0^-3); elsif fp8type == FP8Type_OFP8_E5M2 then if IsZero(exp) then if IsZero(frac) then fptype = FPType_Zero; value = 0.0; else fptype = FPType_Denormal; value = 2.0^-14 * (Real(UInt(frac)) * 2.0^-2); elsif IsOnes(exp) then if IsZero(frac) then fptype = FPType_Infinity; value = 2.0^1000000; else fptype = if frac<1> == '1' then FPType_QNaN else FPType_SNaN; value = 0.0; else fptype = FPType_Nonzero; value = 2.0^(UInt(exp)-15) * (1.0 + Real(UInt(frac)) * 2.0^-2); else // fp8type == FP8Type_UNSUPPORTED fptype = FPType_SNaN; value = 0.0; if sign == '1' then value = -value; return (fptype, sign, value);
```

## J1.3.3.181 FP8Zero

```
// FP8Zero() // ========= bits(N) FP8Zero(FP8Type fp8type, bit sign, integer N) assert N == 8; assert fp8type IN {FP8Type_OFP8_E5M2, FP8Type_OFP8_E4M3}; constant integer E = if fp8type == FP8Type_OFP8_E4M3 then 4 else constant integer F = N - (E + 1); return sign : Zeros(E) : Zeros(F);
```

```
5; J1.3.3.182 FPConvertFP8 // FPConvertFP8() // ============== // Converts a half-precision or single-precision OP to FP8 value. // The scaling factor in FPMR.NSCALE is applied to the value before rounding. bits(M) FPConvertFP8(bits(N) op, FPCR_Type fpcr_in, FPMR_Type fpmr, integer M) assert N IN {16,32} && M == 8; bits(M) result; constant boolean fpexc = TRUE; FPCR_Type fpcr = fpcr_in; fpcr.<FIZ,FZ,FZ16> = '000'; // Do not flush denormal inputs and outputs to zero constant FP8Type fp8type = FP8DecodeType(fpmr.F8D); (fptype,sign,value) = FPUnpack(op, fpcr, fpexc); if fp8type == FP8Type_UNSUPPORTED then result = Ones(M); FPProcessException(FPExc_InvalidOp, fpcr); elsif fptype == FPType_SNaN || fptype == FPType_QNaN then result = FP8DefaultNaN(fp8type, fpcr, M); // Always generate Default NaN as result if fptype == FPType_SNaN then FPProcessException(FPExc_InvalidOp, fpcr); elsif fptype == FPType_Infinity then result = (if fpmr.OSC == '0' then FP8Infinity(fp8type, sign, M) else FP8MaxNormal(fp8type, sign, M)); elsif fptype == FPType_Zero then result = FP8Zero(fp8type, sign, M); else constant integer scale = if N == 16 then SInt(fpmr.NSCALE<4:0>) else SInt(fpmr.NSCALE); constant real result_value = value * (2.0^scale); result = FP8Round(result_value, fp8type, fpcr, fpmr, M); return result; J1.3.3.183 FPAbs // FPAbs() // ======= bits(N) FPAbs(bits(N) op, FPCR_Type fpcr) assert N IN {16,32,64}; if !UsingAArch32() && IsFeatureImplemented(FEAT_AFP) then if fpcr.AH == '1' then (fptype, -, -) = FPUnpack(op, fpcr, FALSE); if fptype IN {FPType_SNaN, FPType_QNaN} then return op; // When fpcr.AH=1, sign of NaN has no consequence return '0' : op<N-2:0>;
```

## J1.3.3.184 FPAbsMax

```
// FPAbsMax() // ========== // Compare absolute value of two operands and return the larger absolute // value without rounding. bits(N) FPAbsMax(bits(N) op1_in, bits(N) op2_in, FPCR_Type fpcr_in) assert N IN {16,32,64}; boolean done; bits(N) result; FPCR_Type fpcr = fpcr_in; fpcr.<AH,FIZ,FZ,FZ16> = '0000'; op1 = '0':op1_in<N-2:0>; op2 = '0':op2_in<N-2:0>; (type1,-,value1) = FPUnpack(op1, fpcr); (type2,-,value2) = FPUnpack(op2, fpcr); (done,result) = FPProcessNaNs(type1, type2, op1_in, op2_in, fpcr); if !done then // This condition covers all results other than NaNs, // including Zero & Infinity result = if value1 > value2 then op1 else op2; return result; J1.3.3.185 FPAbsMin // FPAbsMin() // ========== // Compare absolute value of two operands and return the smaller absolute // value without rounding. bits(N) FPAbsMin(bits(N) op1_in, bits(N) op2_in, FPCR_Type fpcr_in) assert N IN {16,32,64}; boolean done; bits(N) result; FPCR_Type fpcr = fpcr_in; fpcr.<AH,FIZ,FZ,FZ16> = '0000'; op1 = '0':op1_in<N-2:0>; op2 = '0':op2_in<N-2:0>; (type1,-,value1) = FPUnpack(op1, fpcr); (type2,-,value2) = FPUnpack(op2, fpcr); (done,result) = FPProcessNaNs(type1, type2, op1_in, op2_in, fpcr); if !done then // This condition covers all results other than NaNs, // including Zero & Infinity result = if value1 < value2 then op1 else op2; return result; J1.3.3.186 FPAdd // FPAdd() // ======= bits(N) FPAdd(bits(N) op1, bits(N) op2, FPCR_Type fpcr) constant boolean fpexc = TRUE; // Generate floating-point exceptions
```

```
return FPAdd(op1, op2, fpcr, fpexc); op1, bits(N) op2, FPCR_Type fpcr, boolean fpexc) assert N IN {16,32,64}; rounding = FPRoundingMode(fpcr); (type1,sign1,value1) = FPUnpack(op1, fpcr, fpexc); (type2,sign2,value2) = FPUnpack(op2, fpcr, fpexc); (done,result) = FPProcessNaNs(type1, type2, op1, op2, fpcr, fpexc); if !done then inf1 = (type1 == FPType_Infinity); inf2 = (type2 == FPType_Infinity); zero1 = (type1 == FPType_Zero); zero2 = (type2 == FPType_Zero); if inf1 && inf2 && sign1 == NOT(sign2) then result = FPDefaultNaN(fpcr, N); if fpexc then FPProcessException(FPExc_InvalidOp, fpcr); elsif (inf1 && sign1 == '0') || (inf2 && sign2 == '0') then result = FPInfinity('0', N); elsif (inf1 && sign1 == '1') || (inf2 && sign2 == '1') then result = FPInfinity('1', N); elsif zero1 && zero2 && sign1 == sign2 then result = FPZero(sign1, N); else result_value = value1 + value2; if result_value == 0.0 then // Sign of exact zero result depends on rounding mode result_sign = if rounding == FPRounding_NEGINF then '1' else '0'; result = FPZero(result_sign, N); else result = FPRound(result_value, fpcr, rounding, fpexc, N); if fpexc then FPProcessDenorms(type1, type2, N, fpcr); return result;
```

```
// FPAdd() // ======= bits(N) FPAdd(bits(N) J1.3.3.187 FPAdd_ZA // FPAdd_ZA() // ========== // Calculates op1+op2 for SME2 ZA-targeting instructions. bits(N) FPAdd_ZA(bits(N) op1, bits(N) op2, FPCR_Type fpcr_in) FPCR_Type fpcr = fpcr_in; constant boolean fpexc = FALSE; // Do not generate floating-point exceptions fpcr.DN = '1'; // Generate default NaN values return FPAdd(op1, op2, fpcr, fpexc); J1.3.3.188 FPBits // FPBits() // ======== // Returns the minimum exponent, numbers of exponent and fraction bits. FPBitsType FPBits(integer N, boolean isbfloat16) FPFracBits F; integer minimum_exp; if N == 16 then minimum_exp = -14; F = 10; elsif N == 32 && isbfloat16 then minimum_exp = -126; F = 7; elsif N == 32 then
```

```
minimum_exp = -126; F = 23; else // N == 64 minimum_exp = -1022; F = 52; return (F, minimum_exp);
```

## J1.3.3.189 FPBitsType

```
// FPBitsType // ========== type FPBitsType = (FPFracBits, integer);
```

## J1.3.3.190 FPFracBits

```
// FPFracBits // ========== type FPFracBits = integer;
```

## J1.3.3.191 FPCompare

```
// FPCompare() // =========== bits(4) FPCompare(bits(N) op1, bits(N) op2, boolean signal_nans, FPCR_Type fpcr) assert N IN {16,32,64}; (type1,sign1,value1) = FPUnpack(op1, fpcr); (type2,sign2,value2) = FPUnpack(op2, fpcr); bits(4) result; if type1 IN {FPType_SNaN, FPType_QNaN} || type2 IN {FPType_SNaN, FPType_QNaN} then result = '0011'; if type1 == FPType_SNaN || type2 == FPType_SNaN || signal_nans then FPProcessException(FPExc_InvalidOp, fpcr); else // All non-NaN cases can be evaluated on the values produced by FPUnpack() if value1 == value2 then result = '0110'; elsif value1 < value2 then result = '1000'; else // value1 > value2 result = '0010'; FPProcessDenorms(type1, type2, N, fpcr); return result;
```

## J1.3.3.192 FPCompareEQ

```
// FPCompareEQ() // ============= boolean FPCompareEQ(bits(N) op1, bits(N) op2, FPCR_Type fpcr) assert N IN {16,32,64}; (type1,sign1,value1) = FPUnpack(op1, fpcr); (type2,sign2,value2) = FPUnpack(op2, fpcr); boolean result; if type1 IN {FPType_SNaN, FPType_QNaN} || type2 IN {FPType_SNaN, FPType_QNaN} then result = FALSE;
```

```
if type1 == FPType_SNaN || type2 == FPType_SNaN then FPProcessException(FPExc_InvalidOp, fpcr); else // All non-NaN cases can be evaluated on the values produced by result = (value1 == value2); FPProcessDenorms(type1, type2, N, fpcr); return result;
```

```
// FPConvert() // =========== // Convert floating point 'op' with N-bit precision // with rounding controlled by ROUNDING. // This is used by the FP-to-FP conversion instructions and so for // half-precision data ignores FZ16, but observes AHP.
```

## FPUnpack() J1.3.3.193 FPCompareGE // FPCompareGE() // ============= boolean FPCompareGE(bits(N) op1, bits(N) op2, FPCR\_Type fpcr) assert N IN {16,32,64}; (type1,sign1,value1) = FPUnpack(op1, fpcr); (type2,sign2,value2) = FPUnpack(op2, fpcr); boolean result; if type1 IN {FPType\_SNaN, FPType\_QNaN} || type2 IN {FPType\_SNaN, FPType\_QNaN} then result = FALSE; FPProcessException(FPExc\_InvalidOp, fpcr); else // All non-NaN cases can be evaluated on the values produced by FPUnpack() result = (value1 &gt;= value2); FPProcessDenorms(type1, type2, N, fpcr); return result; J1.3.3.194 FPCompareGT // FPCompareGT() // ============= boolean FPCompareGT(bits(N) op1, bits(N) op2, FPCR\_Type fpcr) assert N IN {16,32,64}; (type1,sign1,value1) = FPUnpack(op1, fpcr); (type2,sign2,value2) = FPUnpack(op2, fpcr); boolean result; if type1 IN {FPType\_SNaN, FPType\_QNaN} || type2 IN {FPType\_SNaN, FPType\_QNaN} then result = FALSE; FPProcessException(FPExc\_InvalidOp, fpcr); else // All non-NaN cases can be evaluated on the values produced by FPUnpack() result = (value1 &gt; value2); FPProcessDenorms(type1, type2, N, fpcr); return result; J1.3.3.195 FPConvert to M-bit precision,

```
bits(M) FPConvert(bits(N) op, FPCR_Type fpcr, FPRounding rounding, integer M) assert M IN {16,32,64}; assert N IN {16,32,64}; bits(M) result; // Unpack floating-point operand optionally with flush-to-zero. (fptype,sign,value) = FPUnpackCV(op, fpcr); alt_hp = (M == 16) && (fpcr.AHP == '1'); if fptype == FPType_SNaN || fptype == FPType_QNaN then if alt_hp then result = FPZero(sign, M); elsif fpcr.DN == '1' then result = FPDefaultNaN(fpcr, M); else result = FPConvertNaN(op, M); if fptype == FPType_SNaN || alt_hp then FPProcessException(FPExc_InvalidOp,fpcr); elsif fptype == FPType_Infinity then if alt_hp then result = sign:Ones(M-1); FPProcessException(FPExc_InvalidOp, fpcr); else result = FPInfinity(sign, M); elsif fptype == FPType_Zero then result = FPZero(sign, M); else result = FPRoundCV(value, fpcr, rounding, M); FPProcessDenorm(fptype, N, fpcr); return result; // FPConvert() // =========== bits(M) FPConvert(bits(N) op, FPCR_Type fpcr, integer M) return FPConvert(op, fpcr, FPRoundingMode(fpcr), M);
```

## J1.3.3.196 FPConvertNaN

```
// FPConvertNaN() // ============== // Converts a NaN of one floating-point type to another bits(M) FPConvertNaN(bits(N) op, integer M) assert N IN {16,32,64}; assert M IN {16,32,64}; bits(M) result; bits(51) frac; sign = op<N-1>; // Unpack payload from input NaN case N of when 64 frac = op<50:0>; when 32 frac = op<21:0>:Zeros(29); when 16 frac = op<8:0>:Zeros(42); // Repack payload into output NaN, while // converting an SNaN to a QNaN. case M of when 64 result = sign:Ones(M-52):frac; when 32 result = sign:Ones(M-23):frac<50:29>;
```

```
when 16 result = sign:Ones(M-10):frac<50:42>; return result;
```

```
// FPDefaultNaN() // ============== bits(N) FPDefaultNaN(FPCR_Type fpcr, integer N) assert N IN {16,32,64}; constant integer E = (if N == 16 then 5 else (if N == 32 then 8 else 11)); constant integer F = N - (E + 1); constant bit sign = if IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() then fpcr.AH else '0'; constant bits(E) exp = Ones(E); constant bits(F) frac = '1':Zeros(F-1); return sign : exp : frac;
```

## J1.3.3.197 FPDecodeRM // FPDecodeRM() // ============ // Decode most common AArch32 floating-point rounding encoding. FPRounding FPDecodeRM(bits(2) rm) FPRounding result; case rm of when '00' result = FPRounding\_TIEAWAY; // A when '01' result = FPRounding\_TIEEVEN; // N when '10' result = FPRounding\_POSINF; // P when '11' result = FPRounding\_NEGINF; // M return result; J1.3.3.198 FPDecodeRounding // FPDecodeRounding() // ================== // Decode floating-point rounding mode and common AArch64 encoding. FPRounding FPDecodeRounding(bits(2) rmode) case rmode of when '00' return FPRounding\_TIEEVEN; // N when '01' return FPRounding\_POSINF; // P when '10' return FPRounding\_NEGINF; // M when '11' return FPRounding\_ZERO; // Z J1.3.3.199 FPDefaultNaN J1.3.3.200 FPDiv // FPDiv() // ======= bits(N) FPDiv(bits(N) op1, bits(N) op2, FPCR\_Type fpcr) assert N IN {16,32,64}; (type1,sign1,value1) = FPUnpack(op1, fpcr); (type2,sign2,value2) = FPUnpack(op2, fpcr); (done,result) = FPProcessNaNs(type1, type2, op1, op2, fpcr);

```
if !done then inf1 = type1 == FPType_Infinity; inf2 = type2 == FPType_Infinity; zero1 = type1 == FPType_Zero; zero2 = type2 == FPType_Zero; if (inf1 && inf2) || (zero1 && zero2) then result = FPDefaultNaN(fpcr, N); FPProcessException(FPExc_InvalidOp, fpcr); elsif inf1 || zero2 then result = FPInfinity(sign1 EOR sign2, N); if !inf1 then elsif zero1 || inf2 then result = FPZero(sign1 EOR sign2, N); else result = FPRound(value1/value2, fpcr, N); if !zero2 then FPProcessDenorms(type1, type2, N, fpcr); return result;
```

```
FPProcessException(FPExc_DivideByZero, fpcr); J1.3.3.201 FPDot
```

```
// FPDot() // ======= // Calculates single-precision result of 2-way 16-bit floating-point dot-product // with a single rounding. // The 'fpcr' argument supplies the FPCR control bits and 'isbfloat16' // determines whether input operands are BFloat16 or half-precision type. // and 'fpexc' controls the generation of floating-point exceptions. bits(32) FPDot(bits(16) op1_a, bits(16) op1_b, bits(16) op2_a, bits(16) op2_b, FPCR_Type fpcr, boolean isbfloat16) constant boolean fpexc = TRUE; // Generate floating-point exceptions return FPDot(op1_a, op1_b, op2_a, op2_b, fpcr, isbfloat16, fpexc); bits(32) FPDot(bits(16) op1_a, bits(16) op1_b, bits(16) op2_a, bits(16) op2_b, FPCR_Type fpcr_in, boolean isbfloat16, boolean fpexc) FPCR_Type fpcr = fpcr_in; bits(32) result; boolean done; fpcr.AHP = '0'; // Ignore alternative half-precision option rounding = FPRoundingMode(fpcr); (type1_a,sign1_a,value1_a) = FPUnpackBase(op1_a, fpcr, fpexc, isbfloat16); (type1_b,sign1_b,value1_b) = FPUnpackBase(op1_b, fpcr, fpexc, isbfloat16); (type2_a,sign2_a,value2_a) = FPUnpackBase(op2_a, fpcr, fpexc, isbfloat16); (type2_b,sign2_b,value2_b) = FPUnpackBase(op2_b, fpcr, fpexc, isbfloat16); inf1_a = (type1_a == FPType_Infinity); zero1_a = (type1_a == FPType_Zero); inf1_b = (type1_b == FPType_Infinity); zero1_b = (type1_b == FPType_Zero); inf2_a = (type2_a == FPType_Infinity); zero2_a = (type2_a == FPType_Zero); inf2_b = (type2_b == FPType_Infinity); zero2_b = (type2_b == FPType_Zero); (done,result) = FPProcessNaNs4(type1_a, type1_b, type2_a, type2_b, op1_a, op1_b, op2_a, op2_b, fpcr, fpexc); if !done then // Determine sign and type products will have if it does not cause an Invalid // Operation. signPa = sign1_a EOR sign2_a; signPb = sign1_b EOR sign2_b; infPa = inf1_a || inf2_a; infPb = inf1_b || inf2_b;
```

```
zeroPa = zero1_a || zero2_a; zeroPb = zero1_b || zero2_b; // Non SNaN-generated Invalid Operation cases are multiplies of zero // by infinity and additions of opposite-signed infinities. invalidop = ((inf1_a && zero2_a) || (zero1_a && inf2_a) || (inf1_b && zero2_b) || (zero1_b && inf2_b) || (infPa && infPb && signPa != signPb)); if invalidop then result = FPDefaultNaN(fpcr, 32); if fpexc then FPProcessException(FPExc_InvalidOp, fpcr); // Other cases involving infinities produce an infinity of the same sign. elsif (infPa && signPa == '0') || (infPb && signPb == '0') then result = FPInfinity('0', 32); elsif (infPa && signPa == '1') || (infPb && signPb == '1') then result = FPInfinity('1', 32); // Cases where the result is exactly zero and its sign is not determined by the // rounding mode are additions of same-signed zeros. elsif zeroPa && zeroPb && signPa == signPb then result = FPZero(signPa, 32); // Otherwise calculate fused sum of products and round it. else result_value = (value1_a * value2_a) + (value1_b * value2_b); if result_value == 0.0 then // Sign of exact zero result depends on rounding mode result_sign = if rounding == FPRounding_NEGINF then '1' else '0'; result = FPZero(result_sign, 32); else result = FPRound(result_value, fpcr, rounding, fpexc, 32); result;
```

```
return J1.3.3.202 FPDotAdd // FPDotAdd() // ========== // Half-precision 2-way dot-product and add to single-precision. bits(32) FPDotAdd(bits(32) addend, bits(16) op1_a, bits(16) op1_b, bits(16) op2_a, bits(16) op2_b, FPCR_Type fpcr) bits(32) prod; constant boolean isbfloat16 = FALSE; constant boolean fpexc = TRUE; // Generate floating-point exceptions prod = FPDot(op1_a, op1_b, op2_a, op2_b, fpcr, isbfloat16, fpexc); result = FPAdd(addend, prod, fpcr, fpexc); return result; J1.3.3.203 FPDotAdd_ZA // FPDotAdd_ZA() // ============= // Half-precision 2-way dot-product and add to single-precision // for SME ZA-targeting instructions. bits(32) FPDotAdd_ZA(bits(32) addend, bits(16) op1_a, bits(16) op1_b, bits(16) op2_a, bits(16) op2_b, FPCR_Type fpcr_in) FPCR_Type fpcr = fpcr_in; bits(32) prod; constant boolean isbfloat16 = FALSE; constant boolean fpexc = FALSE; // Do not generate floating-point exceptions
```

```
fpcr.DN = '1'; // Generate default NaN values prod = FPDot(op1_a, op1_b, op2_a, op2_b, fpcr, isbfloat16, result = FPAdd(addend, prod, fpcr, fpexc); return result;
```

## fpexc); J1.3.3.204 FPExc // FPExc // ===== enumeration FPExc {FPExc\_InvalidOp, FPExc\_DivideByZero, FPExc\_Overflow, FPExc\_Underflow, FPExc\_Inexact, FPExc\_InputDenorm}; J1.3.3.205 FPInfinity // FPInfinity() // ============ bits(N) FPInfinity(bit sign, integer N) assert N IN {16,32,64}; constant integer E = (if N == 16 then 5 else (if N == 32 then 8 else 11)); constant integer F = N - (E + 1); constant bits(E) exp = Ones(E); constant bits(F) frac = Zeros(F); return sign : exp : frac; J1.3.3.206 FPMatMulAdd // FPMatMulAdd() // ============= // // Floating point matrix multiply and add to same precision matrix // result[2, 2] = addend[2, 2] + (op1[2, 2] * op2[2, 2]) bits(N) FPMatMulAdd(bits(N) addend, bits(N) op1, bits(N) op2, ESize esize, FPCR\_Type fpcr) assert N == esize * 2 * 2; bits(N) result; bits(esize) prod0, prod1, sum; for i = 0 to 1 for j = 0 to 1 sum = Elem[addend, 2*i + j, esize]; prod0 = FPMul(Elem[op1, 2*i + 0, esize], Elem[op2, 2*j + 0, esize], fpcr); prod1 = FPMul(Elem[op1, 2*i + 1, esize], Elem[op2, 2*j + 1, esize], fpcr); sum = FPAdd(sum, FPAdd(prod0, prod1, fpcr), fpcr); Elem[result, 2*i + j, esize] = sum; return result; J1.3.3.207 FPMatMulAddH // FPMatMulAddH() // ============== // Half-precision matrix multiply and add to single-precision matrix // result[2, 2] = addend[2, 2] + (op1[2, 4] * op2[4, 2]) bits(N) FPMatMulAddH(bits(N) addend, bits(N) op1, bits(N) op2, FPCR\_Type fpcr)

```
assert N == 128; constant integer M = 32; bits(N) result; constant boolean isbfloat16 = FALSE; for i = 0 to 1 for j = 0 to 1 bits(M) sum = Elem[addend, 2*i + j, M]; array[0..1] of bits(M) prod; for k = 0 to 1 constant bits(M DIV 2) elt1_a = Elem[op1, 4*i + 2*k + 0, M DIV 2]; constant bits(M DIV 2) elt1_b = Elem[op1, 4*i + 2*k + 1, M DIV 2]; constant bits(M DIV 2) elt2_a = Elem[op2, 4*j + 2*k + 0, M DIV 2]; constant bits(M DIV 2) elt2_b = Elem[op2, 4*j + 2*k + 1, M DIV 2]; prod[k] = FPDot(elt1_a, elt1_b, elt2_a, elt2_b, fpcr, isbfloat16); sum = FPAdd(sum, FPAdd(prod[0], prod[1], fpcr), fpcr); Elem[result, 2*i + j, M] = sum; return result;
```

## J1.3.3.208 FPMax

```
// FPMax() // ======= bits(N) FPMax(bits(N) op1, bits(N) op2, FPCR_Type fpcr) constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1'; constant boolean fpexc = TRUE; return FPMax(op1, op2, fpcr, altfp, fpexc); // FPMax() // ======= bits(N) FPMax(bits(N) op1, bits(N) op2, FPCR_Type fpcr, boolean altfp) constant boolean fpexc = TRUE; return FPMax(op1, op2, fpcr, altfp, fpexc); // FPMax() // ======= // Compare two inputs and return the larger value after rounding. The // 'fpcr' argument supplies the FPCR control bits and 'altfp' determines // if the function should use alternative floating-point behavior. bits(N) FPMax(bits(N) op1, bits(N) op2, FPCR_Type fpcr_in, boolean altfp, boolean fpexc) assert N IN {16,32,64}; boolean done; bits(N) result; FPCR_Type fpcr = fpcr_in; (type1,sign1,value1) = FPUnpack(op1, fpcr, fpexc); (type2,sign2,value2) = FPUnpack(op2, fpcr, fpexc); if altfp && type1 == FPType_Zero && type2 == FPType_Zero && sign1 != sign2 then // Alternate handling of zeros with differing sign return FPZero(sign2, N); elsif altfp && (type1 IN {FPType_SNaN, FPType_QNaN} || type2 IN {FPType_SNaN, FPType_QNaN}) then // Alternate handling of NaN inputs if fpexc then FPProcessException(FPExc_InvalidOp, fpcr); return (if type2 == FPType_Zero then FPZero(sign2, N) else op2); (done,result) = FPProcessNaNs(type1, type2, op1, op2, fpcr, fpexc); if !done then FPType fptype; bit sign; real value; if value1 > value2 then
```

```
(fptype,sign,value) = (type1,sign1,value1); else (fptype,sign,value) = (type2,sign2,value2); if fptype == FPType_Infinity then result = FPInfinity(sign, N); elsif fptype == FPType_Zero then sign = sign1 AND sign2; // Use most positive sign result = FPZero(sign, N); else // The use of FPRound() covers the case where there is a trapped underflow exception // for a denormalized number even though the result is exact. rounding = FPRoundingMode(fpcr); if altfp then // Denormal output is not flushed to zero fpcr.FZ = '0'; fpcr.FZ16 = '0'; result = FPRound(value, fpcr, rounding, fpexc, N); if fpexc then FPProcessDenorms(type1, type2, N, fpcr); return result;
```

```
J1.3.3.209 FPMaxNormal // FPMaxNormal() // ============= bits(N) FPMaxNormal(bit sign, integer N) assert N IN {16,32,64}; constant integer E = (if N == 16 then 5 else (if N == 32 then 8 else 11)); constant integer F = N - (E + 1); exp = Ones(E-1):'0'; frac = Ones(F); return sign : exp : frac; J1.3.3.210 FPMaxNum // FPMaxNum() // ========== bits(N) FPMaxNum(bits(N) op1, bits(N) op2, FPCR_Type fpcr) constant boolean fpexc = TRUE; return FPMaxNum(op1, op2, fpcr, fpexc); // FPMaxNum() // ========== bits(N) FPMaxNum(bits(N) op1_in, bits(N) op2_in, FPCR_Type fpcr, boolean fpexc) assert N IN {16,32,64}; bits(N) op1 = op1_in; bits(N) op2 = op2_in; (type1,-,-) = FPUnpack(op1, fpcr, fpexc); (type2,-,-) = FPUnpack(op2, fpcr, fpexc); constant boolean type1_nan = type1 IN {FPType_QNaN, FPType_SNaN}; constant boolean type2_nan = type2 IN {FPType_QNaN, FPType_SNaN}; constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1'; if !(altfp && type1_nan && type2_nan) then // Treat a single quiet-NaN as -Infinity. if type1 == FPType_QNaN && type2 != FPType_QNaN then op1 = FPInfinity('1', N); elsif type1 != FPType_QNaN && type2 == FPType_QNaN then op2 = FPInfinity('1', N);
```

```
altfmaxfmin = FALSE; // Restrict use of FMAX/FMIN NaN propagation rules result = FPMax(op1, op2, fpcr, altfmaxfmin, fpexc); return result;
```

## J1.3.3.211 IsMerging

```
// IsMerging() // =========== // Returns TRUE if the output elements other than the lowest are taken from // the destination register. boolean IsMerging(FPCR_Type fpcr) constant bit nep = (if IsFeatureImplemented(FEAT_SME) && PSTATE.SM == '1' && !IsFullA64Enabled() then '0' else fpcr.NEP); return IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && nep == '1';
```

## J1.3.3.212 FPMin

```
// FPMin() // ======= bits(N) FPMin(bits(N) op1, bits(N) op2, FPCR_Type fpcr) constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1'; constant boolean fpexc = TRUE; return FPMin(op1, op2, fpcr, altfp, fpexc); // FPMin() // ======= bits(N) FPMin(bits(N) op1, bits(N) op2, FPCR_Type fpcr, boolean altfp) constant boolean fpexc = TRUE; return FPMin(op1, op2, fpcr, altfp, fpexc); // FPMin() // ======= // Compare two inputs and return the smaller operand after rounding. The // 'fpcr' argument supplies the FPCR control bits and 'altfp' determines // if the function should use alternative floating-point behavior. bits(N) FPMin(bits(N) op1, bits(N) op2, FPCR_Type fpcr_in, boolean altfp, boolean fpexc) assert N IN {16,32,64}; boolean done; bits(N) result; FPCR_Type fpcr = fpcr_in; (type1,sign1,value1) = FPUnpack(op1, fpcr, fpexc); (type2,sign2,value2) = FPUnpack(op2, fpcr, fpexc); if altfp && type1 == FPType_Zero && type2 == FPType_Zero && sign1 != sign2 then // Alternate handling of zeros with differing sign return FPZero(sign2, N); elsif altfp && (type1 IN {FPType_SNaN, FPType_QNaN} || type2 IN {FPType_SNaN, FPType_QNaN}) then // Alternate handling of NaN inputs if fpexc then FPProcessException(FPExc_InvalidOp, fpcr); return (if type2 == FPType_Zero then FPZero(sign2, N) else op2); (done,result) = FPProcessNaNs(type1, type2, op1, op2, fpcr, fpexc); if !done then FPType fptype; bit sign; real value; FPRounding rounding;
```

```
if value1 < value2 then (fptype,sign,value) = (type1,sign1,value1); else (fptype,sign,value) = (type2,sign2,value2); if fptype == FPType_Infinity then result = FPInfinity(sign, N); elsif fptype == FPType_Zero then sign = sign1 OR sign2; // Use most negative sign result = FPZero(sign, N); else // The use of FPRound() covers the case where there is a trapped underflow exception // for a denormalized number even though the result is exact. rounding = FPRoundingMode(fpcr); if altfp then // Denormal output is not flushed to zero fpcr.FZ = '0'; fpcr.FZ16 = '0'; result = FPRound(value, fpcr, rounding, fpexc, N); if fpexc then FPProcessDenorms(type1, type2, N, fpcr); return result;
```

```
J1.3.3.213 FPMinNum // FPMinNum() // ========== bits(N) FPMinNum(bits(N) op1, bits(N) op2, FPCR_Type fpcr) constant boolean fpexc = TRUE; return FPMinNum(op1, op2, fpcr, fpexc); // FPMinNum() // ========== bits(N) FPMinNum(bits(N) op1_in, bits(N) op2_in, FPCR_Type fpcr, boolean fpexc) assert N IN {16,32,64}; bits(N) op1 = op1_in; bits(N) op2 = op2_in; (type1,-,-) = FPUnpack(op1, fpcr, fpexc); (type2,-,-) = FPUnpack(op2, fpcr, fpexc); constant boolean type1_nan = type1 IN {FPType_QNaN, FPType_SNaN}; constant boolean type2_nan = type2 IN {FPType_QNaN, FPType_SNaN}; constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1'; if !(altfp && type1_nan && type2_nan) then // Treat a single quiet-NaN as +Infinity. if type1 == FPType_QNaN && type2 != FPType_QNaN then op1 = FPInfinity('0', N); elsif type1 != FPType_QNaN && type2 == FPType_QNaN then op2 = FPInfinity('0', N); altfmaxfmin = FALSE; // Restrict use of FMAX/FMIN NaN propagation rules result = FPMin(op1, op2, fpcr, altfmaxfmin, fpexc); return result; J1.3.3.214 FPMul
```

```
// FPMul() // ======= bits(N) FPMul(bits(N) op1, bits(N) op2, FPCR_Type fpcr)
```

```
assert N IN {16,32,64}; (type1,sign1,value1) = FPUnpack(op1, fpcr); (type2,sign2,value2) = FPUnpack(op2, fpcr); (done,result) = FPProcessNaNs(type1, type2, op1, op2, fpcr); if !done then inf1 = (type1 == FPType_Infinity); inf2 = (type2 == FPType_Infinity); zero1 = (type1 == FPType_Zero); zero2 = (type2 == FPType_Zero); if (inf1 && zero2) || (zero1 && inf2) then result = FPDefaultNaN(fpcr, N); FPProcessException(FPExc_InvalidOp, fpcr); elsif inf1 || inf2 then result = FPInfinity(sign1 EOR sign2, N); elsif zero1 || zero2 then result = FPZero(sign1 EOR sign2, N); else result = FPRound(value1*value2, fpcr, N); FPProcessDenorms(type1, type2, N, fpcr); return result; J1.3.3.215 FPMulAdd addend, op1, op2, fpcr, fpexc);
```

```
// FPMulAdd() // ========== bits(N) FPMulAdd(bits(N) addend, bits(N) op1, bits(N) op2, FPCR_Type fpcr) constant boolean fpexc = TRUE; // Generate floating-point exceptions return FPMulAdd(addend, op1, op2, fpcr, fpexc); // FPMulAdd() // ========== // // Calculates addend + op1*op2 with a single rounding. The 'fpcr' argument // supplies the FPCR control bits, and 'fpexc' controls the generation of // floating-point exceptions. bits(N) FPMulAdd(bits(N) addend, bits(N) op1, bits(N) op2, FPCR_Type fpcr, boolean fpexc) assert N IN {16,32,64}; (typeA,signA,valueA) = FPUnpack(addend, fpcr, fpexc); (type1,sign1,value1) = FPUnpack(op1, fpcr, fpexc); (type2,sign2,value2) = FPUnpack(op2, fpcr, fpexc); rounding = FPRoundingMode(fpcr); inf1 = (type1 == FPType_Infinity); zero1 = (type1 == FPType_Zero); inf2 = (type2 == FPType_Infinity); zero2 = (type2 == FPType_Zero); (done,result) = FPProcessNaNs3(typeA, type1, type2, if !(IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1') then if typeA == FPType_QNaN && ((inf1 && zero2) || (zero1 && inf2)) then result = FPDefaultNaN(fpcr, N); if fpexc then FPProcessException(FPExc_InvalidOp, fpcr); if !done then infA = (typeA == FPType_Infinity); zeroA = (typeA == FPType_Zero); // Determine sign and type product will have if it does not cause an // Invalid Operation. signP = sign1 EOR sign2; infP = inf1 || inf2;
```

```
zeroP = zero1 || zero2; // Non SNaN-generated Invalid Operation cases are multiplies of zero // by infinity and additions of opposite-signed infinities. invalidop = (inf1 && zero2) || (zero1 && inf2) || (infA && infP && signA != signP); if invalidop then result = FPDefaultNaN(fpcr, N); if fpexc then FPProcessException(FPExc_InvalidOp, fpcr); // Other cases involving infinities produce an infinity of the same sign. elsif (infA && signA == '0') || (infP && signP == '0') then result = FPInfinity('0', N); elsif (infA && signA == '1') || (infP && signP == '1') then result = FPInfinity('1', N); // Cases where the result is exactly zero and its sign is not determined by the // rounding mode are additions of same-signed zeros. elsif zeroA && zeroP && signA == signP then result = FPZero(signA, N); // Otherwise calculate numerical result and round it. else result_value = valueA + (value1 * value2); if result_value == 0.0 then // Sign of exact zero result depends on rounding mode result_sign = if rounding == FPRounding_NEGINF then '1' else '0'; result = FPZero(result_sign, N); else result = FPRound(result_value, fpcr, rounding, fpexc, N); if !invalidop && fpexc then FPProcessDenorms3(typeA, type1, type2, N, fpcr); return result;
```

## J1.3.3.216 FPMulAdd\_ZA

```
// FPMulAdd_ZA() // ============= // Calculates addend + op1*op2 with a single rounding for SME ZA-targeting // instructions. bits(N) FPMulAdd_ZA(bits(N) addend, bits(N) op1, bits(N) op2, FPCR_Type FPCR_Type fpcr = fpcr_in; constant boolean fpexc = FALSE; // Do not generate floating-point fpcr.DN = '1'; // Generate default NaN values return FPMulAdd(addend, op1, op2, fpcr, fpexc);
```

```
// FPMulAddH() // =========== // Calculates addend + op1*op2. bits(32) FPMulAddH(bits(32) addend, bits(16) op1, bits(16) op2, FPCR_Type constant boolean fpexc = TRUE; // Generate floating-point exceptions return FPMulAddH(addend, op1, op2, fpcr, fpexc); // FPMulAddH() // =========== // Calculates addend + op1*op2. bits(32) FPMulAddH(bits(32) addend, bits(16) op1, bits(16) op2, FPCR_Type fpcr, boolean fpexc)
```

```
fpcr_in) exceptions J1.3.3.217 FPMulAddH fpcr)
```

```
rounding = FPRoundingMode(fpcr); (typeA,signA,valueA) = FPUnpack(addend, fpcr, fpexc); (type1,sign1,value1) = FPUnpack(op1, fpcr, fpexc); (type2,sign2,value2) = FPUnpack(op2, fpcr, fpexc); inf1 = (type1 == FPType_Infinity); zero1 = (type1 == FPType_Zero); inf2 = (type2 == FPType_Infinity); zero2 = (type2 == FPType_Zero); (done,result) = FPProcessNaNs3H(typeA, type1, type2, addend, op1, op2, fpcr, fpexc); if !(IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1') then if typeA == FPType_QNaN && ((inf1 && zero2) || (zero1 && inf2)) then result = FPDefaultNaN(fpcr, 32); if fpexc then FPProcessException(FPExc_InvalidOp, fpcr); if !done then infA = (typeA == FPType_Infinity); zeroA = (typeA == FPType_Zero); // Determine sign and type product will have if it does not cause an // Invalid Operation. signP = sign1 EOR sign2; infP = inf1 || inf2; zeroP = zero1 || zero2; // Non SNaN-generated Invalid Operation cases are multiplies of zero by infinity and // additions of opposite-signed infinities. invalidop = (inf1 && zero2) || (zero1 && inf2) || (infA && infP && signA != signP); if invalidop then result = FPDefaultNaN(fpcr, 32); if fpexc then FPProcessException(FPExc_InvalidOp, fpcr); // Other cases involving infinities produce an infinity of the same sign. elsif (infA && signA == '0') || (infP && signP == '0') then result = FPInfinity('0', 32); elsif (infA && signA == '1') || (infP && signP == '1') then result = FPInfinity('1', 32); // Cases where the result is exactly zero and its sign is not determined by the // rounding mode are additions of same-signed zeros. elsif zeroA && zeroP && signA == signP then result = FPZero(signA, 32); // Otherwise calculate numerical result and round it. else result_value = valueA + (value1 * value2); if result_value == 0.0 then // Sign of exact zero result depends on rounding mode result_sign = if rounding == FPRounding_NEGINF then '1' else '0'; result = FPZero(result_sign, 32); else result = FPRound(result_value, fpcr, rounding, fpexc, 32); if !invalidop && fpexc then FPProcessDenorm(typeA, 32, fpcr); return result;
```

## J1.3.3.218 FPMulAddH\_ZA

```
// FPMulAddH_ZA() // ============== // Calculates addend + op1*op2 for SME2 ZA-targeting instructions. bits(32) FPMulAddH_ZA(bits(32) addend, bits(16) op1, bits(16) op2, FPCR_Type fpcr_in) FPCR_Type fpcr = fpcr_in; constant boolean fpexc = FALSE; // Do not generate floating-point exceptions
```

```
fpcr.DN = '1'; // Generate default NaN values return FPMulAddH(addend, op1, op2, fpcr, fpexc);
```

## J1.3.3.219 FPProcessNaNs3H

```
// FPProcessNaNs3H() // ================= (boolean, bits(32)) FPProcessNaNs3H(FPType type1, FPType type2, FPType type3, bits(32) op1, bits(16) op2, bits(16) op3, FPCR_Type fpcr, boolean fpexc) bits(32) result; FPType type_nan; // When TRUE, use alternative NaN propagation rules. constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1'; constant boolean op1_nan = type1 IN {FPType_SNaN, FPType_QNaN}; constant boolean op2_nan = type2 IN {FPType_SNaN, FPType_QNaN}; constant boolean op3_nan = type3 IN {FPType_SNaN, FPType_QNaN}; if altfp then if (type1 == FPType_SNaN || type2 == FPType_SNaN || type3 == FPType_SNaN) then type_nan = FPType_SNaN; else type_nan = FPType_QNaN; boolean done; if altfp && op1_nan && op2_nan && op3_nan then // <n> register NaN selected done = TRUE; result = FPConvertNaN(FPProcessNaN(type_nan, op2, fpcr, fpexc), 32); elsif altfp && op2_nan && (op1_nan || op3_nan) then // <n> register NaN selected done = TRUE; result = FPConvertNaN(FPProcessNaN(type_nan, op2, fpcr, fpexc), 32); elsif altfp && op3_nan && op1_nan then // <m> register NaN selected done = TRUE; result = FPConvertNaN(FPProcessNaN(type_nan, op3, fpcr, fpexc), 32); elsif type1 == FPType_SNaN then done = TRUE; result = FPProcessNaN(type1, op1, fpcr, fpexc); elsif type2 == FPType_SNaN then done = TRUE; result = FPConvertNaN(FPProcessNaN(type2, op2, fpcr, fpexc), 32); elsif type3 == FPType_SNaN then done = TRUE; result = FPConvertNaN(FPProcessNaN(type3, op3, fpcr, fpexc), 32); elsif type1 == FPType_QNaN then done = TRUE; result = FPProcessNaN(type1, op1, fpcr, fpexc); elsif type2 == FPType_QNaN then done = TRUE; result = FPConvertNaN(FPProcessNaN(type2, op2, fpcr, fpexc), 32); elsif type3 == FPType_QNaN then done = TRUE; result = FPConvertNaN(FPProcessNaN(type3, op3, fpcr, fpexc), 32); else done = FALSE; result = Zeros(32); // 'Don't care' result return (done, result);
```

## J1.3.3.220 FPMulX

```
// FPMulX() // ======== bits(N) FPMulX(bits(N) op1, bits(N) op2, FPCR_Type fpcr) assert N IN {16,32,64}; bits(N) result; boolean done; (type1,sign1,value1) = FPUnpack(op1, fpcr); (type2,sign2,value2) = FPUnpack(op2, fpcr); (done,result) = FPProcessNaNs(type1, type2, op1, op2, fpcr); if !done then inf1 = (type1 == FPType_Infinity);
```

```
inf2 = (type2 == FPType_Infinity); zero1 = (type1 == FPType_Zero); zero2 = (type2 == FPType_Zero); if (inf1 && zero2) || (zero1 && inf2) then result = FPTwo(sign1 EOR sign2, N); elsif inf1 || inf2 then result = FPInfinity(sign1 EOR sign2, N); elsif zero1 || zero2 then result = FPZero(sign1 EOR sign2, N); else result = FPProcessDenorms(type1, type2, N, fpcr);
```

## FPRound(value1*value2, fpcr, N); return result; J1.3.3.221 FPNeg // FPNeg() // ======= bits(N) FPNeg(bits(N) op, FPCR\_Type fpcr) assert N IN {16,32,64}; if !UsingAArch32() &amp;&amp; IsFeatureImplemented(FEAT\_AFP) then if fpcr.AH == '1' then (fptype, -, -) = FPUnpack(op, fpcr, FALSE); if fptype IN {FPType\_SNaN, FPType\_QNaN} then return op; // When fpcr.AH=1, sign of NaN has no consequence return NOT(op&lt;N-1&gt;) : op&lt;N-2:0&gt;; J1.3.3.222 FPOnePointFive // FPOnePointFive() // ================ bits(N) FPOnePointFive(bit sign, integer N) assert N IN {16,32,64}; constant integer E = (if N == 16 then 5 else (if N == 32 then 8 else 11)); constant integer F = N - (E + 1); exp = '0':Ones(E-1); frac = '1':Zeros(F-1); result = sign : exp : frac; return result; J1.3.3.223 FPProcessDenorm

```
// FPProcessDenorm() // ================= // Handles denormal input in case of single-precision or double-precision // when using alternative floating-point mode. FPProcessDenorm(FPType fptype, integer N, FPCR_Type fpcr) constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1'; if altfp && N != 16 && fptype == FPType_Denormal then FPProcessException(FPExc_InputDenorm, fpcr);
```

## J1.3.3.224 FPProcessDenorms

```
// FPProcessDenorms() // ================== // Handles denormal input in case of single-precision or double-precision // when using alternative floating-point mode. FPProcessDenorms(FPType type1, FPType type2, integer N, FPCR_Type fpcr) constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == if altfp && N != 16 && (type1 == FPType_Denormal || type2 == FPType_Denormal) then FPProcessException(FPExc_InputDenorm, fpcr);
```

```
'1'; J1.3.3.225 FPProcessDenorms3 // FPProcessDenorms3() // =================== // Handles denormal input in case of single-precision or double-precision // when using alternative floating-point mode. FPProcessDenorms3(FPType type1, FPType type2, FPType type3, integer N, FPCR_Type fpcr) constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1'; if altfp && N != 16 && (type1 == FPType_Denormal || type2 == FPType_Denormal || type3 == FPType_Denormal) then FPProcessException(FPExc_InputDenorm, fpcr); J1.3.3.226 FPProcessDenorms4 // FPProcessDenorms4() // =================== // Handles denormal input in case of single-precision or double-precision // when using alternative floating-point mode. FPProcessDenorms4(FPType type1, FPType type2, FPType type3, FPType type4, integer N, FPCR_Type fpcr) constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1'; if altfp && N != 16 && (type1 == FPType_Denormal || type2 == FPType_Denormal || type3 == FPType_Denormal || type4 == FPType_Denormal) then FPProcessException(FPExc_InputDenorm, fpcr); J1.3.3.227 FPProcessException // FPProcessException() // ==================== // // The 'fpcr' argument supplies FPCR control bits. Status information is // updated directly in the FPSR where appropriate. FPProcessException(FPExc except, FPCR_Type fpcr) integer cumul; // Determine the cumulative exception bit number case except of when FPExc_InvalidOp cumul = 0; when FPExc_DivideByZero cumul = 1; when FPExc_Overflow cumul = 2; when FPExc_Underflow cumul = 3; when FPExc_Inexact cumul = 4; when FPExc_InputDenorm cumul = 7; enable = cumul + 8; if (fpcr<enable> == '1' && (!IsFeatureImplemented(FEAT_SME) || PSTATE.SM == '0' || IsFullA64Enabled())) then // Trapping of the exception enabled. // It is IMPLEMENTATION DEFINED whether the enable bit may be set at all,
```

```
// and if so then how exceptions and in what order that they may be // accumulated before calling FPTrappedException(). bits(8) accumulated_exceptions = GetAccumulatedFPExceptions(); accumulated_exceptions<cumul> = '1'; if boolean IMPLEMENTATION_DEFINED "Support trapping of floating-point exceptions" then if UsingAArch32() then AArch32.FPTrappedException(accumulated_exceptions); else is_ase = IsASEInstruction(); AArch64.FPTrappedException(is_ase, accumulated_exceptions); else // The exceptions generated by this instruction are accumulated by the PE and // FPTrappedException is called later during its execution, before the next // instruction is executed. This field is cleared at the start of each FP instruction. SetAccumulatedFPExceptions(accumulated_exceptions); elsif UsingAArch32() then // Set the cumulative exception bit FPSCR<cumul> = '1'; else // Set the cumulative exception bit FPSR<cumul> = '1'; return;
```

```
J1.3.3.228 FPProcessNaN // FPProcessNaN() // ============== bits(N) FPProcessNaN(FPType fptype, bits(N) op, FPCR_Type fpcr) constant boolean fpexc = TRUE; // Generate floating-point exceptions return FPProcessNaN(fptype, op, fpcr, fpexc); // FPProcessNaN() // ============== // Handle NaN input operands, returning the operand or default NaN value // if fpcr.DN is selected. The 'fpcr' argument supplies the FPCR control bits. // The 'fpexc' argument controls the generation of exceptions, regardless of // whether 'fptype' is a signalling NaN or a quiet NaN. bits(N) FPProcessNaN(FPType fptype, bits(N) op, FPCR_Type fpcr, boolean fpexc) assert N IN {16,32,64}; assert fptype IN {FPType_QNaN, FPType_SNaN}; integer topfrac; case N of when 16 topfrac = 9; when 32 topfrac = 22; when 64 topfrac = 51; result = op; if fptype == FPType_SNaN then result<topfrac> = '1'; if fpexc then FPProcessException(FPExc_InvalidOp, fpcr); if fpcr.DN == '1' then // DefaultNaN requested result = FPDefaultNaN(fpcr, N); return result; J1.3.3.229 FPProcessNaNs
```

```
// FPProcessNaNs() // =============== (boolean, bits(N)) FPProcessNaNs(FPType type1, FPType type2, bits(N) op1,
```

```
bits(N) op2, FPCR_Type fpcr) constant boolean fpexc = TRUE; // Generate floating-point exceptions return FPProcessNaNs(type1, type2, op1, op2, fpcr, fpexc); // FPProcessNaNs() // =============== // // The boolean part of the return value says whether a NaN has been found and // processed. The bits(N) part is only relevant if it has and supplies the // result of the operation. // // The 'fpcr' argument supplies FPCR control bits and 'altfmaxfmin' controls // alternative floating-point behavior for FMAX, FMIN and variants. 'fpexc' // controls the generation of floating-point exceptions. Status information // is updated directly in the FPSR where appropriate. (boolean, bits(N)) FPProcessNaNs(FPType type1, FPType type2, bits(N) op1, bits(N) op2, FPCR_Type fpcr, boolean fpexc) assert N IN {16,32,64}; boolean done; bits(N) result; constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1'; constant boolean op1_nan = type1 IN {FPType_SNaN, FPType_QNaN}; constant boolean op2_nan = type2 IN {FPType_SNaN, FPType_QNaN}; constant boolean any_snan = type1 == FPType_SNaN || type2 == FPType_SNaN; constant FPType type_nan = if any_snan then FPType_SNaN else FPType_QNaN; if altfp && op1_nan && op2_nan then // <n> register NaN selected done = TRUE; result = FPProcessNaN(type_nan, op1, fpcr, fpexc); elsif type1 == FPType_SNaN then done = TRUE; result = FPProcessNaN(type1, op1, fpcr, fpexc); elsif type2 == FPType_SNaN then done = TRUE; result = FPProcessNaN(type2, op2, fpcr, fpexc); elsif type1 == FPType_QNaN then done = TRUE; result = FPProcessNaN(type1, op1, fpcr, fpexc); elsif type2 == FPType_QNaN then done = TRUE; result = FPProcessNaN(type2, op2, fpcr, fpexc); else done = FALSE; result = Zeros(N); // 'Don't care' result return (done, result);
```

## J1.3.3.230 FPProcessNaNs3

```
// FPProcessNaNs3() // ================ (boolean, bits(N)) FPProcessNaNs3(FPType type1, FPType type2, FPType type3, bits(N) op1, bits(N) op2, bits(N) op3, FPCR_Type fpcr) constant boolean fpexc = TRUE; // Generate floating-point exceptions return FPProcessNaNs3(type1, type2, type3, op1, op2, op3, fpcr, fpexc); // FPProcessNaNs3() // ================ // The boolean part of the return value says whether a NaN has been found // processed. The bits(N) part is only relevant if it has and supplies the // result of the operation. // // The 'fpcr' argument supplies FPCR control bits and 'fpexc' controls the // generation of floating-point exceptions. Status information is updated // directly in the FPSR where appropriate. (boolean, bits(N)) FPProcessNaNs3(FPType type1, FPType type2, FPType type3, bits(N) op1, bits(N) op2, bits(N) op3,
```

```
and
```

```
FPCR_Type fpcr, boolean fpexc) assert N IN {16,32,64}; bits(N) result; constant boolean op1_nan = type1 IN {FPType_SNaN, FPType_QNaN}; constant boolean op2_nan = type2 IN {FPType_SNaN, FPType_QNaN}; constant boolean op3_nan = type3 IN {FPType_SNaN, FPType_QNaN}; constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1'; FPType type_nan; if altfp then if type1 == FPType_SNaN || type2 == FPType_SNaN || type3 == FPType_SNaN then type_nan = FPType_SNaN; else type_nan = FPType_QNaN; boolean done; if altfp && op1_nan && op2_nan && op3_nan then // <n> register NaN selected done = TRUE; result = FPProcessNaN(type_nan, op2, fpcr, fpexc); elsif altfp && op2_nan && (op1_nan || op3_nan) then // <n> register NaN selected done = TRUE; result = FPProcessNaN(type_nan, op2, fpcr, fpexc); elsif altfp && op3_nan && op1_nan then // <m> register NaN selected done = TRUE; result = FPProcessNaN(type_nan, op3, fpcr, fpexc); elsif type1 == FPType_SNaN then done = TRUE; result = FPProcessNaN(type1, op1, fpcr, fpexc); elsif type2 == FPType_SNaN then done = TRUE; result = FPProcessNaN(type2, op2, fpcr, fpexc); elsif type3 == FPType_SNaN then done = TRUE; result = FPProcessNaN(type3, op3, fpcr, fpexc); elsif type1 == FPType_QNaN then done = TRUE; result = FPProcessNaN(type1, op1, fpcr, fpexc); elsif type2 == FPType_QNaN then done = TRUE; result = FPProcessNaN(type2, op2, fpcr, fpexc); elsif type3 == FPType_QNaN then done = TRUE; result = FPProcessNaN(type3, op3, fpcr, fpexc); else done = FALSE; result = Zeros(N); // 'Don't care' result return (done, result); J1.3.3.231 FPProcessNaNs4 type4,
```

```
// FPProcessNaNs4() // ================ // The boolean part of the return value says whether a NaN has been found and // processed. The bits(N) part is only relevant if it has and supplies the // result of the operation. // // The 'fpcr' argument supplies FPCR control bits. // Status information is updated directly in the FPSR where appropriate. // The 'fpexc' controls the generation of floating-point exceptions. (boolean, bits(32)) FPProcessNaNs4(FPType type1, FPType type2, FPType type3, FPType bits(16) op1, bits(16) op2, bits(16) op3, bits(16) op4, FPCR_Type fpcr, boolean fpexc) bits(32) result; boolean done; // The FPCR.AH control does not affect these checks if type1 == FPType_SNaN then done = TRUE; result = FPConvertNaN(FPProcessNaN(type1, op1, fpcr, fpexc), 32); elsif type2 == FPType_SNaN then done = TRUE; result = FPConvertNaN(FPProcessNaN(type2, op2, fpcr, fpexc), 32); elsif type3 == FPType_SNaN then
```

```
done = TRUE; result = FPConvertNaN(FPProcessNaN(type3, op3, fpcr, fpexc), 32); elsif type4 == FPType_SNaN then done = TRUE; result = FPConvertNaN(FPProcessNaN(type4, op4, fpcr, fpexc), 32); elsif type1 == FPType_QNaN then done = TRUE; result = FPConvertNaN(FPProcessNaN(type1, op1, fpcr, fpexc), 32); elsif type2 == FPType_QNaN then done = TRUE; result = FPConvertNaN(FPProcessNaN(type2, op2, fpcr, fpexc), 32); elsif type3 == FPType_QNaN then done = TRUE; result = FPConvertNaN(FPProcessNaN(type3, op3, fpcr, fpexc), 32); elsif type4 == FPType_QNaN then done = TRUE; result = FPConvertNaN(FPProcessNaN(type4, op4, fpcr, fpexc), 32); else done = FALSE; result = Zeros(32); // 'Don't care' result return (done, result);
```

## J1.3.3.232 FPRecipEstimate

```
// FPRecipEstimate() // ================= bits(N) FPRecipEstimate(bits(N) operand, FPCR_Type fpcr_in) assert N IN {16,32,64}; FPCR_Type fpcr = fpcr_in; bits(N) result; boolean overflow_to_inf; // When using alternative floating-point behavior, do not generate // floating-point exceptions, flush denormal input and output to zero, // and use RNE rounding mode. constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1'; constant boolean fpexc = !altfp; if altfp then fpcr.<FIZ,FZ> = '11'; if altfp then fpcr.RMode = '00'; (fptype,sign,value) = FPUnpack(operand, fpcr, fpexc); constant FPRounding rounding = FPRoundingMode(fpcr); if fptype == FPType_SNaN || fptype == FPType_QNaN then result = FPProcessNaN(fptype, operand, fpcr, fpexc); elsif fptype == FPType_Infinity then result = FPZero(sign, N); elsif fptype == FPType_Zero then result = FPInfinity(sign, N); if fpexc then FPProcessException(FPExc_DivideByZero, fpcr); elsif ( (N == 16 && Abs(value) < 2.0^-16) || (N == 32 && Abs(value) < 2.0^-128) || (N == 64 && Abs(value) < 2.0^-1024) ) then case rounding of when FPRounding_TIEEVEN overflow_to_inf = TRUE; when FPRounding_POSINF overflow_to_inf = (sign == '0'); when FPRounding_NEGINF overflow_to_inf = (sign == '1'); when FPRounding_ZERO overflow_to_inf = FALSE; result = if overflow_to_inf then FPInfinity(sign, N) else FPMaxNormal(sign, N); if fpexc then FPProcessException(FPExc_Overflow, fpcr); FPProcessException(FPExc_Inexact, fpcr); elsif ((fpcr.FZ == '1' && N != 16) || (fpcr.FZ16 == '1' && N == 16)) && ( (N == 16 && Abs(value) >= 2.0^14) ||
```

```
(N == 32 && Abs(value) >= 2.0^126) || (N == 64 && Abs(value) >= 2.0^1022) ) then // Result flushed to zero of correct sign result = FPZero(sign, N); // Flush-to-zero never generates a trapped exception. if UsingAArch32() then FPSCR.UFC = '1'; else if fpexc then FPSR.UFC = '1'; else // Scale to a fixed point value in the range 0.5 <= x < 1.0 in steps of 1/512, and // calculate result exponent. Scaled value has copied sign bit, // exponent = 1022 = double-precision biased version of -1, // fraction = original fraction bits(52) fraction; integer exp; case N of when 16 fraction = operand<9:0> : Zeros(42); exp = UInt(operand<14:10>); when 32 fraction = operand<22:0> : Zeros(29); exp = UInt(operand<30:23>); when 64 fraction = operand<51:0>; exp = UInt(operand<62:52>); if exp == 0 then if fraction<51> == '0' then exp = -1; fraction = fraction<49:0>:'00'; else fraction = fraction<50:0>:'0'; integer scaled; constant boolean increasedprecision = N==32 && IsFeatureImplemented(FEAT_RPRES) && altfp; if !increasedprecision then scaled = UInt('1':fraction<51:44>); else scaled = UInt('1':fraction<51:41>); integer result_exp; case N of when 16 result_exp = 29 -exp; // In range 29-30 = -1 to 29+1 = 30 when 32 result_exp = 253 -exp; // In range 253-254 = -1 to 253+1 = 254 when 64 result_exp = 2045 -exp; // In range 2045-2046 = -1 to 2045+1 = 2046 // Scaled is in range 256 .. 511 or 2048 .. 4095 range representing a // fixed-point number in range [0.5 .. 1.0]. estimate = RecipEstimate(scaled, increasedprecision); // Estimate is in the range 256 .. 511 or 4096 .. 8191 representing a // fixed-point result in the range [1.0 .. 2.0]. // Convert to scaled floating point result with copied sign bit, // high-order bits from estimate, and exponent calculated above. if !increasedprecision then fraction = estimate<7:0> : Zeros(44); else fraction = estimate<11:0> : Zeros(40); if result_exp == 0 then fraction = '1' : fraction<51:1>; elsif result_exp == -1 then
```

```
fraction = '01' : fraction<51:2>; result_exp = 0; case N of when 16 result = sign : result_exp<N-12:0> : fraction<51:42>; when 32 result = sign : result_exp<N-25:0> : fraction<51:29>; when 64 result = sign : result_exp<N-54:0> : fraction<51:0>; return result;
```

## J1.3.3.233 RecipEstimate

```
// RecipEstimate() // =============== // Compute estimate of reciprocal of 9-bit fixed-point number. // // a is in range 256 .. 511 or 2048 .. 4096 representing a number in // the range 0.5 <= x < 1.0. // increasedprecision determines if the mantissa is 8-bit or 12-bit. // result is in the range 256 .. 511 or 4096 .. 8191 representing a // number in the range 1.0 to 511/256 or 1.00 to 8191/4096. integer RecipEstimate(integer a_in, boolean increasedprecision) integer a = a_in; integer r; if !increasedprecision then assert 256 <= a && a < 512; a = a*2+1; // Round to nearest constant integer b = (2 ^ 19) DIV a; r = (b+1) DIV 2; // Round to nearest assert 256 <= r && r < 512; else assert 2048 <= a && a < 4096; a = a*2+1; // Round to nearest constant integer b = (2 ^ 26) DIV a; r = (b+1) DIV 2; // Round to nearest assert 4096 <= r && r < 8192; return r;
```

## J1.3.3.234 FPRecpX

```
// FPRecpX() // ========= bits(N) FPRecpX(bits(N) op, FPCR_Type fpcr_in) assert N IN {16,32,64}; FPCR_Type fpcr = fpcr_in; constant boolean isbfloat16 = FALSE; constant (F, -) = FPBits(N, isbfloat16); constant E = (N F) 1; bits(N) result; bits(E) exp; bits(E) max_exp; constant bits(F) frac = Zeros(F); constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && fpcr.AH == '1'; constant boolean fpexc = !altfp; // Generate no floating-point exceptions if altfp then fpcr.<FIZ,FZ> = '11'; // Flush denormal input and output to zero (fptype,sign,value) = FPUnpack(op, fpcr, fpexc); exp = op<F+:E>; max_exp = Ones(E) 1; if fptype == FPType_SNaN || fptype == FPType_QNaN then
```

```
result = FPProcessNaN(fptype, op, fpcr, fpexc); else if IsZero(exp) then // Zero and denormals result = ZeroExtend(sign:max_exp:frac, N); else // Infinities and result = ZeroExtend(sign:NOT(exp):frac, N); return result;
```

```
// FPRoundBase() // ============= // For BFloat16, includes an explicit 'isbfloat16' argument. bits(N) FPRoundBase(real op, FPCR_Type fpcr, FPRounding rounding, boolean isbfloat16, integer constant boolean fpexc = TRUE; // Generate floating-point exceptions return FPRoundBase(op, fpcr, rounding, isbfloat16, fpexc, N); // FPRoundBase() // ============= // For FP8 multiply-accumulate, dot product, and outer product instructions, includes // an explicit saturation overflow argument. bits(N) FPRoundBase(real op, FPCR_Type fpcr, FPRounding rounding, boolean isbfloat16, boolean fpexc, integer N) constant boolean satoflo = FALSE; return FPRoundBase(op, fpcr, rounding, isbfloat16, fpexc, satoflo, N); // FPRoundBase() // ============= // Convert a real number 'op' into an N-bit floating-point value using the // supplied rounding mode 'rounding'. // // The 'fpcr' argument supplies FPCR control bits and 'fpexc' controls the
```

```
normals J1.3.3.235 FPRound // FPRound() // ========= // Generic conversion from precise, unbounded real data type to IEEE format. bits(N) FPRound(real op, FPCR_Type fpcr, integer N) return FPRound(op, fpcr, FPRoundingMode(fpcr), N); // FPRound() // ========= // For directed FP conversion, includes an explicit 'rounding' argument. bits(N) FPRound(real op, FPCR_Type fpcr_in, FPRounding rounding, integer N) constant boolean fpexc = TRUE; // Generate floating-point exceptions return FPRound(op, fpcr_in, rounding, fpexc, N); // FPRound() // ========= // For AltFP, includes an explicit FPEXC argument to disable exception // generation and switches off Arm alternate half-precision mode. bits(N) FPRound(real op, FPCR_Type fpcr_in, FPRounding rounding, boolean fpexc, integer N) FPCR_Type fpcr = fpcr_in; fpcr.AHP = '0'; constant boolean isbfloat16 = FALSE; return FPRoundBase(op, fpcr, rounding, isbfloat16, fpexc, N); J1.3.3.236 FPRoundBase N)
```

```
// generation of floating-point exceptions. Status information is updated // directly in the FPSR where appropriate. The 'satoflo' argument // controls whether overflow generates Infinity or MaxNorm for 8-bit floating-point // data processing instructions. bits(N) FPRoundBase(real op, FPCR_Type fpcr, FPRounding rounding, boolean isbfloat16, boolean fpexc, boolean satoflo, integer N) assert N IN {16,32,64}; assert op != 0.0; assert rounding != FPRounding_TIEAWAY; bits(N) result; // Obtain format parameters -minimum exponent, numbers of exponent and fraction bits. constant (F, minimum_exp) = FPBits(N, isbfloat16); constant zeros = if N == 32 && isbfloat16 then 16 else 0; constant E = N - (F + 1 + zeros); // Split value into sign, unrounded mantissa and exponent. bit sign; integer exponent; real mantissa; if op < 0.0 then sign = '1'; mantissa = -op; else sign = '0'; mantissa = op; (mantissa, exponent) = NormalizeReal(mantissa); // When TRUE, detection of underflow occurs after rounding and the test for a // denormalized number for single and double precision values occurs after rounding. altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1'; // Deal with flush-to-zero before rounding if FPCR.AH != '1'. if (!altfp && ((fpcr.FZ == '1' && N != 16) || (fpcr.FZ16 == '1' && N == 16)) && exponent < minimum_exp) then // Flush-to-zero never generates a trapped exception. if UsingAArch32() then FPSCR.UFC = '1'; else if fpexc then FPSR.UFC = '1'; return FPZero(sign, N); biased_exp_unconstrained = (exponent - minimum_exp) + 1; int_mant_unconstrained = RoundDown(mantissa * 2.0^F); error_unconstrained = mantissa * 2.0^F Real(int_mant_unconstrained); // Start creating the exponent value for the result. Start by biasing the actual exponent // so that the minimum exponent becomes 1, lower values 0 (indicating possible underflow). biased_exp = Max((exponent -minimum_exp) + 1, 0); if biased_exp == 0 then mantissa = mantissa / 2.0^(minimum_exp - exponent); // Get the unrounded mantissa as an integer, and the "units in last place" rounding error. int_mant = RoundDown(mantissa * 2.0^F); // < 2.0^F if biased_exp == 0, >= 2.0^F if not error = mantissa * 2.0^F - Real(int_mant); // Underflow occurs if exponent is too small before rounding, and result is inexact or // the Underflow exception is trapped. This applies before rounding if FPCR.AH != '1'. constant boolean trapped_UF = fpcr.UFE == '1' && (!InStreamingMode() || IsFullA64Enabled()); if !altfp && biased_exp == 0 && (error != 0.0 || trapped_UF) then if fpexc then FPProcessException(FPExc_Underflow, fpcr); // Round result according to rounding mode. boolean round_up_unconstrained; boolean round_up; boolean overflow_to_inf; if altfp then
```

```
case rounding of when FPRounding_TIEEVEN round_up_unconstrained = (error_unconstrained > 0.5 || (error_unconstrained == 0.5 && int_mant_unconstrained<0> == '1')); round_up = (error > 0.5 || (error == 0.5 && int_mant<0> == '1')); overflow_to_inf = !satoflo; when FPRounding_POSINF round_up_unconstrained = (error_unconstrained != 0.0 && sign == '0'); round_up = (error != 0.0 && sign == '0'); overflow_to_inf = (sign == '0'); when FPRounding_NEGINF round_up_unconstrained = (error_unconstrained != 0.0 && sign == '1'); round_up = (error != 0.0 && sign == '1'); overflow_to_inf = (sign == '1'); when FPRounding_ZERO, FPRounding_ODD round_up_unconstrained = FALSE; round_up = FALSE; overflow_to_inf = FALSE; if round_up_unconstrained then int_mant_unconstrained = int_mant_unconstrained + 1; if int_mant_unconstrained == 2^(F+1) then // Rounded up to next exponent biased_exp_unconstrained = biased_exp_unconstrained + 1; int_mant_unconstrained = int_mant_unconstrained DIV 2; // Deal with flush-to-zero and underflow after rounding if FPCR.AH == '1'. if biased_exp_unconstrained < 1 && int_mant_unconstrained != 0 then // the result of unconstrained rounding is less than the minimum normalized number if (fpcr.FZ == '1' && N != 16) || (fpcr.FZ16 == '1' && N == 16) then // Flush-to-zero if fpexc then FPSR.UFC = '1'; FPProcessException(FPExc_Inexact, fpcr); return FPZero(sign, N); elsif error != 0.0 || trapped_UF then if fpexc then FPProcessException(FPExc_Underflow, fpcr); else // altfp == FALSE case rounding of when FPRounding_TIEEVEN round_up = (error > 0.5 || (error == 0.5 && int_mant<0> == '1')); overflow_to_inf = !satoflo; when FPRounding_POSINF round_up = (error != 0.0 && sign == '0'); overflow_to_inf = (sign == '0'); when FPRounding_NEGINF round_up = (error != 0.0 && sign == '1'); overflow_to_inf = (sign == '1'); when FPRounding_ZERO, FPRounding_ODD round_up = FALSE; overflow_to_inf = FALSE; if round_up then int_mant = int_mant + 1; if int_mant == 2^F then // Rounded up from denormalized to normalized biased_exp = 1; if int_mant == 2^(F+1) then // Rounded up to next exponent biased_exp = biased_exp + 1; int_mant = int_mant DIV 2; // Handle rounding to odd if error != 0.0 && rounding == FPRounding_ODD && int_mant<0> == '0' then int_mant = int_mant + 1; // Deal with overflow and generate result. if N != 16 || fpcr.AHP == '0' then // Single, double or IEEE half precision if biased_exp >= 2^E - 1 then result = if overflow_to_inf then FPInfinity(sign, N) else FPMaxNormal(sign, N);
```

```
if fpexc then FPProcessException(FPExc_Overflow, fpcr); error = 1.0; // Ensure that an Inexact exception occurs else result = sign : biased_exp<E-1:0> : int_mant<F-1:0> : Zeros(N-(E+F+1)); else // Alternative half precision if biased_exp >= 2^E then result = sign : Ones(N-1); if fpexc then FPProcessException(FPExc_InvalidOp, fpcr); error = 0.0; // Ensure that an Inexact exception does not occur else result = sign : biased_exp<E-1:0> : int_mant<F-1:0> : Zeros(N-(E+F+1)); // Deal with Inexact exception. if error != 0.0 then if fpexc then FPProcessException(FPExc_Inexact, fpcr); return result;
```

## J1.3.3.237 FPRoundCV // FPRoundCV() // =========== // Used for FP to FP conversion instructions. // For half-precision data ignores FZ16 and observes AHP. bits(N) FPRoundCV(real op, FPCR\_Type fpcr\_in, FPRounding rounding, integer N) FPCR\_Type fpcr = fpcr\_in; fpcr.FZ16 = '0'; constant boolean fpexc = TRUE; // Generate floating-point exceptions constant boolean isbfloat16 = FALSE; return FPRoundBase(op, fpcr, rounding, isbfloat16, fpexc, N); J1.3.3.238 FPRound\_FP8 // FPRound\_FP8() // ============= // Used by FP8 multiply-accumulate, dot product, and outer product instructions // which observe FPMR.OSM. bits(N) FPRound\_FP8(real op, FPCR\_Type fpcr\_in, FPRounding rounding, boolean satoflo, integer N) FPCR\_Type fpcr = fpcr\_in; fpcr.AHP = '0'; constant boolean fpexc = FALSE; constant boolean isbfloat16 = FALSE; return FPRoundBase(op, fpcr, rounding, isbfloat16, fpexc, satoflo, N); J1.3.3.239 FPRounding values.

```
// FPRounding // ========== // The conversion and rounding functions take an explicit // rounding mode enumeration instead of booleans or FPCR enumeration FPRounding {FPRounding_TIEEVEN, FPRounding_POSINF, FPRounding_NEGINF, FPRounding_ZERO, FPRounding_TIEAWAY, FPRounding_ODD};
```

## J1.3.3.240 FPRoundingMode

```
// FPRoundingMode() // ================ // Return the current floating-point rounding mode. FPRounding FPRoundingMode(FPCR_Type fpcr) return FPDecodeRounding(fpcr.RMode);
```

## J1.3.3.241 FPRoundInt

```
// FPRoundInt() // ============ // Round op to nearest integral floating point value using rounding mode in FPCR/FPSCR. // If EXACT is TRUE, set FPSR.IXC if result is not numerically equal to op. bits(N) FPRoundInt(bits(N) op, FPCR_Type fpcr, FPRounding rounding, boolean exact) assert rounding != FPRounding_ODD; assert N IN {16,32,64}; // When alternative floating-point support is TRUE, do not generate // Input Denormal floating-point exceptions. altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1'; fpexc = !altfp; // Unpack using FPCR to determine if subnormals are flushed-to-zero. (fptype,sign,value) = FPUnpack(op, fpcr, fpexc); bits(N) result; if fptype == FPType_SNaN || fptype == FPType_QNaN then result = FPProcessNaN(fptype, op, fpcr); elsif fptype == FPType_Infinity then result = FPInfinity(sign, N); elsif fptype == FPType_Zero then result = FPZero(sign, N); else // Extract integer component. int_result = RoundDown(value); error = value -Real(int_result); // Determine whether supplied rounding mode requires an increment. boolean round_up; case rounding of when FPRounding_TIEEVEN round_up = (error > 0.5 || (error == 0.5 && int_result<0> == '1')); when FPRounding_POSINF round_up = (error != 0.0); when FPRounding_NEGINF round_up = FALSE; when FPRounding_ZERO round_up = (error != 0.0 && int_result < 0); when FPRounding_TIEAWAY round_up = (error > 0.5 || (error == 0.5 && int_result >= 0)); if round_up then int_result = int_result + 1; // Convert integer value into an equivalent real value. real_result = Real(int_result); // Re-encode as a floating-point value, result is always exact. if real_result == 0.0 then result = FPZero(sign, N); else
```

```
result = FPRound(real_result, fpcr, FPRounding_ZERO, N); // Generate inexact exceptions. if error != 0.0 && exact then FPProcessException(FPExc_Inexact, fpcr); return result;
```

## J1.3.3.242 FPRoundIntN

```
// FPRoundIntN() // ============= bits(N) FPRoundIntN(bits(N) op, FPCR_Type fpcr, FPRounding rounding, integer intsize) assert rounding != FPRounding_ODD; assert N IN {32,64}; assert intsize IN {32, 64}; integer exp; bits(N) result; boolean round_up; constant integer E = (if N == 32 then 8 else 11); constant integer F = N - (E + 1); // When alternative floating-point support is TRUE, do not generate // Input Denormal floating-point exceptions. altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1'; fpexc = !altfp; // Unpack using FPCR to determine if subnormals are flushed-to-zero. (fptype,sign,value) = FPUnpack(op, fpcr, fpexc); if fptype IN {FPType_SNaN, FPType_QNaN, FPType_Infinity} then if N == 32 then exp = 126 + intsize; result = '1':exp<(E-1):0>:Zeros(F); else exp = 1022+intsize; result = '1':exp<(E-1):0>:Zeros(F); FPProcessException(FPExc_InvalidOp, fpcr); elsif fptype == FPType_Zero then result = FPZero(sign, N); else // Extract integer component. int_result = RoundDown(value); error = value -Real(int_result); // Determine whether supplied rounding mode requires an increment. case rounding of when FPRounding_TIEEVEN round_up = error > 0.5 || (error == 0.5 && int_result<0> == '1'); when FPRounding_POSINF round_up = error != 0.0; when FPRounding_NEGINF round_up = FALSE; when FPRounding_ZERO round_up = error != 0.0 && int_result < 0; when FPRounding_TIEAWAY round_up = error > 0.5 || (error == 0.5 && int_result >= 0); if round_up then int_result = int_result + 1; overflow = int_result > 2^(intsize-1)-1 || int_result < -1*2^(intsize-1); if overflow then if N == 32 then exp = 126 + intsize;
```

```
result = '1':exp<(E-1):0>:Zeros(F); else exp = 1022 + intsize; result = '1':exp<(E-1):0>:Zeros(F); FPProcessException(FPExc_InvalidOp, fpcr); // This case shouldn't set Inexact. error = 0.0; else // Convert integer value into an equivalent real value. real_result = Real(int_result); // Re-encode as a floating-point value, result is if real_result == 0.0 then result = FPZero(sign, N); else result = FPRound(real_result, fpcr, FPRounding_ZERO, N); // Generate inexact exceptions. if error != 0.0 then FPProcessException(FPExc_Inexact, fpcr); return result;
```

## J1.3.3.243

```
// FPRSqrtEstimate() // ================= bits(N) FPRSqrtEstimate(bits(N) operand, FPCR_Type fpcr_in) assert N IN {16,32,64}; FPCR_Type fpcr = fpcr_in; // When using alternative floating-point behavior, do not generate // floating-point exceptions and flush denormal input to zero. constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == constant boolean fpexc = !altfp; if altfp then fpcr.<FIZ,FZ> = '11'; (fptype,sign,value) = FPUnpack(operand, fpcr, fpexc); bits(N) result; if fptype == FPType_SNaN || fptype == FPType_QNaN then result = FPProcessNaN(fptype, operand, fpcr, fpexc); elsif fptype == FPType_Zero then result = FPInfinity(sign, N); if fpexc then FPProcessException(FPExc_DivideByZero, fpcr); elsif sign == '1' then result = FPDefaultNaN(fpcr, N); if fpexc then FPProcessException(FPExc_InvalidOp, fpcr); elsif fptype == FPType_Infinity then result = FPZero('0', N); else // Scale to a fixed-point value in the range 0.25 <= x < 1.0 in steps of 512, with the // evenness or oddness of the exponent unchanged, and calculate result exponent. // Scaled value has copied sign bit, exponent = 1022 or 1021 = double-precision // biased version of -1 or -2, fraction = original fraction extended with zeros. bits(52) fraction; integer exp; case N of when 16 fraction = operand<9:0> : Zeros(42); exp = UInt(operand<14:10>); when 32
```

```
always exact. FPRSqrtEstimate '1';
```

```
fraction = operand<22:0> : Zeros(29); exp = UInt(operand<30:23>); when 64 fraction = operand<51:0>; exp = UInt(operand<62:52>); if exp == 0 then while fraction<51> == '0' do fraction = fraction<50:0> : '0'; exp = exp - 1; fraction = fraction<50:0> : '0'; integer scaled; constant boolean increasedprecision = N==32 && IsFeatureImplemented(FEAT_RPRES) && altfp; if !increasedprecision then if exp<0> == '0' then scaled = UInt('1':fraction<51:44>); else scaled = UInt('01':fraction<51:45>); else if exp<0> == '0' then scaled = UInt('1':fraction<51:41>); else scaled = UInt('01':fraction<51:42>); integer result_exp; case N of when 16 result_exp = ( 44 -exp) DIV 2; when 32 result_exp = ( 380 exp) DIV 2; when 64 result_exp = (3068 -exp) DIV 2; estimate = RecipSqrtEstimate(scaled, increasedprecision); // Estimate is in the range 256 .. 511 or 4096 .. 8191 representing a // fixed-point result in the range [1.0 .. 2.0]. // Convert to scaled floating point result with copied sign bit and high-order // fraction bits, and exponent calculated above. case N of when 16 result = '0' : result_exp<N-12:0> : estimate<7:0>:Zeros(2); when 32 if !increasedprecision then result = '0' : result_exp<N-25:0> : estimate<7:0>:Zeros(15); else result = '0' : result_exp<N-25:0> : estimate<11:0>:Zeros(11); when 64 result = '0' : result_exp<N-54:0> : estimate<7:0>:Zeros(44); return result;
```

```
J1.3.3.244 RecipSqrtEstimate // RecipSqrtEstimate() // =================== // Compute estimate of reciprocal square root of 9-bit fixed-point number. // // a_in is in range 128 .. 511 or 1024 .. 4095, with increased precision, // representing a number in the range 0.25 <= x < 1.0. // increasedprecision determines if the mantissa is 8-bit or 12-bit. // result is in the range 256 .. 511 or 4096 .. 8191, with increased precision, // representing a number in the range 1.0 to 511/256 or 8191/4096. integer RecipSqrtEstimate(integer a_in, boolean increasedprecision) integer a = a_in; integer r; if !increasedprecision then
```

```
assert 128 <= a && a < 512; if a < 256 then // a in [128, 255], represents a value in [0.25, 0.5) a = a*2+1; // promote to 9-bit range in units of 1/512 else // a in [256, 511], represents a value in [0.5, 1.0) a = (a >> 1) << 1; // Discard bottom bit a = (a+1)*2; // round up to nearest 1/256 and convert integer b = 512; while a*(b+1)*(b+1) < 2^28 do b = b+1; // b = largest b such that b < 2^14 / sqrt(a) r = (b+1) DIV 2; // Round to nearest assert 256 <= r && r < 512; else assert 1024 <= a && a < 4096; if a < 2048 then // a in [1024, 2047], represents a value in [0.25, 0.5) a = a*2 + 1; // promote to 13-bit range in units of 1/8192 else // a in [2048, 4095], represents a value in [0.5, 1.0) a = (a >> 1) << 1; // Discard bottom bit a = (a+1)*2; // round up to nearest 1/4096 and convert integer b = 8192; while a*(b+1)*(b+1) < 2^39 do b = b+1; r = (b+1) DIV 2; // Round to nearest assert 4096 <= r && r < 8192; return r;
```

## J1.3.3.245 FPSqrt

```
// FPSqrt() // ======== bits(N) FPSqrt(bits(N) op, FPCR_Type fpcr) assert N IN {16,32,64}; (fptype,sign,value) = FPUnpack(op, fpcr); bits(N) result; if fptype == FPType_SNaN || fptype == FPType_QNaN result = FPProcessNaN(fptype, op, fpcr); elsif fptype == FPType_Zero then result = FPZero(sign, N); elsif fptype == FPType_Infinity && sign == '0' then result = FPInfinity(sign, N); elsif sign == '1' then result = FPDefaultNaN(fpcr, N); FPProcessException(FPExc_InvalidOp, fpcr); else integer prec; boolean inexact; if N == 16 then prec = 13; // 10 fraction bit + 3 elsif N == 32 then prec = 26; // 23 fraction bits + 3 else // N == 64 prec = 55; // 52 fraction bits + 3 (value, inexact) = SqrtRoundDown(value, prec); result = FPRound(value, fpcr, N); if inexact then FPProcessException(FPExc_Inexact, fpcr); FPProcessDenorm(fptype, N, fpcr); return result;
```

## J1.3.3.246

FPSub

```
then
```

```
// FPSub() // ======= bits(N) FPSub(bits(N) op1, bits(N) op2, FPCR_Type fpcr) constant boolean fpexc = TRUE; // Generate floating-point exceptions return FPSub(op1, op2, fpcr, fpexc); // FPSub() // ======= bits(N) FPSub(bits(N) op1, bits(N) op2, FPCR_Type fpcr, boolean fpexc) assert N IN {16,32,64}; rounding = FPRoundingMode(fpcr); (type1,sign1,value1) = FPUnpack(op1, fpcr, fpexc); (type2,sign2,value2) = FPUnpack(op2, fpcr, fpexc); (done,result) = FPProcessNaNs(type1, type2, op1, op2, fpcr, fpexc); if !done then inf1 = (type1 == FPType_Infinity); inf2 = (type2 == FPType_Infinity); zero1 = (type1 == FPType_Zero); zero2 = (type2 == FPType_Zero); if inf1 && inf2 && sign1 == sign2 then result = FPDefaultNaN(fpcr, N); if fpexc then FPProcessException(FPExc_InvalidOp, fpcr); elsif (inf1 && sign1 == '0') || (inf2 && sign2 == '1') then result = FPInfinity('0', N); elsif (inf1 && sign1 == '1') || (inf2 && sign2 == '0') then result = FPInfinity('1', N); elsif zero1 && zero2 && sign1 == NOT(sign2) then result = FPZero(sign1, N); else result_value = value1 - value2; if result_value == 0.0 then // Sign of exact zero result depends on rounding mode result_sign = if rounding == FPRounding_NEGINF then '1' else '0'; result = FPZero(result_sign, N); else result = FPRound(result_value, fpcr, rounding, fpexc, N); if fpexc then FPProcessDenorms(type1, type2, N, fpcr); return result;
```

## J1.3.3.247 FPSub\_ZA

```
// FPSub_ZA() // ========== // Calculates op1-op2 for SME2 ZA-targeting instructions. bits(N) FPSub_ZA(bits(N) op1, bits(N) op2, FPCR_Type fpcr_in) FPCR_Type fpcr = fpcr_in; constant boolean fpexc = FALSE; // Do not generate floating-point fpcr.DN = '1'; // Generate default NaN values return FPSub(op1, op2, fpcr, fpexc);
```

## exceptions J1.3.3.248 FPThree // FPThree() // =========

```
bits(N) FPThree(bit sign, integer N) assert N IN {16,32,64}; constant integer E = (if N == 16 then 5 else (if N == 32 then 8 else constant integer F = N - (E + 1); exp = '1':Zeros(E-1); frac = '1':Zeros(F-1); result = sign : exp : frac; return result;
```

```
11));
```

```
J1.3.3.249 FPToFixed // FPToFixed() // =========== // Convert N-bit precision floating point 'op' to M-bit fixed point with // FBITS fractional bits, controlled by UNSIGNED and ROUNDING. bits(M) FPToFixed(bits(N) op, integer fbits, boolean unsigned, FPCR_Type fpcr, FPRounding rounding, integer M) assert N IN {16,32,64}; assert M IN {16,32,64}; assert fbits >= 0; assert rounding != FPRounding_ODD; // When alternative floating-point support is TRUE, do not generate // Input Denormal floating-point exceptions. altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1'; fpexc = !altfp; // Unpack using fpcr to determine if subnormals are flushed-to-zero. (fptype,sign,value) = FPUnpack(op, fpcr, fpexc); // If NaN, set cumulative flag or take exception. if fptype == FPType_SNaN || fptype == FPType_QNaN then FPProcessException(FPExc_InvalidOp, fpcr); // Scale by fractional bits and produce integer rounded towards minus-infinity. value = value * 2.0^fbits; int_result = RoundDown(value); error = value - Real(int_result); // Determine whether supplied rounding mode requires an increment. boolean round_up; case rounding of when FPRounding_TIEEVEN round_up = (error > 0.5 || (error == 0.5 && int_result<0> == '1')); when FPRounding_POSINF round_up = (error != 0.0); when FPRounding_NEGINF round_up = FALSE; when FPRounding_ZERO round_up = (error != 0.0 && int_result < 0); when FPRounding_TIEAWAY round_up = (error > 0.5 || (error == 0.5 && int_result >= 0)); if round_up then int_result = int_result + 1; // Generate saturated result and exceptions. (result, overflow) = SatQ(int_result, M, unsigned); if overflow then FPProcessException(FPExc_InvalidOp, fpcr); elsif error != 0.0 then FPProcessException(FPExc_Inexact, fpcr);
```

```
return result;
```

## J1.3.3.250 FPToFixedJS

```
// FPToFixedJS() // ============= // Converts a double precision floating point input value // to a signed integer, with rounding to zero. (bits(32), bit) FPToFixedJS(bits(64) op, FPCR_Type fpcr) // If FALSE, never generate Input Denormal floating-point exceptions. fpexc_idenorm = !(IsFeatureImplemented(FEAT_AFP) && !UsingAArch32() && fpcr.AH == '1'); // Unpack using fpcr to determine if subnormals are flushed-to-zero. (fptype,sign,value) = FPUnpack(op, fpcr, fpexc_idenorm); z = '1'; // If NaN, set cumulative flag or take exception. if fptype == FPType_SNaN || fptype == FPType_QNaN then FPProcessException(FPExc_InvalidOp, fpcr); z = '0'; int_result = RoundDown(value); error = value - Real(int_result); // Determine whether supplied rounding mode requires an increment. round_it_up = (error != 0.0 && int_result < 0); if round_it_up then int_result = int_result + 1; integer result; if int_result < 0 then result = int_result - 2^32*RoundUp(Real(int_result)/Real(2^32)); else result = int_result - 2^32*RoundDown(Real(int_result)/Real(2^32)); // Generate exceptions. if int_result < -(2^31) || int_result > (2^31)-1 then FPProcessException(FPExc_InvalidOp, fpcr); z = '0'; elsif error != 0.0 then FPProcessException(FPExc_Inexact, fpcr); z = '0'; elsif sign == '1' && value == 0.0 then z = '0'; elsif sign == '0' && value == 0.0 && !IsZero(op<51:0>) then z = '0'; if fptype == FPType_Infinity then result = 0; return (result<31:0>, z);
```

```
J1.3.3.251 FPTwo // FPTwo() // ======= bits(N) FPTwo(bit sign, integer N) assert N IN {16,32,64}; constant integer E = (if N == 16 then 5 else (if N == 32 then 8 else 11));
```

```
constant integer F = N - (E + 1); exp = '1':Zeros(E-1); frac = Zeros(F); result = sign : exp : frac; return result; J1.3.3.252 FPType // FPType // ====== enumeration FPType {FPType_Zero, FPType_Denormal, FPType_Nonzero, FPType_Infinity, FPType_QNaN, FPType_SNaN}; J1.3.3.253 FPUnpack // FPUnpack() // ========== (FPType, bit, real) FPUnpack(bits(N) fpval, FPCR_Type fpcr_in) FPCR_Type fpcr = fpcr_in; fpcr.AHP = '0'; constant boolean fpexc = TRUE; // Generate floating-point exceptions (fp_type, sign, value) = FPUnpackBase(fpval, fpcr, fpexc); return (fp_type, sign, value); // FPUnpack() // ========== // // Used by data processing, int/fixed to FP and FP to int/fixed conversion instructions. // For half-precision data it ignores AHP, and observes FZ16. (FPType, bit, real) FPUnpack(bits(N) fpval, FPCR_Type fpcr_in, boolean fpexc) FPCR_Type fpcr = fpcr_in; fpcr.AHP = '0'; (fp_type, sign, value) = FPUnpackBase(fpval, fpcr, fpexc); return (fp_type, sign, value); J1.3.3.254 FPUnpackBase
```

```
// FPUnpackBase() // ============== (FPType, bit, real) FPUnpackBase(bits(N) fpval, FPCR_Type fpcr, boolean fpexc) constant boolean isbfloat16 = FALSE; (fp_type, sign, value) = FPUnpackBase(fpval, fpcr, fpexc, isbfloat16); return (fp_type, sign, value); // FPUnpackBase() // ============== // // Unpack a floating-point number into its type, sign bit and the real number // that it represents. The real number result has the correct sign for numbers // and infinities, is very large in magnitude for infinities, and is 0.0 for // NaNs. (These values are chosen to simplify the description of comparisons // and conversions.) //
```

```
// The 'fpcr_in' argument supplies FPCR control bits, 'fpexc' controls the // generation of floating-point exceptions and 'isbfloat16' determines whether // N=16 signifies BFloat16 or half-precision type. Status information is updated // directly in the FPSR where appropriate. (FPType, bit, real) FPUnpackBase(bits(N) fpval, FPCR_Type fpcr_in, boolean fpexc, boolean isbfloat16) assert N IN {16,32,64}; constant FPCR_Type fpcr = fpcr_in; constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && !UsingAArch32(); constant boolean fiz = altfp && fpcr.FIZ == '1'; constant boolean fz = fpcr.FZ == '1' && !(altfp && fpcr.AH == '1'); real value; bit sign; FPType fptype; if N == 16 && !isbfloat16 then sign = fpval<15>; exp16 = fpval<14:10>; frac16 = fpval<9:0>; if IsZero(exp16) then if IsZero(frac16) || fpcr.FZ16 == '1' then fptype = FPType_Zero; value = 0.0; else fptype = FPType_Denormal; value = 2.0^-14 * (Real(UInt(frac16)) * 2.0^-10); elsif IsOnes(exp16) && fpcr.AHP == '0' then // Infinity or NaN in IEEE format if IsZero(frac16) then fptype = FPType_Infinity; value = 2.0^1000000; else fptype = if frac16<9> == '1' then FPType_QNaN else FPType_SNaN; value = 0.0; else fptype = FPType_Nonzero; value = 2.0^(UInt(exp16)-15) * (1.0 + Real(UInt(frac16)) * 2.0^-10); elsif N == 32 || isbfloat16 then bits(8) exp32; bits(23) frac32; if isbfloat16 then sign = fpval<15>; exp32 = fpval<14:7>; frac32 = fpval<6:0> : Zeros(16); else sign = fpval<31>; exp32 = fpval<30:23>; frac32 = fpval<22:0>; if IsZero(exp32) then if IsZero(frac32) then // Produce zero if value is zero. fptype = FPType_Zero; value = 0.0; elsif fz || fiz then // Flush-to-zero if FIZ==1 or AH,FZ==01 fptype = FPType_Zero; value = 0.0; // Check whether to raise Input Denormal floating-point exception. // fpcr.FIZ==1 does not raise Input Denormal exception. if fz then // Denormalized input flushed to zero if fpexc then FPProcessException(FPExc_InputDenorm, fpcr); else fptype = FPType_Denormal; value = 2.0^-126 * (Real(UInt(frac32)) * 2.0^-23); elsif IsOnes(exp32) then if IsZero(frac32) then fptype = FPType_Infinity; value = 2.0^1000000; else
```

```
fptype = if frac32<22> == '1' then FPType_QNaN else FPType_SNaN; value = 0.0; else fptype = FPType_Nonzero; value = 2.0^(UInt(exp32)-127) * (1.0 + Real(UInt(frac32)) * 2.0^-23); else // N == 64 sign = fpval<63>; exp64 = fpval<62:52>; frac64 = fpval<51:0>; if IsZero(exp64) then if IsZero(frac64) then // Produce zero if value is zero. fptype = FPType_Zero; value = 0.0; elsif fz || fiz then // Flush-to-zero if FIZ==1 or AH,FZ==01 fptype = FPType_Zero; value = 0.0; // Check whether to raise Input Denormal floating-point exception. // fpcr.FIZ==1 does not raise Input Denormal exception. if fz then // Denormalized input flushed to zero if fpexc then FPProcessException(FPExc_InputDenorm, fpcr); else fptype = FPType_Denormal; value = 2.0^-1022 * (Real(UInt(frac64)) * 2.0^-52); elsif IsOnes(exp64) then if IsZero(frac64) then fptype = FPType_Infinity; value = 2.0^1000000; else fptype = if frac64<51> == '1' then FPType_QNaN else FPType_SNaN; value = 0.0; else fptype = FPType_Nonzero; value = 2.0^(UInt(exp64)-1023) * (1.0 + Real(UInt(frac64)) * 2.0^-52); if sign == '1' then value = -value; return (fptype, sign, value);
```

## J1.3.3.255 FPUnpackCV

```
// FPUnpackCV() // ============ // // Used for FP to FP conversion instructions. // For half-precision data ignores FZ16 and observes AHP. (FPType, bit, real) FPUnpackCV(bits(N) fpval, FPCR_Type fpcr_in) FPCR_Type fpcr = fpcr_in; fpcr.FZ16 = '0'; constant boolean fpexc = TRUE; // Generate floating-point (fp_type, sign, value) = FPUnpackBase(fpval, fpcr, fpexc); return (fp_type, sign, value);
```

## J1.3.3.256 FPZero

```
// FPZero() // ======== bits(N) FPZero(bit sign, integer N) assert N IN {16,32,64}; constant integer E = (if N == 16 then 5 else (if N == 32 then 8 else constant integer F = N - (E + 1); exp = Zeros(E);
```

```
exceptions 11));
```

```
frac = Zeros(F); result = sign : exp : frac; return result;
```

## J1.3.3.257 VFPExpandImm

```
// VFPExpandImm() // ============== bits(N) VFPExpandImm(bits(8) imm8, integer N) assert N IN {16,32,64}; constant integer E = (if N == 16 then 5 else (if N == 32 then 8 else 11)); constant integer F = (N -E) - 1; sign = imm8<7>; exp = NOT(imm8<6>):Replicate(imm8<6>, E-3):imm8<5:4>; frac = imm8<3:0>:Zeros(F-4); result = sign : exp : frac; return result;
```

## J1.3.3.258 AddWithCarry

```
// AddWithCarry() // ============== // Integer addition with carry input, returning result and NZCV flags (bits(N), bits(4)) AddWithCarry(bits(N) x, bits(N) y, bit carry_in) constant integer unsigned_sum = UInt(x) + UInt(y) + UInt(carry_in); constant integer signed_sum = SInt(x) + SInt(y) + UInt(carry_in); constant bits(N) result = unsigned_sum<N-1:0>; // same value as constant bit n = result<N-1>; constant bit z = if IsZero(result) then '1' else '0'; constant bit c = if UInt(result) == unsigned_sum then '0' else '1'; constant bit v = if SInt(result) == signed_sum then '0' else '1'; return (result, n:z:c:v);
```

## J1.3.3.259 InterruptID

```
// InterruptID // =========== enumeration InterruptID { InterruptID_PMUIRQ, InterruptID_COMMIRQ, InterruptID_CTIIRQ, InterruptID_COMMRX, InterruptID_COMMTX, InterruptID_CNTP, InterruptID_CNTHP, InterruptID_CNTHPS, InterruptID_CNTPS, InterruptID_CNTV, InterruptID_CNTHV, InterruptID_CNTHVS, InterruptID_PMBIRQ, InterruptID_HACDBSIRQ, InterruptID_TRBIRQ, };
```

```
signed_sum<N-1:0>
```

## J1.3.3.260 SetInterruptRequestLevel

```
// SetInterruptRequestLevel() // ========================== // Set a level-sensitive interrupt to the specified level. SetInterruptRequestLevel(InterruptID id, Signal level);
```

## J1.3.3.261 AArch64.BranchAddr

```
// AArch64.BranchAddr() // ==================== // Return the virtual address with tag bits removed. // This is typically used when the address will be stored to the program counter. bits(64) AArch64.BranchAddr(bits(64) vaddress, bits(2) el) assert !UsingAArch32(); constant integer msbit = AddrTop(vaddress, TRUE, el); if msbit == 63 then return vaddress; elsif (el IN {EL0, EL1} || IsInHost()) && vaddress<msbit> == '1' then return SignExtend(vaddress<msbit:0>, 64); else return ZeroExtend(vaddress<msbit:0>, 64);
```

## J1.3.3.262 AccessDescriptor

```
// AccessDescriptor // ================ // Memory access or translation invocation details that steer architectural behavior type AccessDescriptor is ( AccessType acctype, bits(2) el, // Acting EL for the access SecurityState ss, // Acting Security State for the access boolean acqsc, // Acquire with Sequential Consistency boolean acqpc, // FEAT_LRCPC: Acquire with Processor Consistency boolean relsc, // Release with Sequential Consistency boolean limitedordered, // FEAT_LOR: Acquire/Release with limited ordering boolean exclusive, // Access has Exclusive semantics boolean atomicop, // FEAT_LSE: Atomic read-modify-write access MemAtomicOp modop, // FEAT_LSE: The modification operation in the 'atomicop' access boolean nontemporal, // Hints the access is non-temporal boolean read, // Read from memory or only require read permissions boolean write, // Write to memory or only require write permissions CacheOp cacheop, // DC/IC: Cache operation CacheOpScope opscope, // DC/IC: Scope of cache operation CacheType cachetype, // DC/IC: Type of target cache boolean pan, // FEAT_PAN: The access is subject to PSTATE.PAN boolean nonfault, // SVE: Non-faulting load boolean firstfault, // SVE: First-fault load boolean first, // SVE: First-fault load for the first active element boolean contiguous, // SVE: Contiguous load/store not gather load/scatter store boolean predicated, // SVE: Predicated load/store boolean streamingsve, // SME: Access made by PE while in streaming SVE mode boolean ls64, // FEAT_LS64: Accesses by accelerator support loads/stores boolean withstatus, // FEAT_LS64: Store with status result boolean mops, // FEAT_MOPS: Memory operation (CPY/SET) accesses boolean rcw, // FEAT_THE: Read-Check-Write access boolean rcws, // FEAT_THE: Read-Check-Write Software access boolean toplevel, // FEAT_THE: Translation table walk access for TTB address VARange varange, // FEAT_THE: The corresponding TTBR supplying the TTB boolean a32lsmd, // A32 Load/Store Multiple Data access
```

```
)
```

## J1.3.3.263 AccessType // AccessType // ========== enumeration AccessType { AccessType\_IFETCH, // Instruction FETCH AccessType\_GPR, // Software load/store to a General Purpose Register AccessType\_FP, // Software load/store to an FP register AccessType\_ASIMD, // Software ASIMD extension load/store instructions AccessType\_SVE, // Software SVE load/store instructions AccessType\_SME, // Software SME load/store instructions AccessType\_IC, // Sysop IC AccessType\_DC, // Sysop DC (not DC {Z,G,GZ}VA) AccessType\_DCZero, // Sysop DC {Z,G,GZ}VA AccessType\_AT, // Sysop AT AccessType\_NV2, // NV2 memory redirected access AccessType\_SPE, // Statistical Profiling buffer access AccessType\_GCS, // Guarded Control Stack access AccessType\_TRBE, // Trace Buffer access AccessType\_GPTW, // Granule Protection Table Walk AccessType\_HACDBS, // Access to the HACDBS structure AccessType\_HDBSS, // Access to entries in HDBSS AccessType\_TTW // Translation Table Walk }; J1.3.3.264 AddrTop

```
// AddrTop() // ========= // Return the MSB number of a virtual address in the stage 1 translation regime for "el". // If EL1 is using AArch64 then addresses from EL0 using AArch32 are zero-extended to 64 bits. AddressSize AddrTop(bits(64) address, boolean IsInstr, bits(2) el) assert HaveEL(el); regime = S1TranslationRegime(el); if ELUsingAArch32(regime) then // AArch32 translation regime. return 31; else if EffectiveTBI(address, IsInstr, el) == '1' then return 55; else return 63;
```

```
boolean tagchecked, // FEAT_MTE2: Access is tag checked boolean tagaccess, // FEAT_MTE: Access targets the tag bits boolean stzgm, // FEAT_MTE: Accesses that store Allocation tags to Device // memory are CONSTRAINED UNPREDICTABLE integer Rt, // Register named Rt in the instruction integer Rt2, // Register named Rt2 in the instruction integer Rs, // Register named Rs in the instruction integer Rs2, // Register named Rs2 in the instruction boolean ispair, // Access represents a Load/Store pair access boolean highestaddressfirst, // FEAT_LRCPC3: Highest address is accessed first boolean lowestaddress, // Is the current access the lowest address accessed by // this instruction MPAMinfo mpam // FEAT_MPAM: MPAM information
```

## J1.3.3.265 AddressSize

```
// AddressSize // ============ type AddressSize
```

```
= integer;
```

## J1.3.3.266 AlignmentEnforced // AlignmentEnforced() // =================== // For the active translation regime, determine if alignment is required boolean AlignmentEnforced() constant Regime regime = TranslationRegime(PSTATE.EL); bit A; case regime of when Regime\_EL30 A = SCTLR.A; when Regime\_EL3 A = SCTLR\_EL3.A; when Regime\_EL2 A = if ELUsingAArch32(EL2) then HSCTLR.A else SCTLR\_EL2.A; when Regime\_EL20 A = SCTLR\_EL2.A; when Regime\_EL10 A = if ELUsingAArch32(EL1) then SCTLR.A else SCTLR\_EL1.A; otherwise Unreachable(); return A == '1'; J1.3.3.267 Allocation // Allocation hints // ================ constant bits(2) MemHint\_No = '00'; // No Read-Allocate, No Write-Allocate constant bits(2) MemHint\_WA = '01'; // No Read-Allocate, Write-Allocate constant bits(2) MemHint\_RA = '10'; // Read-Allocate, No Write-Allocate constant bits(2) MemHint\_RWA = '11'; // Read-Allocate, Write-Allocate J1.3.3.268 BigEndian then

```
// BigEndian() // =========== boolean BigEndian(AccessType acctype) boolean bigend; if IsFeatureImplemented(FEAT_NV2) && acctype == AccessType_NV2 return SCTLR_EL2.EE == '1'; if UsingAArch32() then bigend = (PSTATE.E != '0'); elsif PSTATE.EL == EL0 then bigend = (SCTLR_ELx[].E0E != '0'); else bigend = (SCTLR_ELx[].EE != '0'); return bigend;
```

```
by all accesses
```

## J1.3.3.269 BigEndianReverse

```
// BigEndianReverse() // ================== bits(width) BigEndianReverse(bits(width) value) assert width IN {8, 16, 32, 64, 128, 256}; if width == 8 then return value; return Reverse(value, 8);
```

## J1.3.3.270 CacheOp

```
// CacheOp // ======= enumeration CacheOp { CacheOp_Clean, CacheOp_Invalidate, CacheOp_CleanInvalidate };
```

## J1.3.3.271 CacheOpScope

```
// CacheOpScope // ============ enumeration CacheOpScope { CacheOpScope_SetWay, CacheOpScope_PoU, CacheOpScope_PoC, CacheOpScope_PoE, CacheOpScope_PoP, CacheOpScope_PoDP, CacheOpScope_PoPA, CacheOpScope_PoPS, CacheOpScope_OuterCache, CacheOpScope_ALLU, CacheOpScope_ALLUIS };
```

## J1.3.3.272 CachePASpace

```
// CachePASpace // ============ enumeration CachePASpace { CPAS_NonSecure, CPAS_Any, // Applicable only for DC *SW / IC IALLU* in Root state: // match entries from any PA Space CPAS_RealmNonSecure, // Applicable only for DC *SW / IC IALLU* in Realm state: // match entries from Realm or Non-Secure PAS CPAS_Realm, CPAS_Root, CPAS_SystemAgent, // Applicable only for DC by PA: // match entries from the System Agent PAS CPAS_NonSecureProtected, // Applicable only for DC by PA: // match entries from the Non-Secure Protected PAS CPAS_NA6, // Reserved CPAS_NA7, // Reserved CPAS_SecureNonSecure, // Applicable only for DC *SW / IC IALLU* in Secure state:
```

## CPAS\_Secure }; J1.3.3.273 CacheType // CacheType // ========= enumeration CacheType { CacheType\_Data, CacheType\_Tag, CacheType\_Data\_Tag, CacheType\_Instruction }; J1.3.3.274 Cacheability // Cacheability attributes // ======================= constant bits(2) MemAttr\_NC = '00'; // Non-cacheable constant bits(2) MemAttr\_WT = '10'; // Write-through constant bits(2) MemAttr\_WB = '11'; // Write-back J1.3.3.275 CreateAccDescA32LSMD // CreateAccDescA32LSMD() // ====================== // Access descriptor for A32 loads/store multiple general purpose registers AccessDescriptor CreateAccDescA32LSMD(MemOp memop) AccessDescriptor accdesc = NewAccDesc(AccessType\_GPR); accdesc.read = memop == MemOp\_LOAD; accdesc.write = memop == MemOp\_STORE; accdesc.pan = TRUE; accdesc.a32lsmd = TRUE; return accdesc; J1.3.3.276 CreateAccDescASIMD tagchecked, tagchecked,

```
// CreateAccDescASIMD() // ==================== // Access descriptor for ASIMD&FP loads/stores AccessDescriptor CreateAccDescASIMD(MemOp memop, boolean nontemporal, boolean boolean privileged) constant boolean ispair = FALSE; return CreateAccDescASIMD(memop, nontemporal, tagchecked, privileged, ispair); // CreateAccDescASIMD() // ==================== AccessDescriptor CreateAccDescASIMD(MemOp memop, boolean nontemporal, boolean boolean privileged, boolean ispair) AccessDescriptor accdesc = NewAccDesc(AccessType_ASIMD); accdesc.nontemporal = nontemporal;
```

```
accdesc.el = if !privileged then EL0 else PSTATE.EL; accdesc.read = memop == MemOp_LOAD; accdesc.write = memop == MemOp_STORE; accdesc.ispair = ispair; accdesc.pan = TRUE; accdesc.streamingsve = InStreamingMode(); if (accdesc.streamingsve && boolean IMPLEMENTATION_DEFINED "No tag checking of SIMD&FP loads and stores in Streaming SVE mode") then accdesc.tagchecked = FALSE; else accdesc.tagchecked = tagchecked; return accdesc;
```

## J1.3.3.277 CreateAccDescASIMDAcqRel

```
// CreateAccDescASIMDAcqRel() // ========================== // Access descriptor for ASIMD&FP loads/stores with ordering semantics AccessDescriptor CreateAccDescASIMDAcqRel(MemOp memop, boolean tagchecked) AccessDescriptor accdesc = NewAccDesc(AccessType_ASIMD); accdesc.acqpc = memop == MemOp_LOAD; accdesc.relsc = memop == MemOp_STORE; accdesc.read = memop == MemOp_LOAD; accdesc.write = memop == MemOp_STORE; accdesc.pan = TRUE; accdesc.streamingsve = InStreamingMode(); if (accdesc.streamingsve && boolean IMPLEMENTATION_DEFINED "No tag checking of SIMD&FP loads and stores in Streaming SVE mode") then accdesc.tagchecked = FALSE; else accdesc.tagchecked = tagchecked; return accdesc;
```

## J1.3.3.278 CreateAccDescAT

```
// CreateAccDescAT() // ================= // Access descriptor for address translation operations AccessDescriptor CreateAccDescAT(SecurityState ss, bits(2) el, ATAccess ataccess) AccessDescriptor accdesc = NewAccDesc(AccessType_AT); accdesc.el = el; accdesc.ss = ss; if boolean IMPLEMENTATION_DEFINED "MPAM uses the EL targeted by the AT instruction" then accdesc.mpam = GenMPAMAtEL(AccessType_AT, el); case ataccess of when ATAccess_Read (accdesc.read, accdesc.write, accdesc.pan) = (TRUE, FALSE, FALSE); when ATAccess_ReadPAN (accdesc.read, accdesc.write, accdesc.pan) = (TRUE, FALSE, TRUE); when ATAccess_Write (accdesc.read, accdesc.write, accdesc.pan) = (FALSE, TRUE, FALSE); when ATAccess_WritePAN (accdesc.read, accdesc.write, accdesc.pan) = (FALSE, TRUE, TRUE); when ATAccess_Any (accdesc.read, accdesc.write, accdesc.pan) = (FALSE, FALSE, FALSE); return accdesc;
```

## J1.3.3.279 CreateAccDescAcqRel

```
// CreateAccDescAcqRel() // ===================== // Access descriptor for general purpose register loads/stores with ordering semantics AccessDescriptor CreateAccDescAcqRel(MemOp memop, boolean tagchecked, boolean acqsc) constant integer Rt = -1; return CreateAccDescAcqRel(memop, tagchecked, acqsc, Rt); AccessDescriptor CreateAccDescAcqRel(MemOp memop, boolean tagchecked, boolean acqsc, integer Rt) constant boolean ispair = FALSE; constant integer Rt2 = -1; return CreateAccDescAcqRel(memop, tagchecked, ispair, acqsc, Rt, Rt2); AccessDescriptor CreateAccDescAcqRel(MemOp memop, boolean tagchecked, boolean ispair, boolean acqsc, integer Rt, integer Rt2) AccessDescriptor accdesc = NewAccDesc(AccessType_GPR); accdesc.acqsc = acqsc; accdesc.relsc = memop == MemOp_STORE; accdesc.read = memop == MemOp_LOAD; accdesc.write = memop == MemOp_STORE; accdesc.pan = TRUE; accdesc.tagchecked = tagchecked; accdesc.ispair = ispair; accdesc.Rt = Rt; accdesc.Rt2 = Rt2; return accdesc;
```

## J1.3.3.280 CreateAccDescAtomicOp

```
// CreateAccDescAtomicOp() // ======================= // Access descriptor for atomic read-modify-write memory accesses AccessDescriptor CreateAccDescAtomicOp(MemAtomicOp modop, boolean acquire, boolean release, boolean tagchecked, boolean privileged, integer Rt, integer Rs) constant integer Rt2 = -1; constant integer Rs2 = -1; return CreateAccDescAtomicOp(modop, acquire, release, tagchecked, privileged, Rt, Rt2, Rs, AccessDescriptor CreateAccDescAtomicOp(MemAtomicOp modop, boolean acquire, boolean release, boolean tagchecked, boolean privileged, integer Rt, integer Rt2, integer Rs, integer Rs2) AccessDescriptor accdesc = NewAccDesc(AccessType_GPR); accdesc.acqsc = acquire; accdesc.el = if !privileged then EL0 else PSTATE.EL; accdesc.relsc = release; accdesc.atomicop = TRUE; accdesc.modop = modop; accdesc.read = TRUE; accdesc.write = TRUE; accdesc.pan = TRUE; accdesc.tagchecked = tagchecked; accdesc.Rs = Rs; accdesc.Rs2 = Rs2; accdesc.Rt = Rt; accdesc.Rt2 = Rt2;
```

```
Rs2);
```

return accdesc;

## J1.3.3.281 CreateAccDescDC

```
// CreateAccDescDC() // ================= // Access descriptor for data cache operations AccessDescriptor CreateAccDescDC(CacheRecord cache) AccessDescriptor accdesc = NewAccDesc(AccessType_DC); accdesc.cacheop = cache.cacheop; accdesc.cachetype = cache.cachetype; accdesc.opscope = cache.opscope; return accdesc;
```

## J1.3.3.282 CreateAccDescDCZero

```
IN {CacheType_Tag, CacheType_Data_Tag};
```

```
// CreateAccDescDCZero() // ===================== // Access descriptor for data cache zero operations AccessDescriptor CreateAccDescDCZero(CacheType cachetype) AccessDescriptor accdesc = NewAccDesc(AccessType_DCZero); accdesc.write = TRUE; accdesc.pan = TRUE; accdesc.tagchecked = cachetype == CacheType_Data; accdesc.tagaccess = cachetype accdesc.cachetype = cachetype; return accdesc;
```

## J1.3.3.283 CreateAccDescExLDST

```
// CreateAccDescExLDST() // ===================== // Access descriptor for general purpose register loads/stores with exclusive semantics AccessDescriptor CreateAccDescExLDST(MemOp memop, boolean acqrel, boolean tagchecked, boolean privileged) constant integer Rt = -1; return CreateAccDescExLDST(memop, acqrel, tagchecked, privileged, Rt); // CreateAccDescExLDST() // ===================== AccessDescriptor CreateAccDescExLDST(MemOp memop, boolean acqrel, boolean tagchecked, boolean privileged, integer Rt) constant boolean ispair = FALSE; constant integer Rt2 = -1; return CreateAccDescExLDST(memop, acqrel, tagchecked, privileged, ispair, Rt, Rt2); // CreateAccDescExLDST() // ===================== AccessDescriptor CreateAccDescExLDST(MemOp memop, boolean acqrel, boolean tagchecked, boolean privileged, boolean ispair, integer Rt, integer Rt2) AccessDescriptor accdesc = NewAccDesc(AccessType_GPR);
```

```
accdesc.acqsc = acqrel && memop == MemOp_LOAD; accdesc.relsc = acqrel && memop == MemOp_STORE; accdesc.exclusive = TRUE; accdesc.el = if !privileged then EL0 else PSTATE.EL; accdesc.read = memop == MemOp_LOAD; accdesc.write = memop == MemOp_STORE; accdesc.ispair = ispair; accdesc.pan = TRUE; accdesc.tagchecked = tagchecked; accdesc.Rt = Rt; accdesc.Rt2 = Rt2; return accdesc;
```

## J1.3.3.284 CreateAccDescFPAtomicOp

```
// CreateAccDescFPAtomicOp() // ========================= // Access descriptor for FP atomic read-modify-write memory accesses AccessDescriptor CreateAccDescFPAtomicOp(MemAtomicOp modop, boolean acquire, boolean release, boolean tagchecked) AccessDescriptor accdesc = NewAccDesc(AccessType_FP); accdesc.acqsc = acquire; accdesc.relsc = release; accdesc.atomicop = TRUE; accdesc.modop = modop; accdesc.read = TRUE; accdesc.write = TRUE; accdesc.pan = TRUE; accdesc.streamingsve = InStreamingMode(); if (accdesc.streamingsve && boolean IMPLEMENTATION_DEFINED "No tag checking of SIMD&FP loads and stores in Streaming SVE mode") then accdesc.tagchecked = FALSE; else accdesc.tagchecked = tagchecked; return accdesc;
```

## J1.3.3.285 CreateAccDescGCS

```
// CreateAccDescGCS() // ================== // Access descriptor for memory accesses to the Guarded Control Stack AccessDescriptor CreateAccDescGCS(MemOp memop, boolean privileged) AccessDescriptor accdesc = NewAccDesc(AccessType_GCS); accdesc.el = if !privileged then EL0 else PSTATE.EL; accdesc.read = memop == MemOp_LOAD; accdesc.write = memop == MemOp_STORE; return accdesc;
```

## J1.3.3.286 CreateAccDescGCSSS1

```
// CreateAccDescGCSSS1() // ===================== // Access descriptor for memory accesses to the Guarded Control Stack that switch stacks
```

```
AccessDescriptor CreateAccDescGCSSS1(boolean privileged) AccessDescriptor accdesc = NewAccDesc(AccessType_GCS); accdesc.el = if !privileged then EL0 else accdesc.atomicop = TRUE; accdesc.modop = MemAtomicOp_GCSSS1; accdesc.read = TRUE; accdesc.write = TRUE; return accdesc;
```

## J1.3.3.287 CreateAccDescGPR

```
// CreateAccDescGPR() // ================== // Access descriptor for general purpose register loads/stores // without exclusive or ordering semantics AccessDescriptor CreateAccDescGPR(MemOp memop, boolean nontemporal, boolean privileged, boolean tagchecked) constant integer Rt = -1; return CreateAccDescGPR(memop, nontemporal, privileged, tagchecked, Rt); AccessDescriptor CreateAccDescGPR(MemOp memop, boolean nontemporal, boolean privileged, boolean tagchecked, integer Rt) constant boolean ispair = FALSE; constant integer Rt2 = -1; return CreateAccDescGPR(memop, nontemporal, privileged, tagchecked, ispair, Rt, Rt2); AccessDescriptor CreateAccDescGPR(MemOp memop, boolean nontemporal, boolean privileged, boolean tagchecked, boolean ispair, integer Rt, integer AccessDescriptor accdesc = NewAccDesc(AccessType_GPR); accdesc.el = if !privileged then EL0 else PSTATE.EL; accdesc.nontemporal = nontemporal; accdesc.read = memop == MemOp_LOAD; accdesc.write = memop == MemOp_STORE; accdesc.pan = TRUE; accdesc.tagchecked = tagchecked; accdesc.Rt = Rt; accdesc.Rt2 = Rt2; accdesc.ispair = ispair; return accdesc;
```

```
Rt2) J1.3.3.288 CreateAccDescGPTW
```

```
NewAccDesc(AccessType_GPTW, accdesc_in.mpam);
```

```
// CreateAccDescGPTW() // =================== // Access descriptor for Granule Protection Table walks AccessDescriptor CreateAccDescGPTW(AccessDescriptor accdesc_in) AccessDescriptor accdesc = accdesc.el = accdesc_in.el; accdesc.ss = accdesc_in.ss; accdesc.read = TRUE; return accdesc;
```

```
PSTATE.EL;
```

## J1.3.3.289 CreateAccDescHACDBS

```
// CreateAccDescHACDBS() // ===================== // Access descriptor for memory accesses to the HACDBS structure. AccessDescriptor CreateAccDescHACDBS() AccessDescriptor accdesc = NewAccDesc(AccessType_HACDBS); accdesc.read = TRUE; return accdesc;
```

## J1.3.3.290 CreateAccDescHDBSS

```
// CreateAccDescHDBSS() // ==================== // Access descriptor for appending entries to the HDBSS AccessDescriptor CreateAccDescHDBSS(AccessDescriptor accdesc_in) AccessDescriptor accdesc = NewAccDesc(AccessType_HDBSS, accdesc_in.mpam); accdesc.el = accdesc_in.el; accdesc.ss = accdesc_in.ss; accdesc.write = TRUE; return accdesc;
```

## J1.3.3.291 CreateAccDescIC

```
// CreateAccDescIC() // ================= // Access descriptor for instruction cache operations AccessDescriptor CreateAccDescIC(CacheRecord cache) AccessDescriptor accdesc = NewAccDesc(AccessType_IC); accdesc.cacheop = cache.cacheop; accdesc.cachetype = cache.cachetype; accdesc.opscope = cache.opscope; return accdesc;
```

## J1.3.3.292 CreateAccDescIFetch

```
// CreateAccDescIFetch() // ===================== // Access descriptor for instruction fetches AccessDescriptor CreateAccDescIFetch() constant AccessDescriptor accdesc = NewAccDesc(AccessType_IFETCH); return accdesc;
```

## J1.3.3.293 CreateAccDescLDAcqPC

```
// CreateAccDescLDAcqPC() // ====================== // Access descriptor for general purpose register loads with local ordering semantics AccessDescriptor CreateAccDescLDAcqPC(boolean tagchecked, boolean acquire, integer Rt) constant boolean ispair = FALSE; constant integer Rt2 = -1; return CreateAccDescLDAcqPC(tagchecked, ispair, acquire, Rt, Rt2); AccessDescriptor CreateAccDescLDAcqPC(boolean tagchecked, boolean ispair, boolean acquire, integer Rt, integer Rt2) AccessDescriptor accdesc = NewAccDesc(AccessType_GPR); accdesc.acqpc = acquire; accdesc.read = TRUE; accdesc.pan = TRUE; accdesc.tagchecked = tagchecked; accdesc.ispair = ispair; accdesc.Rt = Rt; accdesc.Rt2 = Rt2; return accdesc;
```

```
J1.3.3.294 CreateAccDescLDGSTG // CreateAccDescLDGSTG() // ===================== // Access descriptor for tag memory loads/stores AccessDescriptor CreateAccDescLDGSTG(MemOp memop, boolean stzgm, integer Rt) constant boolean ispair = FALSE; constant integer Rt2 = -1; return CreateAccDescLDGSTG(memop, stzgm, ispair, Rt, Rt2); // CreateAccDescLDGSTG() // ===================== AccessDescriptor CreateAccDescLDGSTG(MemOp memop, boolean stzgm, boolean ispair, integer Rt, integer Rt2) AccessDescriptor accdesc = NewAccDesc(AccessType_GPR); accdesc.read = memop == MemOp_LOAD; accdesc.write = memop == MemOp_STORE; accdesc.pan = TRUE; accdesc.tagaccess = TRUE; accdesc.stzgm = stzgm; accdesc.ispair = ispair; accdesc.Rt = Rt; accdesc.Rt2 = Rt2; return accdesc; J1.3.3.295 CreateAccDescLOR semantics
```

```
// CreateAccDescLOR() // ================== // Access descriptor for general purpose register loads/stores with limited ordering AccessDescriptor CreateAccDescLOR(MemOp memop, boolean tagchecked, boolean acqsc, integer Rt) AccessDescriptor accdesc = NewAccDesc(AccessType_GPR);
```

```
accdesc.acqsc = acqsc; accdesc.relsc = memop == MemOp_STORE; accdesc.limitedordered = TRUE; accdesc.read = memop == MemOp_LOAD; accdesc.write = memop == MemOp_STORE; accdesc.pan = TRUE; accdesc.tagchecked = tagchecked; accdesc.Rt = Rt; return accdesc;
```

## J1.3.3.296 CreateAccDescLS64

```
// CreateAccDescLS64() // =================== // Access descriptor for accelerator-supporting memory accesses AccessDescriptor CreateAccDescLS64(MemOp memop, boolean withstatus, boolean tagchecked) AccessDescriptor accdesc = NewAccDesc(AccessType_GPR); accdesc.read = memop == MemOp_LOAD; accdesc.write = memop == MemOp_STORE; accdesc.pan = TRUE; accdesc.ls64 = TRUE; accdesc.withstatus = withstatus; accdesc.tagchecked = tagchecked; return accdesc;
```

## J1.3.3.297 CreateAccDescMOPS

```
// CreateAccDescMOPS() // =================== // Access descriptor for data memory copy and set instructions AccessDescriptor CreateAccDescMOPS(MemOp memop, boolean privileged, boolean nontemporal) AccessDescriptor accdesc = NewAccDesc(AccessType_GPR); accdesc.el = if !privileged then EL0 else PSTATE.EL; accdesc.nontemporal = nontemporal; accdesc.read = memop == MemOp_LOAD; accdesc.write = memop == MemOp_STORE; accdesc.pan = TRUE; accdesc.mops = TRUE; accdesc.tagchecked = TRUE; return accdesc;
```

## J1.3.3.298 CreateAccDescNV2

```
// CreateAccDescNV2() // ================== // Access descriptor nested virtualization memory indirection loads/stores AccessDescriptor CreateAccDescNV2(MemOp memop) AccessDescriptor accdesc = NewAccDesc(AccessType_NV2); accdesc.el = EL2; accdesc.ss = SecurityStateAtEL(EL2); accdesc.read = memop == MemOp_LOAD; accdesc.write = memop == MemOp_STORE; return accdesc;
```

## J1.3.3.299 CreateAccDescRCW

```
// CreateAccDescRCW() // ================== // Access descriptor for atomic read-check-write memory accesses AccessDescriptor CreateAccDescRCW(MemAtomicOp modop, boolean soft, boolean acquire, boolean release, boolean tagchecked, integer Rt, integer Rs) constant integer Rt2 = -1; constant integer Rs2 = -1; return CreateAccDescRCW(modop, soft, acquire, release, tagchecked, Rt, Rt2, Rs, Rs2); AccessDescriptor CreateAccDescRCW(MemAtomicOp modop, boolean soft, boolean acquire, boolean release, boolean tagchecked, integer Rt, integer Rt2, integer Rs, integer Rs2) AccessDescriptor accdesc = NewAccDesc(AccessType_GPR); accdesc.acqsc = acquire; accdesc.relsc = release; accdesc.rcw = TRUE; accdesc.rcws = soft; accdesc.atomicop = TRUE; accdesc.modop = modop; accdesc.read = TRUE; accdesc.write = TRUE; accdesc.pan = TRUE; accdesc.tagchecked = tagchecked; accdesc.Rt = Rt; accdesc.Rt2 = Rt2; accdesc.Rs = Rs; accdesc.Rs2 = Rs2; return accdesc;
```

```
// CreateAccDescS1TTW() // ==================== // Access descriptor for stage 1 translation table walks AccessDescriptor CreateAccDescS1TTW(boolean toplevel, VARange varange, AccessDescriptor accdesc_in) AccessDescriptor accdesc = NewAccDesc(AccessType_TTW, accdesc_in.mpam); accdesc.el = accdesc_in.el; accdesc.ss = accdesc_in.ss; accdesc.read = TRUE; accdesc.toplevel = toplevel; accdesc.varange = varange; return accdesc;
```

```
// CreateAccDescS2TTW() // ==================== // Access descriptor for stage 2 translation table walks AccessDescriptor CreateAccDescS2TTW(AccessDescriptor accdesc_in) AccessDescriptor accdesc = accdesc.el = accdesc_in.el; accdesc.ss = accdesc_in.ss;
```

```
J1.3.3.300 CreateAccDescS1TTW J1.3.3.301 CreateAccDescS2TTW NewAccDesc(AccessType_TTW, accdesc_in.mpam);
```

```
accdesc.read = TRUE; return accdesc;
```

## J1.3.3.302 CreateAccDescSME

```
// CreateAccDescSME() // ================== // Access descriptor for SME loads/stores AccessDescriptor CreateAccDescSME(MemOp memop, boolean nontemporal, boolean contiguous, boolean tagchecked) AccessDescriptor accdesc = NewAccDesc(AccessType_SME); accdesc.nontemporal = nontemporal; accdesc.read = memop == MemOp_LOAD; accdesc.write = memop == MemOp_STORE; accdesc.pan = TRUE; accdesc.contiguous = contiguous; accdesc.streamingsve = TRUE; if boolean IMPLEMENTATION_DEFINED "No tag checking of SME LDR & STR instructions" then accdesc.tagchecked = FALSE; else accdesc.tagchecked = tagchecked; return accdesc;
```

## J1.3.3.303 CreateAccDescSPE

```
// CreateAccDescSPE() // ================== // Access descriptor for memory accesses by Statistical Profiling unit AccessDescriptor CreateAccDescSPE(SecurityState owning_ss, bits(2) owning_el) constant MPAMinfo mpaminfo = GenMPAMAtEL(AccessType_SPE, owning_el); AccessDescriptor accdesc = NewAccDesc(AccessType_SPE, mpaminfo); accdesc.el = owning_el; accdesc.ss = owning_ss; accdesc.write = TRUE; return accdesc;
```

## J1.3.3.304 CreateAccDescSTGMOPS

```
// CreateAccDescSTGMOPS() // ====================== // Access descriptor for tag memory set instructions AccessDescriptor CreateAccDescSTGMOPS(boolean privileged, boolean nontemporal) AccessDescriptor accdesc = NewAccDesc(AccessType_GPR); accdesc.el = if !privileged then EL0 else PSTATE.EL; accdesc.nontemporal = nontemporal; accdesc.write = TRUE; accdesc.pan = TRUE; accdesc.mops = TRUE; accdesc.tagaccess = TRUE; return accdesc;
```

## J1.3.3.305 CreateAccDescSVE

```
// CreateAccDescSVE() // ================== // Access descriptor for general SVE loads/stores AccessDescriptor CreateAccDescSVE(MemOp memop, boolean nontemporal, boolean contiguous, boolean tagchecked) constant boolean predicated = FALSE; return CreateAccDescSVE(memop, nontemporal, contiguous, predicated, tagchecked); AccessDescriptor CreateAccDescSVE(MemOp memop, boolean nontemporal, boolean contiguous, boolean predicated, boolean tagchecked) AccessDescriptor accdesc = NewAccDesc(AccessType_SVE); accdesc.nontemporal = nontemporal; accdesc.read = memop == MemOp_LOAD; accdesc.write = memop == MemOp_STORE; accdesc.pan = TRUE; accdesc.contiguous = contiguous; accdesc.streamingsve = InStreamingMode(); if (accdesc.streamingsve && boolean IMPLEMENTATION_DEFINED "No tag checking of SIMD&FP loads and stores in Streaming SVE mode") then accdesc.tagchecked = FALSE; else accdesc.tagchecked = tagchecked; accdesc.predicated = predicated; return accdesc;
```

## J1.3.3.306 CreateAccDescSVEFF

```
// CreateAccDescSVEFF() // ==================== // Access descriptor for first-fault SVE loads AccessDescriptor CreateAccDescSVEFF(boolean contiguous, boolean tagchecked) AccessDescriptor accdesc = NewAccDesc(AccessType_SVE); accdesc.read = TRUE; accdesc.pan = TRUE; accdesc.firstfault = TRUE; accdesc.first = TRUE; accdesc.contiguous = contiguous; accdesc.streamingsve = InStreamingMode(); if (accdesc.streamingsve && boolean IMPLEMENTATION_DEFINED "No tag checking of SIMD&FP loads and stores in Streaming SVE mode") then accdesc.tagchecked = FALSE; else accdesc.tagchecked = tagchecked; accdesc.predicated = TRUE; return accdesc;
```

## J1.3.3.307 CreateAccDescSVENF

```
// CreateAccDescSVENF() // ==================== // Access descriptor for non-fault SVE loads AccessDescriptor CreateAccDescSVENF(boolean contiguous, boolean tagchecked) AccessDescriptor accdesc = NewAccDesc(AccessType_SVE);
```

```
accdesc.read = TRUE; accdesc.pan = TRUE; accdesc.nonfault = TRUE; accdesc.contiguous = contiguous; accdesc.streamingsve = InStreamingMode(); if (accdesc.streamingsve && boolean IMPLEMENTATION_DEFINED "No tag checking of SIMD&FP loads and stores in Streaming SVE mode") then accdesc.tagchecked = FALSE; else accdesc.tagchecked = tagchecked; accdesc.predicated = TRUE; return accdesc;
```

## J1.3.3.308 CreateAccDescTRBE // CreateAccDescTRBE() // =================== // Access descriptor for memory accesses by Trace Buffer Unit AccessDescriptor CreateAccDescTRBE(SecurityState owning\_ss, bits(2) owning\_el) MPAMinfo mpam; if SelfHostedTraceEnabled() then mpam = GenMPAMAtEL(AccessType\_TRBE, owning\_el); else mpam = GenMPAMCurEL(AccessType\_TRBE); AccessDescriptor accdesc = NewAccDesc(AccessType\_TRBE, mpam); accdesc.el = owning\_el; accdesc.ss = owning\_ss; accdesc.write = TRUE; return accdesc; J1.3.3.309 CreateAccDescTTEUpdate // CreateAccDescTTEUpdate() // ======================== // Access descriptor for translation table entry HW update AccessDescriptor CreateAccDescTTEUpdate(AccessDescriptor accdesc\_in) AccessDescriptor accdesc = NewAccDesc(AccessType\_TTW, accdesc\_in.mpam); accdesc.el = accdesc\_in.el; accdesc.ss = accdesc\_in.ss; accdesc.atomicop = TRUE; accdesc.modop = MemAtomicOp\_CAS; accdesc.read = TRUE; accdesc.write = TRUE; return accdesc; J1.3.3.310 DataMemoryBarrier // DataMemoryBarrier() // =================== DataMemoryBarrier(MBReqDomain domain, MBReqTypes types);

## J1.3.3.311 DataSynchronizationBarrier

```
// DataSynchronizationBarrier() // ============================ DataSynchronizationBarrier(MBReqDomain domain, MBReqTypes types, boolean
```

## J1.3.3.312 DeviceType

```
// DeviceType // ========== // Extended memory types for Device memory. enumeration DeviceType {DeviceType_GRE, DeviceType_nGRE, DeviceType_nGnRE, DeviceType_nGnRnE};
```

## J1.3.3.313 EffectiveMTX

```
// EffectiveMTX() // ============== // Returns the effective MTX in the AArch64 stage 1 translation regime for "el". bit EffectiveMTX(bits(64) address, boolean is_instr, bits(2) el) bit mtx; assert HaveEL(el); regime = S1TranslationRegime(el); assert(!ELUsingAArch32(regime)); if is_instr then mtx = '0'; else case regime of when EL1 mtx = if address<55> == '1' then TCR_EL1.MTX1 else TCR_EL1.MTX0; when EL2 if IsFeatureImplemented(FEAT_VHE) && ELIsInHost(el) then mtx = if address<55> == '1' then TCR_EL2.MTX1 else TCR_EL2.MTX0; else mtx = TCR_EL2.MTX; when EL3 mtx = TCR_EL3.MTX; return mtx;
```

## J1.3.3.314 EffectiveTBI

```
// EffectiveTBI() // ============== // Returns the effective TBI in the AArch64 stage 1 translation regime for "el". bit EffectiveTBI(bits(64) address, boolean IsInstr, bits(2) el) bit tbi; bit tbid; assert HaveEL(el); regime = S1TranslationRegime(el); assert(!ELUsingAArch32(regime)); case regime of when EL1 tbi = if address<55> == '1' then TCR_EL1.TBI1 else TCR_EL1.TBI0; if IsFeatureImplemented(FEAT_PAuth) then tbid = if address<55> == '1' then TCR_EL1.TBID1 else TCR_EL1.TBID0;
```

```
nXS);
```

```
when EL2 if IsFeatureImplemented(FEAT_VHE) && ELIsInHost(el) then tbi = if address<55> == '1' then TCR_EL2.TBI1 else TCR_EL2.TBI0; if IsFeatureImplemented(FEAT_PAuth) then tbid = if address<55> == '1' then TCR_EL2.TBID1 else else tbi = TCR_EL2.TBI; if IsFeatureImplemented(FEAT_PAuth) then tbid = TCR_EL2.TBID; when EL3 tbi = TCR_EL3.TBI; if IsFeatureImplemented(FEAT_PAuth) then tbid = TCR_EL3.TBID; return (if (tbi == '1' && (!IsFeatureImplemented(FEAT_PAuth) || tbid == '0' || !IsInstr)) then '1' else '0');
```

```
TCR_EL2.TBID0; J1.3.3.315 EffectiveTCMA // EffectiveTCMA() // =============== // Returns the effective TCMA of a virtual address in the stage 1 translation regime for "el". bit EffectiveTCMA(bits(64) address, bits(2) el) bit tcma; assert HaveEL(el); regime = S1TranslationRegime(el); assert(!ELUsingAArch32(regime)); case regime of when EL1 tcma = if address<55> == '1' then TCR_EL1.TCMA1 else TCR_EL1.TCMA0; when EL2 if IsFeatureImplemented(FEAT_VHE) && ELIsInHost(el) then tcma = if address<55> == '1' then TCR_EL2.TCMA1 else TCR_EL2.TCMA0; else tcma = TCR_EL2.TCMA; when EL3 tcma = TCR_EL3.TCMA; return tcma; J1.3.3.316 ErrorState // ErrorState // ========== // The allowed error states that can be returned by memory and used by the PE. enumeration ErrorState {ErrorState_UC, // Uncontainable ErrorState_UEU, // Unrecoverable state ErrorState_UEO, // Restartable state ErrorState_UER, // Recoverable state ErrorState_CE}; // Corrected J1.3.3.317 Fault // Fault // ===== // Fault types. enumeration Fault {Fault_None, Fault_AccessFlag, Fault_Alignment,
```

```
Fault_Background, Fault_Domain, Fault_Permission, Fault_Translation, Fault_AddressSize, Fault_SyncExternal, Fault_SyncParity, Fault_SyncParityOnWalk, Fault_GPCFOnWalk, Fault_GPCFOnOutput, Fault_AsyncParity, Fault_AsyncExternal, Fault_TagCheck, Fault_Debug, Fault_TLBConflict, Fault_BranchTarget, Fault_Lockdown, Fault_Exclusive, Fault_ICacheMaint};
```

```
// FullAddress // =========== // Physical or Intermediate Physical Address type. // Although AArch32 only has access to 40 bits of physical or intermediate physical // the full address type has 56 bits to allow interprocessing with AArch64. // The maximum physical or intermediate physical address size is IMPLEMENTATION DEFINED, // but never exceeds 56 bits.
```

```
Fault_SyncExternalOnWalk, Fault_HWUpdateAccessFlag, J1.3.3.318 FaultRecord // FaultRecord // =========== // Fields that relate only to Faults. type FaultRecord is ( Fault statuscode, // Fault Status AccessDescriptor accessdesc, // Details of the faulting access bits(64) vaddress, // Faulting virtual address FullAddress ipaddress, // Intermediate physical address FullAddress paddress, // Physical address GPCFRecord gpcf, // Granule Protection Check Fault record boolean gpcfs2walk, // GPC for a stage 2 translation table walk boolean s2fs1walk, // Is on a Stage 1 translation table walk boolean write, // TRUE for a write, FALSE for a read boolean s1tagnotdata, // TRUE for a fault due to tag not accessible at stage 1. boolean tagaccess, // TRUE for a fault due to NoTagAccess permission. integer level, // For translation, access flag and Permission faults bit extflag, // IMPLEMENTATION DEFINED syndrome for External aborts boolean secondstage, // Is a Stage 2 abort boolean assuredonly, // Stage 2 Permission fault due to AssuredOnly attribute boolean toplevel, // Stage 2 Permission fault due to TopLevel boolean overlay, // Fault due to overlay permissions boolean dirtybit, // Fault due to dirty state bits(4) domain, // Domain number, AArch32 only ErrorState merrorstate, // Incoming error state from memory boolean hdbssf, // Fault caused by HDBSS WatchpointInfo watchptinfo, // Watchpoint related fields bits(4) debugmoe // Debug method of entry, from AArch32 only ) J1.3.3.319 FullAddress address space,
```

```
type FullAddress is ( PASpace paspace, bits(56) address )
```

## J1.3.3.320 GPCF

```
// GPCF // ==== // Possible Granule Protection Check Fault reasons enumeration GPCF { GPCF_None, // No fault GPCF_AddressSize, // GPT address size fault GPCF_Walk, // GPT walk fault GPCF_EABT, // Synchronous External abort on GPT fetch GPCF_Fail // Granule protection fault };
```

## J1.3.3.321 GPCFRecord

```
// GPCFRecord // ========== // Full details of a Granule Protection Check Fault type GPCFRecord is ( GPCF gpf, integer level )
```

## J1.3.3.322 Hint\_Prefetch

```
// Hint_Prefetch() // =============== // Signals the memory system that memory accesses of type HINT to or from the specified address are // likely in the near future. The memory system may take some action to speed up the memory // accesses when they do occur, such as pre-loading the specified address into one or more // caches as indicated by the innermost cache level target (0=L1, 1=L2, etc) and non-temporal hint // stream. Any or all prefetch hints may be treated as a NOP. A prefetch hint must not cause a // synchronous abort due to Alignment or Translation faults and the like. Its only effect on // software-visible state should be on caches and TLBs associated with address, which must be // accessible by reads, writes or execution, as defined in the translation regime of the current // Exception level. It is guaranteed not to access Device memory. // A Prefetch_EXEC hint must not result in an access that could not be performed by a speculative // instruction fetch, therefore if all associated MMUs are disabled, then it cannot access any // memory location that cannot be accessed by instruction fetches. Hint_Prefetch(bits(64) address, PrefetchHint hint, integer target, boolean stream);
```

## J1.3.3.323 Hint\_RangePrefetch

```
// Hint_RangePrefetch() // ==================== // Signals the memory system that data memory accesses from a specified range // of addresses are likely to occur in the near future. The memory system can // respond by taking actions that are expected to speed up the memory accesses // when they do occur, such as preloading the locations within the specified // address ranges into one or more caches.
```

```
Hint_RangePrefetch(bits(64) address, integer length, integer stride, integer count, integer reuse, bits(6) operation);
```

## J1.3.3.324 IsContiguousSVEAccess

```
// IsContiguousSVEAccess() // ======================= // Return TRUE if memory access is contiguous load/stores in an SVE mode. boolean IsContiguousSVEAccess(AccessDescriptor accdesc) return (IsFeatureImplemented(FEAT_SVE) && accdesc.acctype == AccessType_SVE && accdesc.contiguous);
```

## J1.3.3.325 IsRelaxedWatchpointAccess

```
// IsRelaxedWatchpointAccess() // =========================== // Return TRUE if memory access is one of -// -SIMD&FP load/store instruction when the PE is in Streaming SVE mode // -SVE contiguous vector load/store instruction. // -SME load/store instruction boolean IsRelaxedWatchpointAccess(AccessDescriptor accdesc) return (IsContiguousSVEAccess(accdesc) || IsSMEAccess(accdesc) || (IsSIMDFPAccess(accdesc) && InStreamingMode()));
```

## J1.3.3.326 IsSIMDFPAccess

```
// IsSIMDFPAccess() // ================ // Return TRUE if access is SIMD&FP. boolean IsSIMDFPAccess(AccessDescriptor accdesc) return accdesc.acctype == AccessType_ASIMD;
```

## J1.3.3.327 IsSMEAccess

```
// IsSMEAccess() // ============= // Return TRUE if access is of SME load/stores. boolean IsSMEAccess(AccessDescriptor accdesc) return IsFeatureImplemented(FEAT_SME) && accdesc.acctype == AccessType_SME;
```

## J1.3.3.328 IsWatchpointableAccess

```
// IsWatchpointableAccess() // ======================== // Return TRUE if access should be checked for watchpoints. boolean IsWatchpointableAccess(AccessDescriptor accdesc) return (!(accdesc.acctype IN {AccessType_IFETCH, AccessType_TTW, AccessType_DC, AccessType_IC, AccessType_SPE,
```

```
AccessType_TRBE, AccessType_AT}) || (accdesc.acctype == AccessType_DC && accdesc.cacheop == CacheOp_Invalidate && (!UsingAArch32() || (boolean IMPLEMENTATION_DEFINED "DCIMVAC generates watchpoint"))));
```

## J1.3.3.329 MBReqDomain

```
// MBReqDomain // =========== // Memory barrier domain. enumeration MBReqDomain {MBReqDomain_Nonshareable, MBReqDomain_InnerShareable, MBReqDomain_OuterShareable, MBReqDomain_FullSystem};
```

## J1.3.3.330 MBReqTypes

```
// MBReqTypes // ========== // Memory barrier read/write. enumeration MBReqTypes {MBReqTypes_Reads, MBReqTypes_Writes, MBReqTypes_All};
```

## J1.3.3.331 MemAtomicOp

```
// MemAtomicOp // =========== // Atomic data processing instruction enumeration MemAtomicOp { MemAtomicOp_GCSSS1, MemAtomicOp_ADD, MemAtomicOp_BIC, MemAtomicOp_EOR, MemAtomicOp_ORR, MemAtomicOp_SMAX, MemAtomicOp_SMIN, MemAtomicOp_UMAX, MemAtomicOp_UMIN, MemAtomicOp_SWP, MemAtomicOp_CAS, MemAtomicOp_FPADD, MemAtomicOp_FPMAX, MemAtomicOp_FPMIN, MemAtomicOp_FPMAXNM, MemAtomicOp_FPMINNM, MemAtomicOp_BFADD, MemAtomicOp_BFMAX, MemAtomicOp_BFMIN, MemAtomicOp_BFMAXNM, MemAtomicOp_BFMINNM };
```

```
types.
```

## J1.3.3.332 MemAttrHints

```
// MemAttrHints // ============ // Attributes and hints for Normal memory. type MemAttrHints is (
```

```
bits(2) attrs, // See MemAttr_*, Cacheability attributes bits(2) hints, // See MemHint_*, Allocation hints boolean transient )
```

## J1.3.3.333 MemOp

```
// MemOp // ===== // Memory access instruction types. enumeration MemOp {MemOp_LOAD, MemOp_STORE, MemOp_PREFETCH};
```

## J1.3.3.334 MemType

```
// MemType // ======= // Basic memory types. enumeration
```

```
MemType {MemType_Normal, MemType_Device};
```

## J1.3.3.335 Memory

```
// Memory Tag type // =============== enumeration MemTagType { MemTag_AllocationTagged, MemTag_CanonicallyTagged, MemTag_Untagged };
```

## J1.3.3.336 MemoryAttributes

```
// MemoryAttributes // ================ // Memory attributes descriptor type MemoryAttributes is ( MemType memtype, DeviceType device, // For Device memory types MemAttrHints inner, // Inner hints and attributes MemAttrHints outer, // Outer hints and attributes Shareability shareability, // Shareability attribute MemTagType tags, // MTE tag type for this memory. boolean notagaccess, // Allocation Tag access permission bit xs // XS attribute )
```

## J1.3.3.337 NewAccDesc

```
// NewAccDesc() // ============ // Create a new AccessDescriptor with initialised fields AccessDescriptor NewAccDesc(AccessType acctype) constant MPAMinfo mpaminfo = GenMPAMCurEL(acctype); return NewAccDesc(acctype, mpaminfo);
```

```
AccessDescriptor NewAccDesc(AccessType acctype, MPAMinfo mpam) AccessDescriptor accdesc; accdesc.acctype = acctype; accdesc.el = PSTATE.EL; accdesc.ss = SecurityStateAtEL(PSTATE.EL); accdesc.acqsc = FALSE; accdesc.acqpc = FALSE; accdesc.relsc = FALSE; accdesc.limitedordered = FALSE; accdesc.exclusive = FALSE; accdesc.rcw = FALSE; accdesc.rcws = FALSE; accdesc.atomicop = FALSE; accdesc.nontemporal = FALSE; accdesc.read = FALSE; accdesc.write = FALSE; accdesc.pan = FALSE; accdesc.nonfault = FALSE; accdesc.firstfault = FALSE; accdesc.first = FALSE; accdesc.contiguous = FALSE; accdesc.predicated = FALSE; accdesc.streamingsve = FALSE; accdesc.ls64 = FALSE; accdesc.withstatus = FALSE; accdesc.mops = FALSE; accdesc.a32lsmd = FALSE; accdesc.tagchecked = FALSE; accdesc.tagaccess = FALSE; accdesc.stzgm = FALSE; accdesc.mpam = mpam; accdesc.Rs = -1; accdesc.Rs2 = -1; accdesc.Rt = -1; accdesc.Rt2 = -1; accdesc.ispair = FALSE; accdesc.highestaddressfirst = FALSE; accdesc.lowestaddress = TRUE; return accdesc;
```

## J1.3.3.338 PASpace

```
// PASpace // ======= // Physical address spaces enumeration PASpace { PAS_Root, PAS_SystemAgent, PAS_NonSecureProtected, PAS_NA6, PAS_NA7, PAS_Realm, PAS_Secure, PAS_NonSecure };
```

## J1.3.3.339 Permissions

```
// Reserved // Reserved
```

```
// Permissions // =========== // Access Control bits in translation table descriptors type Permissions is ( bits(2) ap_table, // Stage 1 hierarchical access permissions bit xn_table, // Stage 1 hierarchical execute-never for single bit pxn_table, // Stage 1 hierarchical privileged execute-never bit uxn_table, // Stage 1 hierarchical unprivileged execute-never bits(3) ap, // Stage 1 access permissions bit xn, // Stage 1 execute-never for single EL regimes bit uxn, // Stage 1 unprivileged execute-never bit pxn, // Stage 1 privileged execute-never bits(4) ppi, // Stage 1 privileged indirect permissions bits(4) upi, // Stage 1 unprivileged indirect permissions bit ndirty, // Stage 1 dirty state for indirect permissions scheme bits(4) s2pi, // Stage 2 indirect permissions bit s2dirty, // Stage 2 dirty state bits(4) po_index, // Stage 1 overlay permissions index bits(4) s2po_index, // Stage 2 overlay permissions index bits(2) s2ap, // Stage 2 access permissions bit s2tag_na, // Stage 2 tag access bit s2xnx, // Stage 2 extended execute-never bit dbm, // Dirty bit management bit s2xn // Stage 2 execute-never )
```

```
// PhysMemWrite() // ============== // Writes the value to memory, and returns the status of the write. // If there is an External abort on the write, the PhysMemRetStatus indicates // Otherwise the statuscode of PhysMemRetStatus is Fault_None.
```

## EL regimes J1.3.3.340 PhysMemRead // PhysMemRead() // ============= // Returns the value read from memory, and a status. // Returned value is UNKNOWN if an External abort occurred while reading the // memory. // Otherwise the PhysMemRetStatus statuscode is Fault\_None. (PhysMemRetStatus, bits(8*size)) PhysMemRead(AddressDescriptor desc, integer size, AccessDescriptor accdesc); J1.3.3.341 PhysMemRetStatus // PhysMemRetStatus // ================ // Fields that relate only to return values of PhysMem functions. type PhysMemRetStatus is ( Fault statuscode, // Fault Status bit extflag, // IMPLEMENTATION DEFINED syndrome for External aborts ErrorState merrorstate, // Optional error state returned on a physical memory access bits(64) store64bstatus // Status of 64B store ) J1.3.3.342 PhysMemWrite this.

```
PhysMemRetStatus PhysMemWrite(AddressDescriptor desc, integer size, AccessDescriptor accdesc, bits(8*size) value); J1.3.3.343 PrefetchHint // PrefetchHint // ============ // Prefetch hint types. enumeration PrefetchHint {Prefetch_READ, Prefetch_WRITE, Prefetch_EXEC}; J1.3.3.344 S1AccessControls // S1AccessControls // ================ // Effective access controls defined by stage 1 translation type S1AccessControls is ( bit r, // Stage 1 base read permission bit w, // Stage 1 base write permission bit x, // Stage 1 base execute permission bit gcs, // Stage 1 GCS permission boolean overlay, // Stage 1 FEAT_S1POE overlay applies bit or, // Stage 1 FEAT_S1POE overlay read permission bit ow, // Stage 1 FEAT_S1POE overlay write permission bit ox, // Stage 1 FEAT_S1POE overlay execute permission bit wxn // Stage 1 write permission implies execute-never ) J1.3.3.345 S2AccessControls // S2AccessControls // ================ // Effective access controls defined by stage 2 translation type S2AccessControls is ( bit r, // Stage 2 read permission. bit w, // Stage 2 write permission. bit x, // Stage 2 execute permission. bit r_rcw, // Stage 2 Read perms for RCW instruction. bit w_rcw, // Stage 2 Write perms for RCW instruction. bit r_mmu, // Stage 2 Read perms for TTW data. bit w_mmu, // Stage 2 Write perms for TTW data. bit toplevel0, // IPA as top level table for TTBR0_EL1. bit toplevel1, // IPA as top level table for TTBR1_EL1. boolean overlay, // Overlay enable bit or, // Stage 2 overlay read permission. bit ow, // Stage 2 overlay write permission. bit ox, // Stage 2 overlay execute permission. bit or_rcw, // Stage 2 overlay Read perms for RCW instruction. bit ow_rcw, // Stage 2 overlay Write perms for RCW instruction. bit or_mmu, // Stage 2 overlay Read perms for TTW data. bit ow_mmu, // Stage 2 overlay Write perms for TTW data. )
```

## J1.3.3.346 Shareability

```
// Shareability // ============ enumeration Shareability { Shareability_NSH, Shareability_ISH, Shareability_OSH };
```

## J1.3.3.347 SpeculativeStoreBypassBarrierToPA

```
// SpeculativeStoreBypassBarrierToPA()
```

```
// =================================== SpeculativeStoreBypassBarrierToPA();
```

## J1.3.3.348 SpeculativeStoreBypassBarrierToVA

```
// SpeculativeStoreBypassBarrierToVA() // =================================== SpeculativeStoreBypassBarrierToVA();
```

## J1.3.3.349 Tag

```
// Tag Granule size // ================ constant integer LOG2_TAG_GRANULE = 4; constant integer TAG_GRANULE = 1 << LOG2_TAG_GRANULE;
```

## J1.3.3.350 VARange

```
// VARange // ======= // Virtual address ranges enumeration VARange { VARange_LOWER, VARange_UPPER };
```

## J1.3.3.351 AltPARTIDSpace

```
// AltPARTIDSpace() // ================ // From the Security state, EL and ALTSP configuration, determine // whether to primary space or the alt space is selected and which // PARTID space is the alternative space. Return that alternative // PARTID space if selected or the primary space if not. PARTIDSpaceType AltPARTIDSpace(bits(2) el, SecurityState security, PARTIDSpaceType primaryPIDSpace) case security of when SS_NonSecure
```

```
assert el != EL3; return primaryPIDSpace; when SS_Secure assert el != EL3; if primaryPIDSpace == PIDSpace_NonSecure then return primaryPIDSpace; return AltPIDSecure(el, primaryPIDSpace); when SS_Root assert el == EL3; if MPAM3_EL3.ALTSP_EL3 == '1' then if MPAM3_EL3.RT_ALTSP_NS == '1' then return PIDSpace_NonSecure; else return PIDSpace_Secure; else return primaryPIDSpace; when SS_Realm assert el != EL3; return AltPIDRealm(el, primaryPIDSpace); otherwise Unreachable();
```

## J1.3.3.352 AltPIDRealm

```
// AltPIDRealm() // ============= // Compute PARTID space as either the primary PARTID space or // alternative PARTID space in the Realm Security state. // Helper for AltPARTIDSpace. PARTIDSpaceType AltPIDRealm(bits(2) el, PARTIDSpaceType primaryPIDSpace) PARTIDSpaceType PIDSpace = primaryPIDSpace; case el of when EL0 if ELIsInHost(EL0) then if !UsePrimarySpaceEL2() then PIDSpace = PIDSpace_NonSecure; elsif !UsePrimarySpaceEL10() then PIDSpace = PIDSpace_NonSecure; when EL1 if !UsePrimarySpaceEL10() then PIDSpace = PIDSpace_NonSecure; when EL2 if !UsePrimarySpaceEL2() then PIDSpace = PIDSpace_NonSecure; otherwise Unreachable(); return PIDSpace;
```

## J1.3.3.353 AltPIDSecure

```
// AltPIDSecure() // ============== // Compute PARTID space as either the primary PARTID space or // alternative PARTID space in the Secure Security state. // Helper for AltPARTIDSpace. PARTIDSpaceType AltPIDSecure(bits(2) el, PARTIDSpaceType primaryPIDSpace) PARTIDSpaceType PIDSpace = primaryPIDSpace; case el of when EL0 if EL2Enabled() then if ELIsInHost(EL0) then
```

```
if !UsePrimarySpaceEL2() then PIDSpace = PIDSpace_NonSecure; elsif !UsePrimarySpaceEL10() then PIDSpace = PIDSpace_NonSecure; elsif MPAM3_EL3.ALTSP_HEN == '0' && MPAM3_EL3.ALTSP_HFC == '1' then PIDSpace = PIDSpace_NonSecure; when EL1 if EL2Enabled() then if !UsePrimarySpaceEL10() then PIDSpace = PIDSpace_NonSecure; elsif MPAM3_EL3.ALTSP_HEN == '0' && MPAM3_EL3.ALTSP_HFC == '1' then PIDSpace = PIDSpace_NonSecure; when EL2 if !UsePrimarySpaceEL2() then PIDSpace = PIDSpace_NonSecure; otherwise Unreachable(); return PIDSpace;
```

```
J1.3.3.354 DefaultMPAMInfo // DefaultMPAMInfo() // ================= // Returns default MPAM info. The partidspace argument sets // the PARTID space of the default MPAM information returned. MPAMinfo DefaultMPAMInfo(PARTIDSpaceType partidspace) MPAMinfo defaultinfo; defaultinfo.mpam_sp = partidspace; defaultinfo.partid = DEFAULT_PARTID; defaultinfo.pmg = DEFAULT_PMG; return defaultinfo; J1.3.3.355 GenMPAM to
```

```
// GenMPAM() // ========= // Returns MPAMinfo for Exception level el. // If mpamdata.sm is TRUE returns MPAM information using MPAMSM_EL1. // If mpamdata.trb is TRUE returns MPAM information using TRBMPAM_EL1. // Otherwise returns MPAM information using MPAMn_ELx. MPAMinfo GenMPAM(bits(2) el_in, MPAMdata mpamdata, PARTIDSpaceType pspace) MPAMinfo returninfo; PARTIDType partidel; boolean perr; bits(2) el = el_in; // Check if the guest OS application is locked by the EL2 hypervisor // only use the EL1 virtual machine's PARTIDs. if (el == EL0 && EL2Enabled() && MPAMHCR_EL2.GSTAPP_PLK == '1' && HCR_EL2.TGE == '0') then el = EL1; (partidel, perr) = GenPARTID(el, mpamdata, pspace); constant PMGType groupel = GenPMG(el, mpamdata, perr, pspace); returninfo.mpam_sp = pspace; returninfo.partid = partidel; returninfo.pmg = groupel; return returninfo;
```

## J1.3.3.356 GenMPAMAtEL

```
// GenMPAMAtEL() // ============= // Returns MPAMinfo for the specified EL. // May be called if MPAM is not implemented (but in an version that supports // MPAM), MPAM is disabled, or in AArch32. In AArch32, convert the mode to // EL if can and use that to drive MPAM information generation. If mode // cannot be converted, MPAM is not implemented, or MPAM is disabled return // default MPAM information for the current security state. MPAMinfo GenMPAMAtEL(AccessType acctype, bits(2) el) bits(2) mpamEL; PARTIDSpaceType pspace; constant SecurityState security = SecurityStateAtEL(el); MPAMdata mpamdata = GenNewMPAMData(); pspace = PARTIDSpaceFromSS(security); if pspace == PIDSpace_NonSecure && !MPAMIsEnabled() then return DefaultMPAMInfo(pspace); mpamEL = if acctype == AccessType_NV2 then EL2 else el; case acctype of when AccessType_IFETCH, AccessType_IC mpamdata.in_d = TRUE; when AccessType_SME mpamdata.sm = (boolean IMPLEMENTATION_DEFINED "Shared SMCU" || boolean IMPLEMENTATION_DEFINED "MPAMSM_EL1 label precedence"); when AccessType_FP, AccessType_ASIMD, AccessType_SVE mpamdata.sm = (IsFeatureImplemented(FEAT_SME) && PSTATE.SM == '1' && (boolean IMPLEMENTATION_DEFINED "Shared SMCU" || boolean IMPLEMENTATION_DEFINED "MPAMSM_EL1 label precedence")); when AccessType_TRBE if !SelfHostedTraceEnabled() then if !IsFeatureImplemented(FEAT_TRBE_MPAM) || TRBMPAM_EL1.EN == '0' then return DefaultMPAMInfo(pspace); else mpamdata.trb = TRUE; if mpamdata.trb then SecurityState ss; case TRBMPAM_EL1.MPAM_SP of when '00' ss = SS_Secure; when '01' ss = SS_NonSecure; when '10' ss = SS_Root; when '11' ss = SS_Realm; pspace = PARTIDSpaceFromSS(ss); otherwise // Other access types are DATA accesses mpamdata.in_d = FALSE; if IsFeatureImplemented(FEAT_RME) && MPAMIDR_EL1.HAS_ALTSP == '1' then // Substitute alternative PARTID space if selected pspace = AltPARTIDSpace(mpamEL, security, pspace); if IsFeatureImplemented(FEAT_MPAMv0p1) && MPAMIDR_EL1.HAS_FORCE_NS == '1' then if MPAM3_EL3.FORCE_NS == '1' && security == SS_Secure then pspace = PIDSpace_NonSecure; if ((IsFeatureImplemented(FEAT_MPAMv0p1) || IsFeatureImplemented(FEAT_MPAMv1p1)) && MPAMIDR_EL1.HAS_SDEFLT == '1') then if MPAM3_EL3.SDEFLT == '1' && security == SS_Secure then return DefaultMPAMInfo(pspace); if !MPAMIsEnabled() then return DefaultMPAMInfo(pspace); else return GenMPAM(mpamEL, mpamdata, pspace);
```

## J1.3.3.357 GenMPAMCurEL

```
// GenMPAMCurEL() // ============== // Returns MPAMinfo for the current EL and security state. // May be called if MPAM is not implemented (but in an version that // MPAM), MPAM is disabled, or in AArch32. In AArch32, convert the mode to // EL if can and use that to drive MPAM information generation. If mode // cannot be converted, MPAM is not implemented, or MPAM is disabled return // default MPAM information for the current security state. MPAMinfo GenMPAMCurEL(AccessType acctype) return GenMPAMAtEL(acctype, PSTATE.EL);
```

```
// GenPMG() // ======== // Returns PMG for Exception level el. // if mpamdata.sm is TRUE then PMG is from MPAMSM_EL1. // If mpamdata.trb is TRUE then PMG is from TRBMPAM_EL1. // Otherwise, PMG is from MPAMn_ELx. // If PARTID generation (GenPARTID) encountered an error, GenPMG() should be // called with partid_err as TRUE. PMGType GenPMG(bits(2) el, MPAMdata mpamdata, boolean partid_err, PARTIDSpaceType if partid_err && ConstrainUnpredictableBool(Unpredictable_USE_DEFAULT_PMG) then return DEFAULT_PMG; constant PMGType groupel = GetMPAM_PMG(el, mpamdata); constant integer pmg_max = (if mpamdata.trb then UInt(TRBDEVID1.PMG_MAX)
```

```
supports J1.3.3.358 GenNewMPAMData // GenNewMPAMData() // ================ MPAMdata GenNewMPAMData() MPAMdata mpamdata; mpamdata.in_d = FALSE; mpamdata.sm = FALSE; mpamdata.trb = FALSE; return mpamdata; J1.3.3.359 GenPARTID // GenPARTID() // =========== // Returns physical PARTID and error boolean for Exception level el. // If mpamdata.sm is TRUE then PARTID is from MPAMSM_EL1. // If mpamdata.trb is TRUE then PARTID is from TRBMPAM_EL1. // Otherwise, the PARTID is from MPAMn_ELx. (PARTIDType, boolean) GenPARTID(bits(2) el, MPAMdata mpamdata, PARTIDSpaceType pspace) constant PARTIDType partidel = GetMPAM_PARTID(el, mpamdata); constant PARTIDType partid_max = (if mpamdata.trb then TRBDEVID1.PARTID_MAX else MPAMIDR_EL1.PARTID_MAX); if UInt(partidel) > UInt(partid_max) then return (DEFAULT_PARTID, TRUE); if MPAMIsVirtual(el, mpamdata) then return MAP_vPARTID(partidel); else return (partidel, FALSE); J1.3.3.360 GenPMG pspace)
```

```
if UInt(groupel) <= pmg_max then return groupel; return DEFAULT_PMG;
```

## J1.3.3.361 GetMPAM\_PARTID

```
// GetMPAM_PARTID() // ================ // Returns a PARTID // If mpamdata.sm is TRUE then PARTID is from MPAMSM_EL1. // If mpamdata.trb is TRUE then PARTID is from TRBMPAM_EL1. // Otherwise, the PARTID is from MPAMn_ELx. PARTIDType GetMPAM_PARTID(bits(2) MPAMn, MPAMdata mpamdata) if mpamdata.sm then return MPAMSM_EL1.PARTID_D; if mpamdata.trb then return TRBMPAM_EL1.PARTID; if mpamdata.in_d then case MPAMn of when '11' return MPAM3_EL3.PARTID_I; when '10' return (if EL2Enabled() then MPAM2_EL2.PARTID_I else DEFAULT_PARTID); when '01' return MPAM1_EL1.PARTID_I; when '00' return MPAM0_EL1.PARTID_I; else case MPAMn of when '11' return MPAM3_EL3.PARTID_D; when '10' return (if EL2Enabled() then MPAM2_EL2.PARTID_D else DEFAULT_PARTID); when '01' return MPAM1_EL1.PARTID_D; when '00' return MPAM0_EL1.PARTID_D;
```

## J1.3.3.362 GetMPAM\_PMG

```
// GetMPAM_PMG() // ============= // Returns a PMG. // if mpamdata.sm is TRUE then PMG is from MPAMSM_EL1. // If mpamdata.trb is TRUE then PMG is from TRBMPAM_EL1. // Otherwise, PMG is from MPAMn_ELx. PMGType GetMPAM_PMG(bits(2) MPAMn, MPAMdata mpamdata) if mpamdata.sm then return MPAMSM_EL1.PMG_D; if mpamdata.trb then return TRBMPAM_EL1.PMG; if mpamdata.in_d then case MPAMn of when '11' return MPAM3_EL3.PMG_I; when '10' return (if EL2Enabled() then MPAM2_EL2.PMG_I else DEFAULT_PMG); when '01' return MPAM1_EL1.PMG_I; when '00' return MPAM0_EL1.PMG_I; else case MPAMn of when '11' return MPAM3_EL3.PMG_D; when '10' return (if EL2Enabled() then MPAM2_EL2.PMG_D else DEFAULT_PMG); when '01' return MPAM1_EL1.PMG_D; when '00' return MPAM0_EL1.PMG_D;
```

else UInt(MPAMIDR\_EL1.PMG\_MAX));

## J1.3.3.363 MAP\_vPARTID

```
// MAP_vPARTID() // ============= // Performs conversion of virtual PARTID into physical PARTID // Contains all of the error checking and implementation // choices for the conversion. (PARTIDType, boolean) MAP_vPARTID(PARTIDType vpartid) // should not ever be called if EL2 is not implemented // or is implemented but not enabled in the current // security state. PARTIDType ret; boolean err; integer virt = UInt(vpartid); constant integer vpmrmax = UInt(MPAMIDR_EL1.VPMR_MAX); // vpartid_max is largest vpartid supported constant integer vpartid_max = (vpmrmax << 2) + 3; // One of many ways to reduce vpartid to value less than vpartid_max. if UInt(vpartid) > vpartid_max then virt = virt MOD (vpartid_max+1); // Check for valid mapping entry. if MPAMVPMV_EL2<virt> == '1' then // vpartid has a valid mapping so access the map. ret = mapvpmw(virt); err = FALSE; // Is the default virtual PARTID valid? elsif MPAMVPMV_EL2<0> == '1' then // Yes, so use default mapping for vpartid == 0. ret = MPAMVPM0_EL2<0 +: 16>; err = FALSE; // Neither is valid so use default physical PARTID. else ret = DEFAULT_PARTID; err = TRUE; // Check that the physical PARTID is in-range. // This physical PARTID came from a virtual mapping entry. constant integer partid_max = UInt(MPAMIDR_EL1.PARTID_MAX); if UInt(ret) > partid_max then // Out of range, so return default physical PARTID ret = DEFAULT_PARTID; err = TRUE; return (ret, err);
```

## J1.3.3.364 MPAM

```
constant PARTIDType DEFAULT_PARTID = 0<15:0>; constant PMGType DEFAULT_PMG = 0<7:0>; // Defines the MPAM _engine_. The _engine_ produces the MPAM labels for memory // accesses from the state information stored in the MPAM System registers. // The MPAM _engine_ runs in all states and with the MPAM AArch64 system // registers and PE execution state controlling its behavior. // MPAM Types // ==========
```

```
type PARTIDType = bits(16); type PMGType = bits(8); enumeration PARTIDSpaceType { PIDSpace_Secure, PIDSpace_Root, PIDSpace_Realm, PIDSpace_NonSecure }; type MPAMinfo is ( PARTIDSpaceType mpam_sp, PARTIDType partid, PMGType pmg ) type MPAMdata is ( boolean in_d, // TRUE for instruction accesses boolean sm, // TRUE for SME, SVE, SIMD&FP access, and SVE prefetch // instructions, when the PE is in Streaming mode boolean trb // TRUE for TRBE accesses using External mode when TRBMPAM_EL1.EN is 0b1 )
```

```
J1.3.3.365 MPAMIsEnabled // MPAMIsEnabled() // =============== // Returns TRUE if MPAM is enabled. boolean MPAMIsEnabled() el = HighestEL(); case el of when EL3 return MPAM3_EL3.MPAMEN == '1'; when EL2 return MPAM2_EL2.MPAMEN == '1'; when EL1 return MPAM1_EL1.MPAMEN == '1'; J1.3.3.366 MPAMIsVirtual // MPAMIsVirtual() // =============== // Returns TRUE if MPAM is configured to be virtual at the given el. boolean MPAMIsVirtual(bits(2) el, MPAMdata mpamdata) if mpamdata.trb then return FALSE; return (MPAMIDR_EL1.HAS_HCR == '1' && EL2Enabled() && ((el == EL0 && MPAMHCR_EL2.EL0_VPMEN == '1' && !ELIsInHost(EL0)) || (el == EL1 && MPAMHCR_EL2.EL1_VPMEN == '1'))); J1.3.3.367 PARTIDSpaceFromSS State.
```

```
// PARTIDSpaceFromSS() // =================== // Returns the primary PARTID space from the Security PARTIDSpaceType PARTIDSpaceFromSS(SecurityState security) case security of when SS_NonSecure return PIDSpace_NonSecure;
```

```
when SS_Root return PIDSpace_Root; when SS_Realm return PIDSpace_Realm; when SS_Secure return PIDSpace_Secure; otherwise Unreachable();
```

## J1.3.3.368 UsePrimarySpaceEL10

```
// UsePrimarySpaceEL10() // ===================== // Checks whether Primary space is configured in the // MPAM3_EL3 and MPAM2_EL2 ALTSP control bits that affect // MPAM ALTSP use at EL1 and EL0. boolean UsePrimarySpaceEL10() if MPAM3_EL3.ALTSP_HEN == '0' then return MPAM3_EL3.ALTSP_HFC == '0'; return !MPAMIsEnabled() || !EL2Enabled() || MPAM2_EL2.ALTSP_HFC == '0';
```

## J1.3.3.369 UsePrimarySpaceEL2

```
// UsePrimarySpaceEL2() // ==================== // Checks whether Primary space is configured in the // MPAM3_EL3 and MPAM2_EL2 ALTSP control bits that affect // MPAM ALTSP use at EL2. boolean UsePrimarySpaceEL2() if MPAM3_EL3.ALTSP_HEN == '0' then return MPAM3_EL3.ALTSP_HFC == '0'; return !MPAMIsEnabled() || MPAM2_EL2.ALTSP_EL2 == '0';
```

## J1.3.3.370 mapvpmw

```
// mapvpmw() // ========= // Map a virtual PARTID into a physical PARTID using // the MPAMVPMn_EL2 registers. // vpartid is now assumed in-range and valid (checked by caller) // returns physical PARTID from mapping entry. PARTIDType mapvpmw(integer vpartid) bits(64) vpmw; constant integer wd = vpartid DIV 4; case wd of when 0 vpmw = MPAMVPM0_EL2; when 1 vpmw = MPAMVPM1_EL2; when 2 vpmw = MPAMVPM2_EL2; when 3 vpmw = MPAMVPM3_EL2; when 4 vpmw = MPAMVPM4_EL2; when 5 vpmw = MPAMVPM5_EL2; when 6 vpmw = MPAMVPM6_EL2; when 7 vpmw = MPAMVPM7_EL2; otherwise vpmw = Zeros(64); // vpme_lsb selects LSB of field within register constant integer vpme_lsb = (vpartid MOD 4) * 16; return vpmw<vpme_lsb +: 16>;
```

## J1.3.3.371 ASID

```
// ASID // ==== // Effective ASID. bits(16) ASID[] if ELIsInHost(EL0) then if TCR_EL2.A1 == '1' then return TTBR1_EL2.ASID; else return TTBR0_EL2.ASID; if !ELUsingAArch32(EL1) then if TCR_EL1.A1 == '1' then return TTBR1_EL1.ASID; else return TTBR0_EL1.ASID; else if TTBCR.EAE == '0' then return else if TTBCR.A1 == '1' then return ZeroExtend(TTBR1.ASID, 16); else return ZeroExtend(TTBR0.ASID, 16);
```

```
// ExecutionCntxt // =============== // Context information for prediction restriction operation. type ExecutionCntxt is ( boolean is_vmid_valid, // is vmid valid for current context boolean all_vmid, // should the operation be applied for all vmids bits(16) vmid, // if all_vmid = FALSE, vmid to which operation is applied boolean is_asid_valid, // is asid valid for current context boolean all_asid, // should the operation be applied for all asids bits(16) asid, // if all_asid = FALSE, ASID to which operation is applied bits(2) target_el, // target EL at which operation is performed SecurityState security, RestrictType restriction // type of restriction operation )
```

```
// RestrictType // ============ // Type of restriction enumeration RestrictType { RestrictType_DataValue,
```

## ZeroExtend(CONTEXTIDR.ASID, 16); J1.3.3.372 ExecutionCntxt J1.3.3.373 RESTRICT\_PREDICTIONS // RESTRICT\_PREDICTIONS() // ====================== // Clear all speculated values. RESTRICT\_PREDICTIONS(ExecutionCntxt c) IMPLEMENTATION\_DEFINED; J1.3.3.374 RestrictType on speculation.

```
RestrictType_ControlFlow, RestrictType_Other
```

```
RestrictType_CachePrefetch, // Any other trained speculation mechanisms than those above };
```

## J1.3.3.375 TargetSecurityState

```
// TargetSecurityState() // ===================== // Decode the target security state for the prediction SecurityState TargetSecurityState(bit NS, bit NSE) curr_ss = SecurityStateAtEL(PSTATE.EL); if curr_ss == SS_NonSecure then return SS_NonSecure; elsif curr_ss == SS_Secure then case NS of when '0' return SS_Secure; when '1' return SS_NonSecure; elsif IsFeatureImplemented(FEAT_RME) then if curr_ss == SS_Root then case NSE:NS of when '00' return SS_Secure; when '01' return SS_NonSecure; when '11' return SS_Realm; when '10' return SS_Root; elsif curr_ss == SS_Realm then return SS_Realm; Unreachable();
```

## J1.3.3.376 BranchTo

```
// BranchTo() // ========== // Set program counter to a new address, with a branch type. // Parameter branch_conditional indicates whether the executed branch has a conditional encoding. // In AArch64 state the address might include a tag in the top eight bits. BranchTo(bits(N) target, BranchType branch_type, boolean branch_conditional) Hint_Branch(branch_type); if N == 32 then assert UsingAArch32(); _PC = ZeroExtend(target, 64); else assert N == 64 && !UsingAArch32(); constant bits(64) target_vaddress = AArch64.BranchAddr(target<63:0>, PSTATE.EL); if (IsFeatureImplemented(FEAT_BRBE) && branch_type IN {BranchType_DIR, BranchType_INDIR, BranchType_DIRCALL, BranchType_INDCALL, BranchType_RET}) then BRBEBranch(branch_type, branch_conditional, target_vaddress); constant boolean branch_taken = TRUE; if IsFeatureImplemented(FEAT_SPE) then SPEBranch(target, branch_type, branch_conditional, branch_taken); _PC = target_vaddress; return;
```

```
context.
```

## J1.3.3.377 BranchToAddr

```
// BranchToAddr() // ============== // Set program counter to a new address, with a branch type. // In AArch64 state the address does not include a tag in the top eight BranchToAddr(bits(N) target, BranchType branch_type) Hint_Branch(branch_type); if N == 32 then assert UsingAArch32(); _PC = ZeroExtend(target, 64); else assert N == 64 && !UsingAArch32(); _PC = target<63:0>; return;
```

```
// EffectiveFPCR() // =============== // Returns the effective FPCR FPCR_Type EffectiveFPCR() return FPCR;
```

## bits. J1.3.3.378 BranchType // BranchType // ========== // Information associated with a change in control flow. enumeration BranchType { BranchType\_DIRCALL, // Direct Branch with link BranchType\_INDCALL, // Indirect Branch with link BranchType\_ERET, // Exception return (indirect) BranchType\_DBGEXIT, // Exit from Debug state BranchType\_RET, // Indirect branch with function return hint BranchType\_DIR, // Direct branch BranchType\_INDIR, // Indirect branch BranchType\_EXCEPTION, // Exception entry BranchType\_RESET, // Reset BranchType\_UNKNOWN}; // Other J1.3.3.379 ESize // SIMD and Floating-point registers // +++++++++++++++++++++++++++++++++ // ESize // ===== type ESize = integer; J1.3.3.380 EffectiveFPCR value

## J1.3.3.381 FPCR\_Type

```
// FPCR_Type // ========= // A type representing the FPCR register type FPCR_Type;
```

## J1.3.3.382 FPMR\_Type

```
// FPMR_Type // ========= // A type representing the FPMR register type FPMR_Type;
```

## J1.3.3.383 Hint\_Branch

```
// Hint_Branch() // ============= // Report the hint passed to BranchTo() and BranchToAddr(), for consideration when processing // the next instruction. Hint_Branch(BranchType hint);
```

## J1.3.3.384 NextInstrAddr

```
// NextInstrAddr() // =============== // Return address of the sequentially next instruction. bits(N) NextInstrAddr(integer N);
```

## J1.3.3.385 ResetExternalDebugRegisters

```
// ResetExternalDebugRegisters() // ============================= // Reset the External Debug registers in the Core power domain. ResetExternalDebugRegisters(boolean cold_reset);
```

## J1.3.3.386 ThisInstrAddr

```
// ThisInstrAddr() // =============== // Return address of the current instruction. bits(N) ThisInstrAddr(integer N) assert N == 64 || (N == 32 && UsingAArch32()); return _PC<N-1:0>;
```

## J1.3.3.387 UnimplementedIDRegister

```
// UnimplementedIDRegister() // ========================= // Trap access to unimplemented encodings in the feature ID register space. UnimplementedIDRegister() if IsFeatureImplemented(FEAT_IDST) then target_el = PSTATE.EL; if PSTATE.EL == EL0 then target_el = if EL2Enabled() && HCR_EL2.TGE == '1' then EL2 else AArch64.SystemAccessTrap(target_el, 0x18); UNDEFINED;
```

## J1.3.3.388 V

```
// V -setter // ========== // Write to SIMD&FP register with implicit extension from // 8, 16, 32, 64 or 128 bits. V[integer n, ESize width] = bits(width) value assert n >= 0 && n <= 31; assert width IN {8, 16, 32, 64, 128}; constant VecLen vlen = if IsSVEEnabled(PSTATE.EL) then CurrentVL else 128; if ConstrainUnpredictableBool(Unpredictable_SVEZEROUPPER) then _Z[n] = ZeroExtend(value, MAX_VL); else _Z[n]<vlen-1:0> = ZeroExtend(value, vlen); // V -getter // ========== // Read from SIMD&FP register with implicit slice of 8, 16 // 32, 64 or 128 bits. bits(width) V[integer n, ESize width] assert n >= 0 && n <= 31; assert width IN {8, 16, 32, 64, 128}; return _Z[n]<width-1:0>;
```

## J1.3.3.389 Vpart

```
// Vpart -getter // ============== // Reads a 128-bit SIMD&FP register in up to two parts: // part 0 returns the bottom 8, 16, 32 or 64 bits of a value held in the register; // part 1 returns the top half of the bottom 64 bits or the top half of the 128-bit // value held in the register. bits(width) Vpart[integer n, integer part, ESize width] assert n >= 0 && n <= 31; assert part IN {0, 1}; if part == 0 then assert width < 128; return V[n, width]; else assert width IN {32,64}; constant bits(128) vreg = V[n, 128]; return vreg<(width * 2)-1:width>; // Vpart -setter // ============== // Writes a 128-bit SIMD&FP register in up to two parts:
```

```
EL1;
```

```
// part 0 zero extends a 8, 16, 32, or 64-bit value to fill the whole register; // part 1 inserts a 64-bit value into the top half of the register. Vpart[integer n, integer part, ESize width] = bits(width) value assert n >= 0 && n <= 31; assert part IN {0, 1}; if part == 0 then assert width < 128; V[n, width] = value; else assert width == 64; constant bits(64) vreg = V[n, 64]; V[n, 128] = value<63:0> : vreg;
```

## J1.3.3.390 \_PC

```
// _PC - the program counter // ========================= bits(64) _PC;
```

## J1.3.3.391 \_R

```
// _R - the general-purpose register file array // ============================================ array bits(64) _R[0..30];
```

## J1.3.3.392 SPSR\_ELx

```
// SPSR_ELx - getter // ================= bits(64) SPSR_ELx[] bits(64) result; case PSTATE.EL of when EL1 result = SPSR_EL1<63:0>; when EL2 result = SPSR_EL2<63:0>; when EL3 result = SPSR_EL3<63:0>; otherwise Unreachable(); return result; // SPSR_ELx - setter // ================= SPSR_ELx[] = bits(64) value case PSTATE.EL of when EL1 SPSR_EL1<63:0> = value<63:0>; when EL2 SPSR_EL2<63:0> = value<63:0>; when EL3 SPSR_EL3<63:0> = value<63:0>; otherwise Unreachable(); return;
```

## J1.3.3.393 SPSR\_curr

```
// SPSR_curr - getter // ================== bits(32) SPSR_curr[] bits(32) result;
```

```
case PSTATE.M of when M32_FIQ result = SPSR_fiq<31:0>; when M32_IRQ result = SPSR_irq<31:0>; when M32_Svc result = SPSR_svc<31:0>; when M32_Monitor result = SPSR_mon<31:0>; when M32_Abort result = SPSR_abt<31:0>; when M32_Hyp result = SPSR_hyp<31:0>; when M32_Undef result = SPSR_und<31:0>; otherwise Unreachable(); return result; // SPSR_curr - setter // ================== SPSR_curr[] = bits(32) value case PSTATE.M of when M32_FIQ SPSR_fiq<31:0> = when M32_IRQ SPSR_irq<31:0> = when M32_Svc SPSR_svc<31:0> = when M32_Monitor SPSR_mon<31:0> = when M32_Abort SPSR_abt<31:0> = when M32_Hyp SPSR_hyp<31:0> = when M32_Undef SPSR_und<31:0> = otherwise Unreachable(); return;
```

```
// AddressInNaturallyAlignedBlock() // ================================ // Returns TRUE if the given addresses are in the same naturally aligned block, and FALSE // An address is in a naturally aligned block if it meets any of the below conditions: // * is a power-of-two size. // * Is no larger than the DC ZVA block size if ESR_ELx.FnP is being set to 0b0, or EDHSR is not // implemented or EDHSR.FnP is being set to 0b0 (as appropriate).
```

## value&lt;31:0&gt;; value&lt;31:0&gt;; value&lt;31:0&gt;; value&lt;31:0&gt;; value&lt;31:0&gt;; value&lt;31:0&gt;; value&lt;31:0&gt;; J1.3.3.394 AArch64.ChkFeat // AArch64.ChkFeat() // ================= // Indicates the status of some features bits(64) AArch64.ChkFeat(bits(64) feat\_select) bits(64) feat\_en = Zeros(64); feat\_en&lt;0&gt; = if IsFeatureImplemented(FEAT\_GCS) &amp;&amp; GCSEnabled(PSTATE.EL) then '1' else '0'; return feat\_select AND NOT(feat\_en); J1.3.3.395 AddressAdd // AddressAdd() // ============ // Add an address with an offset and return the result. // If FEAT\_CPA2 is implemented, the pointer arithmetic is checked. bits(64) AddressAdd(bits(64) base, integer offset, AccessDescriptor accdesc) return AddressAdd(base, offset&lt;63:0&gt;, accdesc); bits(64) AddressAdd(bits(64) base, bits(64) offset, AccessDescriptor accdesc) bits(64) result = base + offset; result = PointerAddCheckAtEL(accdesc.el, result, base); return result; J1.3.3.396 AddressInNaturallyAlignedBlock otherwise.

```
// * Is no larger than the smallest implemented translation granule if ESR_ELx.FnP, or EDHSR.FnP // (as appropriate) is being set to 0b1. // * Contains a watchpointed address accessed by the memory access or set of contiguous memory // accesses that triggered the watchpoint.
```

boolean AddressInNaturallyAlignedBlock(bits(64) address1, bits(64) address2);

## J1.3.3.397 AddressIncrement

```
// AddressIncrement() // ================== // Increment an address and return the result. // If FEAT_CPA2 is implemented, the pointer arithmetic may be checked. bits(64) AddressIncrement(bits(64) base, integer increment, AccessDescriptor accdesc) return AddressIncrement(base, increment<63:0>, accdesc); bits(64) AddressIncrement(bits(64) base, bits(64) increment, AccessDescriptor accdesc) bits(64) result = base + increment; // Checking the Pointer Arithmetic on an increment is equivalent to checking the // bytes in a sequential access crossing the 0xXXFF_FFFF_FFFF_FFFF boundary. if ConstrainUnpredictableBool(Unpredictable_CPACHECK) then result = PointerAddCheckAtEL(accdesc.el, result, base); return result;
```

## J1.3.3.398 BranchTargetCheck

```
// BranchTargetCheck() // =================== // This function is executed checks if the current instruction is a valid target for a branch // taken into, or inside, a guarded page. It is executed on every cycle once the current // instruction has been decoded and the values of InGuardedPage and BTypeCompatible have been // determined for the current instruction. BranchTargetCheck() assert IsFeatureImplemented(FEAT_BTI) && !UsingAArch32(); // The branch target check considers the following state variables: // * InGuardedPage, which is evaluated during instruction fetch. // * BTypeCompatible, which is evaluated during instruction decode. if Halted() then return; elsif IsZero(PSTATE.BTYPE) then return; elsif InGuardedPage && !BTypeCompatible then constant bits(64) pc = ThisInstrAddr(64); AArch64.BranchTargetException(pc<51:0>);
```

## J1.3.3.399 ClearEventRegister

```
// ClearEventRegister() // ==================== // Clear the Event Register of this ClearEventRegister() EventRegister = '0'; return;
```

```
PE.
```

## J1.3.3.400 ConditionHolds

```
// ConditionHolds() // ================ // Return TRUE iff COND currently holds boolean ConditionHolds(bits(4) cond) // Evaluate base condition. boolean result; case cond<3:1> of when '000' result = (PSTATE.Z == '1'); // EQ or NE when '001' result = (PSTATE.C == '1'); // CS or CC when '010' result = (PSTATE.N == '1'); // MI or PL when '011' result = (PSTATE.V == '1'); // VS or VC when '100' result = (PSTATE.C == '1' && PSTATE.Z == '0'); // HI or LS when '101' result = (PSTATE.N == PSTATE.V); // GE or LT when '110' result = (PSTATE.N == PSTATE.V && PSTATE.Z == '0'); // GT or LE when '111' result = TRUE; // AL // Condition flag values in the set '111x' indicate always true // Otherwise, invert condition if necessary. if cond<0> == '1' && cond != '1111' then result = !result; return result;
```

## J1.3.3.401 ConsumptionOfSpeculativeDataBarrier

## // ConsumptionOfSpeculativeDataBarrier() // ===================================== ConsumptionOfSpeculativeDataBarrier(); J1.3.3.402 CurrentInstrSet // CurrentInstrSet() // ================= InstrSet CurrentInstrSet() InstrSet result; if UsingAArch32() then result = if PSTATE.T == '0' then InstrSet\_A32 else InstrSet\_T32; // PSTATE.J is RES0. Implementation of T32EE or Jazelle state not permitted. else result = InstrSet\_A64; return result; J1.3.3.403 CurrentSecurityState current settings.

```
// CurrentSecurityState() // ====================== // Returns the effective security state at the exception level based off SecurityState CurrentSecurityState() return SecurityStateAtEL(PSTATE.EL);
```

## J1.3.3.404 DSBAlias

```
// DSBAlias // ======== // Aliases of DSB. enumeration DSBAlias {DSBAlias_SSBB, DSBAlias_PSSBB, DSBAlias_DSB};
```

## J1.3.3.405 EL0

```
// EL0-3 // ===== // PSTATE.EL Exception level constant bits(2) EL3 = '11'; constant bits(2) EL2 = '10'; constant bits(2) EL1 = '01'; constant bits(2) EL0 = '00';
```

## J1.3.3.406 EL2Enabled

```
// EL2Enabled() // ============ // Returns TRUE if EL2 is present and executing // -with the PE in Non-secure state when Non-secure EL2 is implemented, or // -with the PE in Realm state when Realm EL2 is implemented, or // -with the PE in Secure state when Secure EL2 is implemented and enabled, or // -when EL3 is not implemented. boolean EL2Enabled() bit scr_ns; if HaveEL(EL3) then if ELUsingAArch32(EL3) then scr_ns = SCR.NS; else scr_ns = SCR_EL3.NS; return HaveEL(EL2) && (!HaveEL(EL3) || scr_ns == '1' || IsSecureEL2Enabled());
```

## J1.3.3.407 EL3SDDUndef

```
// EL3SDDUndef() // ============= // Returns TRUE if in Debug state and EDSCR.SDD is set. boolean EL3SDDUndef() if Halted() && EDSCR.SDD == '1' then assert (PSTATE.EL != EL3 && (IsFeatureImplemented(FEAT_RME) || CurrentSecurityState() != return TRUE; else return FALSE;
```

```
bits.
```

```
SS_Secure));
```

## J1.3.3.408 EL3SDDUndefPriority

```
// EL3SDDUndefPriority() // ===================== // Returns TRUE if in Debug state, EDSCR.SDD is set, and an EL3 trap by an // EL3 control register has priority over other traps. // The IMPLEMENTATION DEFINED priority may be different for each case. boolean EL3SDDUndefPriority() return EL3SDDUndef() && boolean IMPLEMENTATION_DEFINED "EL3 trap priority when SDD == '1'";
```

```
J1.3.3.409 ELFromM32 // ELFromM32() // =========== (boolean,bits(2)) ELFromM32(bits(5) mode) // Convert an AArch32 mode encoding to an Exception level. // Returns (valid,EL): // 'valid' is TRUE if 'mode<4:0>' encodes a mode that is both valid for this implementation // and the current value of SCR.NS/SCR_EL3.NS. // 'EL' is the Exception level decoded from 'mode'. bits(2) el; boolean valid = !BadMode(mode); // Check for modes that are not valid for this implementation constant bits(2) effective_nse_ns = EffectiveSCR_EL3_NSE() : EffectiveSCR_EL3_NS(); case mode of when M32_Monitor el = EL3; when M32_Hyp el = EL2; when M32_FIQ, M32_IRQ, M32_Svc, M32_Abort, M32_Undef, M32_System // If EL3 is implemented and using AArch32, then these modes are EL3 modes in Secure // state, and EL1 modes in Non-secure state. If EL3 is not implemented or is using // AArch64, then these modes are EL1 modes. el = (if HaveEL(EL3) && !HaveAArch64() && SCR.NS == '0' then EL3 else EL1); when M32_User el = EL0; otherwise valid = FALSE; // Passed an illegal mode value if valid && el == EL2 && HaveEL(EL3) then if ELUsingAArch32(EL3) && SCR.NS == '0' then valid = FALSE; // EL2 only valid in Non-secure state in AArch32 elsif !ELUsingAArch32(EL3) && SCR_EL3.NS == '0' then valid = FALSE; // EL2 only valid in Non-secure state in AArch32 elsif valid && IsFeatureImplemented(FEAT_RME) && effective_nse_ns == '10' then valid = FALSE; // Illegal Exception Return from EL3 if SCR_EL3.<NSE,NS> // selects a reserved encoding if !valid then el = bits(2) UNKNOWN; return (valid, el); J1.3.3.410 ELFromSPSR // ELFromSPSR() // ============ // Convert an SPSR value encoding to an Exception level. // Returns (valid,EL): // 'valid' is TRUE if 'spsr<4:0>' encodes a valid mode for the current state. // 'EL' is the Exception level decoded from 'spsr'.
```

```
ELFromSPSR(bits(N) spsr) bits(2) el; boolean valid; if spsr<4> == '0' then // AArch64 state el = spsr<3:2>; constant bits(2) effective_nse_ns = EffectiveSCR_EL3_NSE() : EffectiveSCR_EL3_NS(); if !HaveAArch64() then valid = FALSE; // No AArch64 support elsif !HaveEL(el) then valid = FALSE; // Exception level not implemented elsif spsr<1> == '1' then valid = FALSE; // M<1> must be 0 elsif el == EL0 && spsr<0> == '1' then valid = FALSE; // for EL0, M<0> must be 0 elsif IsFeatureImplemented(FEAT_RME) && el != EL3 && effective_nse_ns == '10' then valid = FALSE; // Only EL3 valid in Root state elsif el == EL2 && HaveEL(EL3) && !IsSecureEL2Enabled() && EffectiveSCR_EL3_NS() == '0' then valid = FALSE; // Unless Secure EL2 is enabled, EL2 valid only in Non-secure state else valid = TRUE; elsif HaveAArch32() then // AArch32 state (valid, el) = ELFromM32(spsr<4:0>); else valid = FALSE; if !valid then el = bits(2) UNKNOWN; return (valid,el);
```

```
(boolean,bits(2)) J1.3.3.411 ELIsInHost // ELIsInHost() // ============ boolean ELIsInHost(bits(2) el) if !IsFeatureImplemented(FEAT_VHE) || ELUsingAArch32(EL2) then return FALSE; case el of when EL3 return FALSE; when EL2 return EL2Enabled() && EffectiveHCR_EL2_E2H() == '1'; when EL1 return FALSE; when EL0 return EL2Enabled() && EffectiveHCR_EL2_E2H():HCR_EL2.TGE == '11'; otherwise Unreachable(); J1.3.3.412 ELStateUsingAArch32
```

```
// ELStateUsingAArch32() // ===================== boolean ELStateUsingAArch32(bits(2) el, boolean secure) // See ELStateUsingAArch32K() for description. Must only be called in circumstances where // result is valid (typically, that means 'el IN {EL1,EL2,EL3}'). (known, aarch32) = ELStateUsingAArch32K(el, secure); assert known; return aarch32;
```

## J1.3.3.413 ELStateUsingAArch32K

```
// ELStateUsingAArch32K() // ====================== // Returns (known, aarch32): // 'known' is FALSE for EL0 if the current Exception level is not EL0 and EL1 is // using AArch64, since it cannot determine the state of EL0; TRUE otherwise. // 'aarch32' is TRUE if the specified Exception level is using AArch32; FALSE otherwise. (boolean, boolean) ELStateUsingAArch32K(bits(2) el, boolean secure) assert HaveEL(el); if !HaveAArch32EL(el) then return (TRUE, FALSE); // Exception level is using AArch64 elsif secure && el == EL2 then return (TRUE, FALSE); // Secure EL2 is using AArch64 elsif !HaveAArch64() then return (TRUE, TRUE); // Highest Exception level, therefore all levels are using AArch32 // Remainder of function deals with the interprocessing cases when highest // Exception level is using AArch64. if el == EL3 then return (TRUE, FALSE); if (HaveEL(EL3) && SCR_EL3.RW == '0' && (!secure || !IsFeatureImplemented(FEAT_SEL2) || SCR_EL3.EEL2 == '0')) then // AArch32 below EL3. return (TRUE, TRUE); if el == EL2 then return (TRUE, FALSE); if (HaveEL(EL2) && !ELIsInHost(EL0) && HCR_EL2.RW == '0' && (!secure || (IsFeatureImplemented(FEAT_SEL2) && SCR_EL3.EEL2 == '1'))) then // AArch32 below EL2. return (TRUE, TRUE); if el == EL1 then return (TRUE, FALSE); // The execution state of EL0 is only known from PSTATE.nRW when executing at EL0. if PSTATE.EL == EL0 then return (TRUE, PSTATE.nRW == '1'); else return (FALSE, boolean UNKNOWN);
```

## J1.3.3.414 ELUsingAArch32 // ELUsingAArch32() // ================ boolean ELUsingAArch32(bits(2) el) return ELStateUsingAArch32(el, IsSecureBelowEL3()); J1.3.3.415 ELUsingAArch32K // ELUsingAArch32K() // ================= (boolean,boolean) ELUsingAArch32K(bits(2) el) return ELStateUsingAArch32K(el, IsSecureBelowEL3());

## J1.3.3.416 EffectiveEA

```
// EffectiveEA() // ============= // Returns effective SCR_EL3.EA value bit EffectiveEA() if !HaveEL(EL3) || Halted() then return '0'; else return if HaveAArch64() then SCR_EL3.EA else SCR.EA;
```

## J1.3.3.417 EffectiveHCR\_EL2\_E2H

```
// EffectiveHCR_EL2_E2H() // ====================== // Return the Effective HCR_EL2.E2H value. bit EffectiveHCR_EL2_E2H() if !IsFeatureImplemented(FEAT_VHE) then return '0'; if !IsFeatureImplemented(FEAT_E2H0) then return '1'; return HCR_EL2.E2H;
```

## J1.3.3.418 EffectiveHCR\_EL2\_NVx

```
// EffectiveHCR_EL2_NVx() // ====================== // Return the Effective value of HCR_EL2.<NV2,NV1,NV>. bits(3) EffectiveHCR_EL2_NVx() if !EL2Enabled() || !IsFeatureImplemented(FEAT_NV) then return '000'; bit nv1 = HCR_EL2.NV1; if (!IsFeatureImplemented(FEAT_E2H0) && boolean IMPLEMENTATION_DEFINED "HCR_EL2.NV1 is implemented as RAZ") then nv1 = '0'; if HCR_EL2.NV == '0' then if nv1 == '1' then case ConstrainUnpredictable(Unpredictable_NVNV1) of when Constraint_NVNV1_00 return '000'; when Constraint_NVNV1_01 return '010'; when Constraint_NVNV1_11 return '011'; else return '000'; if !IsFeatureImplemented(FEAT_NV2) then return '0' : nv1 : '1'; bit nv2 = HCR_EL2.NV2; if (nv2 == '0' && boolean IMPLEMENTATION_DEFINED "Programming HCR_EL2.<NV,NV2> to '10' behaves as '11'") then nv2 = '1'; return nv2 : nv1 : '1';
```

## J1.3.3.419 EffectiveSCR\_EL3\_NS

```
// EffectiveSCR_EL3_NS() // ===================== // Return Effective SCR_EL3.NS value. bit EffectiveSCR_EL3_NS() if !HaveSecureState() then return '1'; elsif !HaveEL(EL3) then return '0'; elsif ELUsingAArch32(EL3) then return SCR.NS; else return SCR_EL3.NS;
```

## J1.3.3.420 EffectiveSCR\_EL3\_NSE

```
// EffectiveSCR_EL3_NSE() // ====================== // Return Effective SCR_EL3.NSE value. bit EffectiveSCR_EL3_NSE() return if !IsFeatureImplemented(FEAT_RME) then '0' else SCR_EL3.NSE;
```

## J1.3.3.421 EffectiveSCR\_EL3\_RW

```
// EffectiveSCR_EL3_RW() // ===================== // Returns effective SCR_EL3.RW value bit EffectiveSCR_EL3_RW() if !HaveAArch64() then return '0'; if !HaveAArch32EL(EL2) && !HaveAArch32EL(EL1) then return '1'; if HaveAArch32EL(EL1) then if !HaveAArch32EL(EL2) && EffectiveSCR_EL3_NS() == '1' then return '1'; if (IsFeatureImplemented(FEAT_SEL2) && SCR_EL3.EEL2 == '1' && EffectiveSCR_EL3_NS() == '0') then return '1'; return SCR_EL3.RW;
```

## J1.3.3.422 EffectiveTGE

```
// EffectiveTGE() // ============== // Returns effective TGE value bit EffectiveTGE() if EL2Enabled() then return if ELUsingAArch32(EL2) then HCR.TGE else HCR_EL2.TGE; else return '0'; // Effective value of TGE is zero
```

## J1.3.3.423 EndOfInstruction

```
// EndOfInstruction() // ================== // Terminate processing of the current instruction. EndOfInstruction();
```

## J1.3.3.424 EnterLowPowerState

```
// EnterLowPowerState() // ==================== // PE enters a low-power state. EnterLowPowerState();
```

## J1.3.3.425 EventRegister

```
// EventRegister // ============= // Event Register for this PE. bits(1) EventRegister;
```

## J1.3.3.426 ExceptionalOccurrenceTargetState

```
// ExceptionalOccurrenceTargetState // ================================ // Enumeration to represent the target state of an Exceptional Occurrence. // The Exceptional Occurrence can be either Exception or Debug State entry. enumeration ExceptionalOccurrenceTargetState { AArch32_NonDebugState, AArch64_NonDebugState, DebugState };
```

## J1.3.3.427 ExecuteAsNOP

```
// ExecuteAsNOP() // ============== ExecuteAsNOP() EndOfInstruction();
```

## J1.3.3.428 FIQPending

```
// FIQPending() // ============ // Returns a tuple indicating if there is any pending physical FIQ // and if the pending FIQ has superpriority. (boolean, boolean) FIQPending();
```

## J1.3.3.429 GetAccumulatedFPExceptions

```
// GetAccumulatedFPExceptions() // ============================ // Returns FP exceptions accumulated by the PE. bits(8) GetAccumulatedFPExceptions();
```

## J1.3.3.430 GetLoadStoreType

```
// GetLoadStoreType() // ================== // Returns the Load/Store Type. Used when a Translation fault, // Access flag fault, or Permission fault generates a Data Abort. bits(2) GetLoadStoreType();
```

## J1.3.3.431 GetPSRFromPSTATE

```
// GetPSRFromPSTATE() // ================== // Return a PSR value which represents the current PSTATE bits(N) GetPSRFromPSTATE(ExceptionalOccurrenceTargetState targetELState, integer N) if UsingAArch32() && targetELState == AArch32_NonDebugState then assert N == 32; else assert N == 64; bits(N) spsr = Zeros(N); if IsFeatureImplemented(FEAT_UINJ) && targetELState == DebugState then spsr<36> = PSTATE.UINJ; spsr<31:28> = PSTATE.<N,Z,C,V>; if IsFeatureImplemented(FEAT_PAN) then spsr<22> = PSTATE.PAN; spsr<20> = PSTATE.IL; if PSTATE.nRW == '1' then // AArch32 state if IsFeatureImplemented(FEAT_SEBEP) && targetELState != AArch32_NonDebugState then spsr<33> = PSTATE.PPEND; spsr<27> = PSTATE.Q; spsr<26:25> = PSTATE.IT<1:0>; if IsFeatureImplemented(FEAT_SSBS) then spsr<23> = PSTATE.SSBS; if IsFeatureImplemented(FEAT_DIT) then if targetELState == AArch32_NonDebugState then spsr<21> = PSTATE.DIT; else // AArch64_NonDebugState or DebugState spsr<24> = PSTATE.DIT; if targetELState IN {AArch64_NonDebugState, DebugState} then spsr<21> = PSTATE.SS; spsr<19:16> = PSTATE.GE; spsr<15:10> = PSTATE.IT<7:2>; spsr<9> = PSTATE.E; spsr<8:6> = PSTATE.<A,I,F>; // No PSTATE.D in AArch32 state spsr<5> = PSTATE.T; assert PSTATE.M<4> == PSTATE.nRW; // bit [4] is the discriminator spsr<4:0> = PSTATE.M; else // AArch64 state if IsFeatureImplemented(FEAT_PAuth_LR) then spsr<35> = PSTATE.PACM; if IsFeatureImplemented(FEAT_GCS) then spsr<34> = PSTATE.EXLOCK; if IsFeatureImplemented(FEAT_SEBEP) then spsr<33> = PSTATE.PPEND; if (IsFeatureImplemented(FEAT_EBEP) || IsFeatureImplemented(FEAT_SPE_EXC) || IsFeatureImplemented(FEAT_TRBE_EXC)) then spsr<32> = PSTATE.PM; if IsFeatureImplemented(FEAT_MTE) then spsr<25> = PSTATE.TCO;
```

```
if IsFeatureImplemented(FEAT_DIT) then spsr<24> = PSTATE.DIT; if IsFeatureImplemented(FEAT_UAO) then spsr<23> = PSTATE.UAO; spsr<21> = PSTATE.SS; if IsFeatureImplemented(FEAT_NMI) then spsr<13> = PSTATE.ALLINT; if IsFeatureImplemented(FEAT_SSBS) then spsr<12> = PSTATE.SSBS; if IsFeatureImplemented(FEAT_BTI) then spsr<11:10> = spsr<9:6> = PSTATE.<D,A,I,F>; spsr<4> = PSTATE.nRW; spsr<3:2> = PSTATE.EL; spsr<0> = PSTATE.SP; spsr;
```

## PSTATE.BTYPE; return J1.3.3.432 HaveAArch32 // HaveAArch32() // ============= // Return TRUE if AArch32 state is supported at at least EL0. boolean HaveAArch32() return IsFeatureImplemented(FEAT\_AA32EL0); J1.3.3.433 HaveAArch32EL // HaveAArch32EL() // =============== // Return TRUE if Exception level 'el' supports AArch32 in this implementation boolean HaveAArch32EL(bits(2) el) case el of when EL0 return IsFeatureImplemented(FEAT\_AA32EL0); when EL1 return IsFeatureImplemented(FEAT\_AA32EL1); when EL2 return IsFeatureImplemented(FEAT\_AA32EL2); when EL3 return IsFeatureImplemented(FEAT\_AA32EL3); J1.3.3.434 HaveAArch64 // HaveAArch64() // ============= // Return TRUE if the highest Exception level is using AArch64 state. boolean HaveAArch64() return (IsFeatureImplemented(FEAT\_AA64EL0) || IsFeatureImplemented(FEAT\_AA64EL1) || IsFeatureImplemented(FEAT\_AA64EL2) || IsFeatureImplemented(FEAT\_AA64EL3) ); J1.3.3.435 HaveEL // HaveEL() // ======== // Return TRUE if Exception level 'el' is supported boolean HaveEL(bits(2) el) case el of when EL1,EL0 return TRUE; // EL1 and EL0 must exist when EL2 return IsFeatureImplemented(FEAT\_AA64EL2) || IsFeatureImplemented(FEAT\_AA32EL2); when EL3

```
return IsFeatureImplemented(FEAT_AA64EL3) || IsFeatureImplemented(FEAT_AA32EL3); otherwise Unreachable();
```

## J1.3.3.436 HaveELUsingSecurityState // HaveELUsingSecurityState() // ========================== // Returns TRUE if Exception level 'el' with Security state 'secure' is supported, // FALSE otherwise. boolean HaveELUsingSecurityState(bits(2) el, boolean secure) case el of when EL3 assert secure; return HaveEL(EL3); when EL2 if secure then return HaveEL(EL2) &amp;&amp; IsFeatureImplemented(FEAT\_SEL2); else return HaveEL(EL2); otherwise return (HaveEL(EL3) || (secure == boolean IMPLEMENTATION\_DEFINED "Secure-only implementation")); J1.3.3.437 HaveSecureState // HaveSecureState() // ================= // Return TRUE if Secure State is supported. boolean HaveSecureState() if !HaveEL(EL3) then return SecureOnlyImplementation(); if IsFeatureImplemented(FEAT\_RME) &amp;&amp; !IsFeatureImplemented(FEAT\_SEL2) then return FALSE; return TRUE; J1.3.3.438 HighestEL // HighestEL() // =========== // Returns the highest implemented Exception level. bits(2) HighestEL() if HaveEL(EL3) then return EL3; elsif HaveEL(EL2) then return EL2; else return EL1; J1.3.3.439 Hint\_CLRBHB the current context.

```
// Hint_CLRBHB() // ============= // Provides a hint to clear the branch history for Hint_CLRBHB();
```

## J1.3.3.440 Hint\_DGH

```
// Hint_DGH() // ========== // Provides a hint to close any gathering occurring within the implementation. Hint_DGH();
```

## J1.3.3.441 Hint\_StoreShared

```
// Hint_StoreShared() // ================== // Provides a hint that if the next instruction is an explict write it is being waited on by // observers and as such the data should propagate to them with minimum latency. // A stream value of FALSE indicates KEEP whilst a value of TRUE indicates STRM. Hint_StoreShared(boolean stream);
```

## J1.3.3.442 Hint\_WFE

```
// Hint_WFE() // ========== // Provides a hint indicating that the PE can enter a low-power state and // remain there until a wakeup event occurs. Hint_WFE() if IsEventRegisterSet() then ClearEventRegister(); return; boolean trap; bits(2) target_el; (trap, target_el) = AArch64.CheckForWFxTrap(WFxType_WFE); if trap then if IsFeatureImplemented(FEAT_TWED) then // Determine if trap delay is enabled and delay amount boolean delay_enabled; integer delay; (delay_enabled, delay) = WFETrapDelay(target_el); if WaitForEventUntilDelay(delay_enabled, delay) then // Event arrived before delay return; // Proceed with trapping if target_el == EL3 && EL3SDDUndef() then UNDEFINED; else AArch64.WFxTrap(WFxType_WFE, target_el); else WaitForEvent();
```

## J1.3.3.443 Hint\_WFET

```
// Hint_WFET() // =========== // Provides a hint indicating that the PE can enter a low-power state // and remain there until a wakeup event occurs or, for WFET, a local // timeout event is generated when the virtual timer value equals or // exceeds the supplied threshold value. Hint_WFET(integer localtimeout)
```

```
if IsEventRegisterSet() then ClearEventRegister(); return; if IsFeatureImplemented(FEAT_WFxT) && LocalTimeoutEvent(localtimeout) then // No further operation if the local timeout has expired. EndOfInstruction(); return; boolean trap; bits(2) target_el; (trap, target_el) = AArch64.CheckForWFxTrap(WFxType_WFET); if trap then if IsFeatureImplemented(FEAT_TWED) then // Determine if trap delay is enabled and delay amount boolean delay_enabled; integer delay; (delay_enabled, delay) = WFETrapDelay(target_el); if WaitForEventUntilDelay(delay_enabled, delay) then // Event arrived before the delay expired return; // Proceed with trapping if target_el == EL3 && EL3SDDUndef() then UNDEFINED; else AArch64.WFxTrap(WFxType_WFET, target_el); else WaitForEvent(localtimeout);
```

## J1.3.3.444 Hint\_WFI

```
// Hint_WFI() // ========== // Provides a hint indicating that the PE can enter a low-power state and // remain there until a wakeup event occurs. Hint_WFI() if AArch64.InterruptPending() then // No further operation if an interrupt is pending. EndOfInstruction(); return; boolean trap; bits(2) target_el; (trap, target_el) = AArch64.CheckForWFxTrap(WFxType_WFI); if trap then if target_el == EL3 && EL3SDDUndef() then UNDEFINED; AArch64.WFxTrap(WFxType_WFI, target_el); else WaitForInterrupt();
```

## J1.3.3.445 Hint\_WFIT

```
// Hint_WFIT() // =========== // Provides a hint indicating that the PE can enter a low-power state and // remain there until a wakeup event occurs or, for WFIT, a local timeout // event is generated when the virtual timer value equals or exceeds the // supplied threshold value. Hint_WFIT(integer localtimeout)
```

```
if (AArch64.InterruptPending() || (IsFeatureImplemented(FEAT_WFxT) && LocalTimeoutEvent(localtimeout))) then // No further operation if an interrupt is pending or the local timeout has expired. EndOfInstruction(); return; boolean trap; bits(2) target_el; (trap, target_el) = AArch64.CheckForWFxTrap(WFxType_WFIT); if trap then if target_el == EL3 && EL3SDDUndef() then UNDEFINED; AArch64.WFxTrap(WFxType_WFIT, target_el); else WaitForInterrupt(localtimeout); J1.3.3.446 Hint_Yield // Hint_Yield() // ============ // Provides a hint that the task performed by a thread is of low // importance so that it could yield to improve overall performance. Hint_Yield(); J1.3.3.447 IRQPending // IRQPending() // ============ // Returns a tuple indicating if there is any pending physical IRQ // and if the pending IRQ has superpriority. (boolean, boolean) IRQPending(); J1.3.3.448 IllegalExceptionReturn // IllegalExceptionReturn() // ======================== boolean IllegalExceptionReturn(bits(N) spsr) // Check for illegal return: // * To an unimplemented Exception level. // * To EL2 in Secure state, when SecureEL2 is not enabled. // * To EL0 using AArch64 state, with SPSR.M<0>==1. // * To AArch64 state with SPSR.M<1>==1. // * To AArch32 state with an illegal value of SPSR.M. (valid, target) = ELFromSPSR(spsr); if !valid then return TRUE; // Check for return to higher Exception level. if UInt(target) > UInt(PSTATE.EL) then return TRUE; spsr_mode_is_aarch32 = (spsr<4> == '1'); // Check for illegal return: // * To EL1, EL2 or EL3 with register width specified in the SPSR different from the // Execution state used in the Exception level being returned to, as determined by // the SCR_EL3.RW or HCR_EL2.RW bits, or as configured from reset. // * To EL0 using AArch64 state when EL1 is using AArch32 state as determined by the // SCR_EL3.RW or HCR_EL2.RW bits or as configured from reset. // * To AArch64 state from AArch32 state (should be caught by above).
```

```
(known, target_el_is_aarch32) = ELUsingAArch32K(target); assert known || (target == EL0 && !ELUsingAArch32(EL1)); if known && spsr_mode_is_aarch32 != target_el_is_aarch32 then return TRUE; // Check for illegal return from AArch32 to AArch64. if UsingAArch32() && !spsr_mode_is_aarch32 then return TRUE; // Check for illegal return to EL1 when HCR_EL2.TGE is set and when either // * SecureEL2 is enabled. // * SecureEL2 is not enabled and EL1 is in Non-secure state. if EL2Enabled() && target == EL1 && HCR_EL2.TGE == '1' then if (!IsSecureBelowEL3() || IsSecureEL2Enabled()) then return TRUE; if (IsFeatureImplemented(FEAT_GCS) && PSTATE.EXLOCK == '0' && PSTATE.EL == target && GetCurrentEXLOCKEN()) then return TRUE; return FALSE;
```

```
// IsCurrentSecurityState() // ======================== // Returns TRUE if the current Security state // the given Security state, and FALSE otherwise. boolean IsCurrentSecurityState(SecurityState ss) return CurrentSecurityState() == ss;
```

## of J1.3.3.449 InstrSet // InstrSet // ======== enumeration InstrSet {InstrSet\_A64, InstrSet\_A32, InstrSet\_T32}; J1.3.3.450 InstructionFetchBarrier // InstructionFetchBarrier() // ========================= InstructionFetchBarrier(); J1.3.3.451 InstructionSynchronizationBarrier // InstructionSynchronizationBarrier() // =================================== InstructionSynchronizationBarrier(); J1.3.3.452 IsASEInstruction // IsASEInstruction() // ================== // Returns TRUE if the current instruction is an ASIMD or SVE vector instruction. boolean IsASEInstruction(); J1.3.3.453 IsCurrentSecurityState matches

## J1.3.3.454 IsEventRegisterSet

```
// IsEventRegisterSet() // ==================== // Return TRUE if the Event Register of this PE is set, and FALSE if it is clear. boolean IsEventRegisterSet() return EventRegister == '1';
```

## J1.3.3.455 IsHighestEL

```
// IsHighestEL() // ============= // Returns TRUE if given exception level is the highest exception level implemented boolean IsHighestEL(bits(2) el) return HighestEL() == el;
```

## J1.3.3.456 IsInHost

```
// IsInHost() // ========== boolean IsInHost() return ELIsInHost(PSTATE.EL);
```

## J1.3.3.457 IsSecureBelowEL3

```
// IsSecureBelowEL3() // ================== // Return TRUE if an Exception level below EL3 is in Secure state // or would be following an exception return to that level. // // That is, if at AArch64 EL3 or in AArch32 Monitor mode, whether an // exception return would pass to Secure or Non-secure state. boolean IsSecureBelowEL3() if HaveEL(EL3) then return if !HaveAArch64() then SCR.NS == '0' else SCR_EL3.NS == '0'; elsif HaveEL(EL2) && (!IsFeatureImplemented(FEAT_SEL2) || !HaveAArch64()) then // If Secure EL2 is not an architecture option then we must be Non-secure. return FALSE; else // TRUE if PE is Secure or FALSE if Non-secure. return boolean IMPLEMENTATION_DEFINED "Secure-only implementation";
```

## J1.3.3.458 IsSecureEL2Enabled

```
// IsSecureEL2Enabled() // ==================== // Returns TRUE if Secure EL2 is enabled, FALSE otherwise. boolean IsSecureEL2Enabled() if HaveEL(EL2) && IsFeatureImplemented(FEAT_SEL2) then if HaveEL(EL3) then if !ELUsingAArch32(EL3) && SCR_EL3.EEL2 == '1' then return TRUE; else return FALSE;
```

```
else return else return FALSE;
```

## SecureOnlyImplementation(); J1.3.3.459 LocalTimeoutEvent // LocalTimeoutEvent() // =================== // Returns TRUE if CNTVCT\_EL0 equals or exceeds the localtimeout value. boolean LocalTimeoutEvent(integer localtimeout) assert localtimeout &gt;= 0; constant bits(64) cntvct = VirtualCounterTimer(); if UInt(cntvct) &gt;= localtimeout then return TRUE; IsLocalTimeoutEventPending = TRUE; LocalTimeoutVal = localtimeout&lt;63:0&gt;; // Store value to compare against // Virtual Counter Timer at subsequent clock ticks return FALSE; J1.3.3.460 Mode // Mode bits // ========= // AArch32 PSTATE.M mode bits. constant bits(5) M32\_User = '10000'; constant bits(5) M32\_FIQ = '10001'; constant bits(5) M32\_IRQ = '10010'; constant bits(5) M32\_Svc = '10011'; constant bits(5) M32\_Monitor = '10110'; constant bits(5) M32\_Abort = '10111'; constant bits(5) M32\_Hyp = '11010'; constant bits(5) M32\_Undef = '11011'; constant bits(5) M32\_System = '11111'; J1.3.3.461 NonSecureOnlyImplementation // NonSecureOnlyImplementation() // ============================= // Returns TRUE if the security state is always Non-secure for this implementation. boolean NonSecureOnlyImplementation() return boolean IMPLEMENTATION\_DEFINED "Non-secure only implementation"; J1.3.3.462 PLOfEL

```
// PLOfEL() // ======== PrivilegeLevel PLOfEL(bits(2) el) case el of when EL3 return if !HaveAArch64() then PL1 else when EL2 return PL2; when EL1 return PL1; when EL0 return PL0;
```

```
PL3;
```

## J1.3.3.463 PSTATE

```
// PSTATE // ====== // Global per-processor ProcState PSTATE;
```

```
// ProcState // ========= // PE state bits. // There is no significance to the field order. type ProcState is ( bits (1) N, // Negative condition flag bits (1) Z, // Zero condition flag bits (1) C, // Carry condition flag bits (1) V, // Overflow condition flag bits (1) D, // Debug mask bit [AArch64 only] bits (1) A, // SError interrupt mask bit bits (1) I, // IRQ mask bit bits (1) F, // FIQ mask bit bits (1) EXLOCK, // Lock exception return state bits (1) PAN, // Privileged Access Never Bit [v8.1] bits (1) UAO, // User Access Override [v8.2] bits (1) DIT, // Data Independent Timing [v8.4] bits (1) TCO, // Tag Check Override [v8.5, bits (1) PM, // PMU exception Mask bits (1) PPEND, // synchronous PMU exception to be observed bits (2) BTYPE, // Branch Type [v8.5] bits (1) PACM, // PAC instruction modifier bits (1) ZA, // Accumulation array enabled [SME] bits (1) SM, // Streaming SVE mode enabled [SME] bits (1) ALLINT, // Interrupt mask bit bits (1) UINJ, // Undefined Exception Injection bits (1) SS, // Software step bit bits (1) IL, // Illegal Execution state bit bits (2) EL, // Exception level bits (1) nRW, // Execution state: 0=AArch64, 1=AArch32 bits (1) SP, // Stack pointer select: 0=SP0, 1=SPx [AArch64 only] bits (1) Q, // Cumulative saturation flag [AArch32 only] bits (4) GE, // Greater than or Equal flags [AArch32 only]
```

## state J1.3.3.464 PhysicalCountInt // PhysicalCountInt() // ================== // Returns the integral part of physical count value of the System counter. bits(64) PhysicalCountInt() return PhysicalCount&lt;87:24&gt;; J1.3.3.465 PrivilegeLevel // PrivilegeLevel // ============== // Privilege Level abstraction. enumeration PrivilegeLevel {PL3, PL2, PL1, PL0}; J1.3.3.466 ProcState AArch64 only]

```
bits (1) SSBS, // Speculative Store Bypass Safe bits (8) IT, // If-then bits, RES0 in CPSR [AArch32 only] bits (1) J, // J bit, RES0 [AArch32 only, RES0 in SPSR and CPSR] bits (1) T, // T32 bit, RES0 in CPSR [AArch32 only] bits (1) E, // Endianness bit [AArch32 only] bits (5) M // Mode field [AArch32 only] )
```

## J1.3.3.467 RestoredITBits // RestoredITBits() // ================ // Get the value of PSTATE.IT to be restored on this exception return. bits(8) RestoredITBits(bits(N) spsr) it = spsr&lt;15:10,26:25&gt;; // When PSTATE.IL is set, it is CONSTRAINED UNPREDICTABLE whether the IT bits are each set // to zero or copied from the SPSR. if PSTATE.IL == '1' then if ConstrainUnpredictableBool(Unpredictable\_ILZEROIT) then return '00000000'; else return it; // The IT bits are forced to zero when they are set to a reserved value. if !IsZero(it&lt;7:4&gt;) &amp;&amp; IsZero(it&lt;3:0&gt;) then return '00000000'; // The IT bits are forced to zero when returning to A32 state, or when returning to an EL // with the ITD bit set to 1, and the IT bits are describing a multi-instruction block. itd = if PSTATE.EL == EL2 then HSCTLR.ITD else SCTLR.ITD; if (spsr&lt;5&gt; == '0' &amp;&amp; !IsZero(it)) || (itd == '1' &amp;&amp; !IsZero(it&lt;2:0&gt;)) then return '00000000'; else return it; J1.3.3.468 SecureOnlyImplementation // SecureOnlyImplementation() // ========================== // Returns TRUE if the security state is always Secure for this implementation. boolean SecureOnlyImplementation() return boolean IMPLEMENTATION\_DEFINED "Secure-only implementation"; J1.3.3.469 SecurityState context

```
// SecurityState // ============= // The Security state of an execution enumeration SecurityState { SS_NonSecure, SS_Root, SS_Realm, SS_Secure };
```

## J1.3.3.470 SecurityStateAtEL

```
// SecurityStateAtEL() // =================== // Returns the effective security state at the exception level based off current settings. SecurityState SecurityStateAtEL(bits(2) EL) if IsFeatureImplemented(FEAT_RME) then if EL == EL3 then return SS_Root; effective_nse_ns = EffectiveSCR_EL3_NSE() : EffectiveSCR_EL3_NS(); case effective_nse_ns of when '00' if IsFeatureImplemented(FEAT_SEL2) then return SS_Secure; else Unreachable(); when '01' return SS_NonSecure; when '11' return SS_Realm; otherwise Unreachable(); if !HaveEL(EL3) then if SecureOnlyImplementation() then return SS_Secure; else return SS_NonSecure; elsif EL == EL3 then return SS_Secure; else // For EL2 call only when EL2 is enabled in current security state assert(EL != EL2 || EL2Enabled()); if !ELUsingAArch32(EL3) then return if EffectiveSCR_EL3_NS() == '1' then SS_NonSecure else SS_Secure; else return if SCR.NS == '1' then SS_NonSecure else SS_Secure; J1.3.3.471 SendEvent // SendEvent() // =========== // Signal an event to all PEs in a multiprocessor system to set their Event Registers. // When a PE executes the SEV instruction, it causes this function to be executed. SendEvent(); J1.3.3.472 SendEventLocal to be executed.
```

```
// SendEventLocal() // ================ // Set the local Event Register of this PE. // When a PE executes the SEVL instruction, it causes this function SendEventLocal() EventRegister = '1'; return;
```

## J1.3.3.473 SetAccumulatedFPExceptions

```
// SetAccumulatedFPExceptions() // ============================ // Stores FP Exceptions accumulated by the PE. SetAccumulatedFPExceptions(bits(8) accumulated_exceptions);
```

## J1.3.3.474 SetPSTATEFromPSR

```
// SetPSTATEFromPSR() // ================== SetPSTATEFromPSR(bits(N) spsr) constant boolean illegal_psr_state = IllegalExceptionReturn(spsr); SetPSTATEFromPSR(spsr, illegal_psr_state); // SetPSTATEFromPSR() // ================== // Set PSTATE based on a PSR value SetPSTATEFromPSR(bits(N) spsr_in, boolean illegal_psr_state) bits(N) spsr = spsr_in; constant boolean from_aarch64 = !UsingAArch32(); PSTATE.SS = DebugExceptionReturnSS(spsr); if IsFeatureImplemented(FEAT_SEBEP) then assert N == 64; ExceptionReturnPPEND(ZeroExtend(spsr, 64)); ShouldAdvanceSS = FALSE; if illegal_psr_state then PSTATE.IL = '1'; if IsFeatureImplemented(FEAT_SSBS) then PSTATE.SSBS = bit UNKNOWN; if IsFeatureImplemented(FEAT_BTI) then PSTATE.BTYPE = bits(2) UNKNOWN; if IsFeatureImplemented(FEAT_UAO) then PSTATE.UAO = bit UNKNOWN; if IsFeatureImplemented(FEAT_DIT) then PSTATE.DIT = bit UNKNOWN; if IsFeatureImplemented(FEAT_MTE) then PSTATE.TCO = bit UNKNOWN; if IsFeatureImplemented(FEAT_PAuth_LR) then PSTATE.PACM = bit UNKNOWN; if IsFeatureImplemented(FEAT_UINJ) then PSTATE.UINJ = '0'; else // State that is reinstated only on a legal exception return PSTATE.IL = spsr<20>; if IsFeatureImplemented(FEAT_UINJ) then PSTATE.UINJ = spsr<36>; if spsr<4> == '1' then // AArch32 state AArch32.WriteMode(spsr<4:0>); // Sets PSTATE.EL correctly if IsFeatureImplemented(FEAT_SSBS) then PSTATE.SSBS = spsr<23>; else // AArch64 state PSTATE.nRW = '0'; (-, PSTATE.EL) = ELFromSPSR(spsr); PSTATE.SP = spsr<0>; if IsFeatureImplemented(FEAT_BTI) then PSTATE.BTYPE = spsr<11:10>; if IsFeatureImplemented(FEAT_SSBS) then PSTATE.SSBS = spsr<12>; if IsFeatureImplemented(FEAT_UAO) then PSTATE.UAO = spsr<23>; if IsFeatureImplemented(FEAT_DIT) then PSTATE.DIT = spsr<24>; if IsFeatureImplemented(FEAT_MTE) then PSTATE.TCO = spsr<25>; if IsFeatureImplemented(FEAT_GCS) then PSTATE.EXLOCK = spsr<34>; if IsFeatureImplemented(FEAT_PAuth_LR) then PSTATE.PACM = if IsPACMEnabled() then spsr<35> else '0'; // If PSTATE.IL is set, it is CONSTRAINED UNPREDICTABLE whether the T bit is set to zero or // copied from SPSR. if PSTATE.IL == '1' && PSTATE.nRW == '1' then if ConstrainUnpredictableBool(Unpredictable_ILZEROT) then spsr<5> = '0';
```

```
// State that is reinstated regardless of illegal exception return PSTATE.<N,Z,C,V> = spsr<31:28>; if IsFeatureImplemented(FEAT_PAN) then PSTATE.PAN = spsr<22>; if PSTATE.nRW == '1' then // AArch32 state PSTATE.Q = spsr<27>; PSTATE.IT = RestoredITBits(spsr); ShouldAdvanceIT = FALSE; if IsFeatureImplemented(FEAT_DIT) then PSTATE.DIT = (if (Restarting() || from_aarch64) then spsr<24> else spsr<21>); PSTATE.GE = spsr<19:16>; PSTATE.E = spsr<9>; PSTATE.<A,I,F> = spsr<8:6>; // No PSTATE.D in AArch32 state PSTATE.T = spsr<5>; // PSTATE.J is RES0 else // AArch64 state if (IsFeatureImplemented(FEAT_EBEP) || IsFeatureImplemented(FEAT_SPE_EXC) || IsFeatureImplemented(FEAT_TRBE_EXC)) then PSTATE.PM = spsr<32>; if IsFeatureImplemented(FEAT_NMI) then PSTATE.ALLINT = spsr<13>; PSTATE.<D,A,I,F> = spsr<9:6>; // No PSTATE.<Q,IT,GE,E,T> in AArch64 return;
```

```
state J1.3.3.475 ShouldAdvanceHS // ShouldAdvanceHS // =============== // Cleared if we should not advance the EDESR.SS after the current instruction. boolean ShouldAdvanceHS; J1.3.3.476 ShouldAdvanceIT // ShouldAdvanceIT // =============== // Cleared if we should not advance the PSTATE.IT after the current instruction. boolean ShouldAdvanceIT; J1.3.3.477 ShouldAdvanceSS // ShouldAdvanceSS // =============== // Cleared if PSTATE.SS is written by the current instruction. boolean ShouldAdvanceSS; J1.3.3.478 ShouldSetPPEND
```

```
// ShouldSetPPEND // ============== // TRUE if PSTATE.PPEND is set or cleared at the end of the current instruction, according to // whether a PMU counter configured for synchronous mode overflowed or not. // Otherwise, PSTATE.PPEND is not changed at the end of the instruction. boolean ShouldSetPPEND;
```

## J1.3.3.479 SmallestTranslationGranule

```
// SmallestTranslationGranule() // ============================ // Smallest implemented translation granule. integer SmallestTranslationGranule() if IsFeatureImplemented(FEAT_TGran4K) then return 12; if IsFeatureImplemented(FEAT_TGran16K) then return 14; if IsFeatureImplemented(FEAT_TGran64K) then return Unreachable();
```

## 16; J1.3.3.480 SpeculationBarrier // SpeculationBarrier() // ==================== SpeculationBarrier(); J1.3.3.481 SyncCounterOverflowed // SyncCounterOverflowed // ===================== // Set if a PMU counter configured for synchronous mode has overflowed // during the execution of the current instruction. boolean SyncCounterOverflowed; J1.3.3.482 SynchronizeContext // SynchronizeContext() // ==================== // Context Synchronization event, includes Instruction Fetch Barrier effect SynchronizeContext(); J1.3.3.483 SynchronizeErrors // SynchronizeErrors() // =================== // Implements the error synchronization event. SynchronizeErrors(); J1.3.3.484 TakeUnmaskedPhysicalSErrorInterrupts // TakeUnmaskedPhysicalSErrorInterrupts() // ====================================== // Take any pending unmasked physical SError interrupt. TakeUnmaskedPhysicalSErrorInterrupts(boolean iesb\_req);

## J1.3.3.485 TakeUnmaskedSErrorInterrupts

```
// TakeUnmaskedSErrorInterrupts() // ============================== // Take any pending unmasked physical SError interrupt or unmasked // interrupt. TakeUnmaskedSErrorInterrupts();
```

```
// ValidSecurityStateAtEL() // ======================== // Returns TRUE if the current settings and architecture // implementation permit a valid Security state at the indicated EL. boolean ValidSecurityStateAtEL(bits(2) el) if !HaveEL(el) then return FALSE; if el == EL3 then
```

## virtual SError J1.3.3.486 ThisInstr // ThisInstr() // =========== bits(32) ThisInstr(); J1.3.3.487 ThisInstrLength // ThisInstrLength() // ================= integer ThisInstrLength(); J1.3.3.488 UndefinedInjectionCheck // UndefinedInjectionCheck() // ========================= // Check PSTATE.UINJ to determine if execution of the current // instruction should cause an Undefined exception. UndefinedInjectionCheck() if IsFeatureImplemented(FEAT\_UINJ) &amp;&amp; PSTATE.UINJ == '1' then UNDEFINED; J1.3.3.489 UsingAArch32 // UsingAArch32() // ============== // Return TRUE if the current Exception level is using AArch32, FALSE if using AArch64. boolean UsingAArch32() constant boolean aarch32 = (PSTATE.nRW == '1'); if !HaveAArch32() then assert !aarch32; if !HaveAArch64() then assert aarch32; return aarch32; J1.3.3.490 ValidSecurityStateAtEL choices for this

```
return TRUE; if IsFeatureImplemented(FEAT_RME) then constant bits(2) effective_nse_ns = EffectiveSCR_EL3_NSE() : EffectiveSCR_EL3_NS(); if effective_nse_ns == '10' then return FALSE; if el == EL2 then return EL2Enabled(); return TRUE;
```

## J1.3.3.491 VirtualFIQPending // VirtualFIQPending() // =================== // Returns TRUE if there is any pending virtual FIQ. boolean VirtualFIQPending(); J1.3.3.492 VirtualIRQPending // VirtualIRQPending() // =================== // Returns TRUE if there is any pending virtual IRQ. boolean VirtualIRQPending(); J1.3.3.493 WFxType // WFxType // ======= // WFx instruction types. enumeration WFxType {WFxType\_WFE, WFxType\_WFI, WFxType\_WFET, WFxType\_WFIT}; J1.3.3.494 WaitForEvent // WaitForEvent() // ============== // PE optionally suspends execution until one of the following occurs: // -A WFE wakeup event. // -A reset. // -The implementation chooses to resume execution. // It is IMPLEMENTATION DEFINED whether restarting execution after the period of // suspension causes the Event Register to be cleared. WaitForEvent() if Halted() then return; if !IsEventRegisterSet() then EnterLowPowerState(); return; // WaitForEvent() // ============== // PE optionally suspends execution until one of the following occurs: // -A WFE wakeup event. // -A reset. // -The implementation chooses to resume execution. // -A Wait for Event with Timeout (WFET) is executing, and a local timeout event occurs

```
// It is IMPLEMENTATION DEFINED whether restarting execution after the period // suspension causes the Event Register to be cleared. WaitForEvent(integer localtimeout) if Halted() then return; if !(IsEventRegisterSet() || LocalTimeoutEvent(localtimeout)) then EnterLowPowerState(); return;
```

## J1.3.3.495 WaitForInterrupt

```
// WaitForInterrupt() // ================== // PE optionally suspends execution until one of the following occurs: // -A WFI wakeup event. // -A reset. // -The implementation chooses to resume execution. WaitForInterrupt() if Halted() then return; EnterLowPowerState(); return; // WaitForInterrupt() // ================== // PE optionally suspends execution until one of the following occurs: // -A WFI wakeup event. // -A reset. // -The implementation chooses to resume execution. // -A Wait for Interrupt with Timeout (WFIT) is executing, and a local timeout event occurs. WaitForInterrupt(integer localtimeout) if Halted() then return; if !LocalTimeoutEvent(localtimeout) then EnterLowPowerState(); return;
```

```
J1.3.3.496 WatchpointRelatedSyndrome // WatchpointRelatedSyndrome() // =========================== // Update common Watchpoint related fields. bits(24) WatchpointRelatedSyndrome(FaultRecord fault) bits(24) syndrome = Zeros(24); if fault.watchptinfo.maybe_false_match then syndrome<16> = '1'; // WPF elsif IsFeatureImplemented(FEAT_Debugv8p2) then syndrome<16> = bit IMPLEMENTATION_DEFINED "WPF value on TRUE Watchpoint match"; if IsRelaxedWatchpointAccess(fault.accessdesc) then if HaltOnBreakpointOrWatchpoint() then if boolean IMPLEMENTATION_DEFINED "EDWAR is not valid on watchpoint debug event" then syndrome<10> = '1'; // FnV else if boolean IMPLEMENTATION_DEFINED "FAR is not valid on watchpoint exception" then syndrome<10> = '1'; // FnV else if WatchpointFARNotPrecise(fault) then syndrome<15> = '1'; // FnP // Watchpoint number is valid if FEAT_Debugv8p9 is implemented or
```

```
of
```

```
// if Feat_Debugv8p2 is implemented and below set of conditions are satisfied: // - Either FnV = 1 or FnP = 1. // - If the address recorded in FAR is not within a naturally-aligned block of memory. // Otherwise, it is IMPLEMENTATION DEFINED if watchpoint number is valid. if IsFeatureImplemented(FEAT_Debugv8p9) then syndrome<17> = '1'; // WPTV syndrome<23:18> = fault.watchptinfo.watchpt_num<5:0>; // WPT elsif IsFeatureImplemented(FEAT_Debugv8p2) then if syndrome<15> == '1' || syndrome<10> == '1' then // Either of FnP or FnV is 1 syndrome<17> = '1'; // WPTV elsif !AddressInNaturallyAlignedBlock(fault.vaddress, fault.watchptinfo.vaddress) then syndrome<17> = '1'; // WPTV elsif boolean IMPLEMENTATION_DEFINED "WPTV field is valid" then syndrome<17> = '1'; if syndrome<17> == '1' then syndrome<23:18> = fault.watchptinfo.watchpt_num<5:0>; // WPT else syndrome<23:18> = bits(6) UNKNOWN; return syndrome;
```

```
J1.3.3.497 ASID_NONE constant bits(16) ASID_NONE = Zeros(16); J1.3.3.498 Broadcast // Broadcast // ========= enumeration Broadcast { Broadcast_ISH, Broadcast_ForcedISH, Broadcast_OSH, Broadcast_NSH }; J1.3.3.499 BroadcastTLBI // BroadcastTLBI() // =============== // IMPLEMENTATION DEFINED function to broadcast TLBI operation within the indicated broadcast // domain. BroadcastTLBI(Broadcast broadcast, TLBIRecord r) IMPLEMENTATION_DEFINED; J1.3.3.500 TLBI TRUE.
```

```
// TLBI() // ====== // Invalidates TLB entries for which TLBIMatch() returns TLBI(TLBIRecord r) IMPLEMENTATION_DEFINED;
```

## J1.3.3.501 TLBILevel

```
// TLBILevel // ========= enumeration TLBILevel { TLBILevel_Any, // this applies to TLB entries at all levels TLBILevel_Last // this applies to TLB entries at last level only };
```

## J1.3.3.502 TLBIMemAttr // TLBIMemAttr // =========== // Defines the attributes of the memory operations that must be completed in // order to deem the TLBI operation as completed. enumeration TLBIMemAttr { TLBI\_AllAttr, // All TLB entries within the scope of the invalidation TLBI\_ExcludeXS // Only TLB entries with XS=0 within the scope of the invalidation }; J1.3.3.503 TLBIOp // TLBIOp // ====== enumeration TLBIOp { TLBIOp\_DALL, // AArch32 Data TLBI operations -deprecated TLBIOp\_DASID, TLBIOp\_DVA, TLBIOp\_IALL, // AArch32 Instruction TLBI operations -deprecated TLBIOp\_IASID, TLBIOp\_IVA, TLBIOp\_ALL, TLBIOp\_ASID, TLBIOp\_IPAS2, TLBIPOp\_IPAS2, TLBIOp\_VAA, TLBIOp\_VA, TLBIPOp\_VAA, TLBIPOp\_VA, TLBIOp\_VMALL, TLBIOp\_VMALLS12, TLBIOp\_RIPAS2, TLBIPOp\_RIPAS2, TLBIOp\_RVAA, TLBIOp\_RVA, TLBIPOp\_RVAA, TLBIPOp\_RVA, TLBIOp\_RPA, TLBIOp\_PAALL, TLBIOp\_VMALLWS2 }; J1.3.3.504 TLBIRecord

```
// TLBIRecord // ========== // Details related to a TLBI operation.
```

```
type TLBIRecord is ( TLBIOp op, boolean from_aarch64, // originated as an AArch64 operation SecurityState security, Regime regime, boolean use_vmid, bits(16) vmid, bits(16) asid, TLBILevel level, TLBIMemAttr attr, PASpace ipaspace, // For operations that take IPA as input address bits(64) address, // input address, for range operations, start address bits(64) end_address, // for range operations, end address boolean d64, // For operations that evict VMSAv8-64 based TLB entries boolean d128, // For operations that evict VMSAv9-128 based TLB entries bits(4) ttl, // translation table walk level holding the leaf entry // for the address being invalidated // For Non-Range Invalidations: // When the ttl is // '00xx' : this applies to all TLB entries // Otherwise : TLBIP instructions invalidates D128 TLB // entries only // TLBI instructions invalidates D64 TLB // entries only // For Range Invalidations: // When the ttl is // '00' : this applies to all TLB entries // Otherwise : TLBIP instructions invalidates D128 TLB // entries only // TLBI instructions invalidates D64 TLB // entries only bits(2) tg // for range operations, translation granule )
```

```
// VMID -getter // ============= // Effective VMID. bits(16) VMID[] if EL2Enabled() then if !ELUsingAArch32(EL2) then if IsFeatureImplemented(FEAT_VMID16) && VTCR_EL2.VS == '1' then return VTTBR_EL2.VMID; else return ZeroExtend(VTTBR_EL2.VMID<7:0>, 16); else return ZeroExtend(VTTBR.VMID, 16); elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_SEL2) then return Zeros(16); else return VMID_NONE;
```

J1.3.3.505 VMID J1.3.3.506 VMID\_NONE constant bits(16) VMID\_NONE = Zeros(16);

## J1.3.3.507 ConstrainUnpredictable

```
// ConstrainUnpredictable() // ======================== // Return the appropriate Constraint result to control the caller's behavior. // The return value is IMPLEMENTATION DEFINED within a permitted list for each // UNPREDICTABLE case. // (The permitted list is determined by an assert or case statement at the call site.) Constraint ConstrainUnpredictable(Unpredictable which);
```

## J1.3.3.508 ConstrainUnpredictableBits

```
// ConstrainUnpredictableBits() // ============================ // This is a variant of ConstrainUnpredictable for when the result can be Constraint_UNKNOWN. // If the result is Constraint_UNKNOWN then the function also returns UNKNOWN value, but that // value is always an allocated value; that is, one for which the behavior is not itself // CONSTRAINED. (Constraint,bits(width)) ConstrainUnpredictableBits(Unpredictable which, integer width);
```

## J1.3.3.509 ConstrainUnpredictableBool

```
// ConstrainUnpredictableBool() // ============================ // This is a variant of the ConstrainUnpredictable function where the result is either // Constraint_TRUE or Constraint_FALSE. boolean ConstrainUnpredictableBool(Unpredictable which);
```

## J1.3.3.510 ConstrainUnpredictableInteger

```
// ConstrainUnpredictableInteger() // =============================== // This is a variant of ConstrainUnpredictable for when the result can be Constraint_UNKNOWN. // If the result is Constraint_UNKNOWN then the function also returns an UNKNOWN // value in the range low to high, inclusive. (Constraint,integer) ConstrainUnpredictableInteger(integer low, integer high, Unpredictable which);
```

## J1.3.3.511 ConstrainUnpredictableProcedure

```
// ConstrainUnpredictableProcedure() // ================================= // This is a variant of ConstrainUnpredictable that implements a Constrained // Unpredictable behavior for a given Unpredictable situation. // The behavior is within permitted behaviors for a given Unpredictable situation, // these are documented in the textual part of the architecture specification. // // This function is expected to be refined in an IMPLEMENTATION DEFINED manner. // The details of possible outcomes may not be present in the code and must be interpreted // for each use with respect to the CONSTRAINED UNPREDICTABLE specifications // for the specific area.
```

ConstrainUnpredictableProcedure(Unpredictable which);

## J1.3.3.512 Constraint

```
// Constraint // ========== // List of Constrained Unpredictable behaviors. enumeration Constraint {// General Constraint_NONE, // Instruction executes with // no change or side-effect // to its described behavior Constraint_UNKNOWN, // Destination register // has UNKNOWN value Constraint_UNDEF, // Instruction is UNDEFINED Constraint_UNDEFEL0, // Instruction is UNDEFINED at EL0 only Constraint_NOP, // Instruction executes as NOP Constraint_TRUE, Constraint_FALSE, Constraint_DISABLED, Constraint_UNCOND, // Instruction executes unconditionally Constraint_COND, // Instruction executes conditionally Constraint_ADDITIONAL_DECODE, // Instruction executes // with additional decode // Load-store Constraint_WBSUPPRESS, Constraint_FAULT, Constraint_LIMITED_ATOMICITY, // Accesses are not // single-copy atomic // above the byte level Constraint_NVNV1_00, Constraint_NVNV1_01, Constraint_NVNV1_11, Constraint_EL1TIMESTAMP, // Constrain to Virtual Timestamp Constraint_EL2TIMESTAMP, // Constrain to Virtual Timestamp Constraint_OSH, // Constrain to Outer Shareable Constraint_ISH, // Constrain to Inner Shareable Constraint_NSH, // Constrain to Nonshareable Constraint_NC, // Constrain to Noncacheable Constraint_WT, // Constrain to Writethrough Constraint_WB, // Constrain to Writeback Constraint_RESS, // Bits behave as RESS for all purposes // other than reading back the register Constraint_ALLRESS, // Bits behave as RESS for all purposes // IPA too large Constraint_FORCE, Constraint_FORCENOSLCHECK, // An unallocated System register value maps onto an allocated value Constraint_MAPTOALLOCATED, // PMSCR_PCT reserved values select Virtual timestamp Constraint_PMSCR_PCT_VIRT, Constraint_ANYREG, // Any allocated register is chosen };
```

## J1.3.3.513 Unpredictable

```
// Unpredictable // ============= // List of Constrained Unpredictable situations. enumeration Unpredictable { // VMSR on MVFR Unpredictable_VMSR, // Writeback/transfer register overlap (load) Unpredictable_WBOVERLAPLD,
```

```
// Writeback/transfer register overlap (store) Unpredictable_WBOVERLAPST, // Load Pair transfer register overlap Unpredictable_LDPOVERLAP, // Store-exclusive base/status register overlap Unpredictable_BASEOVERLAP, // Store-exclusive data/status register overlap Unpredictable_DATAOVERLAP, // Load-store alignment checks Unpredictable_DEVPAGE2, // Instruction fetch from Device memory Unpredictable_INSTRDEVICE, // Reserved CPACR value Unpredictable_RESCPACR, // Reserved MAIR value Unpredictable_RESMAIR, // Effect of SCTLR_ELx.C on Tagged attribute Unpredictable_S1CTAGGED, // Reserved Stage 2 MemAttr value Unpredictable_S2RESMEMATTR, // Reserved TEX:C:B value Unpredictable_RESTEXCB, // Reserved PRRR value Unpredictable_RESPRRR, // Reserved DACR field Unpredictable_RESDACR, // Reserved VTCR.S value Unpredictable_RESVTCRS, // Reserved TCR.TnSZ value Unpredictable_RESTnSZ, // Reserved SCTLR_ELx.TCF value Unpredictable_RESTCF, // Tag stored to Device memory Unpredictable_DEVICETAGSTORE, // Out-of-range TCR.TnSZ value Unpredictable_OORTnSZ, // IPA size exceeds PA size Unpredictable_LARGEIPA, // Syndrome for a known-passing conditional A32 instruction Unpredictable_ESRCONDPASS, // Illegal State exception: zero PSTATE.IT Unpredictable_ILZEROIT, // Illegal State exception: zero PSTATE.T Unpredictable_ILZEROT, // Debug: prioritization of Vector Catch Unpredictable_BPVECTORCATCHPRI, // Debug Vector Catch: match on 2nd halfword Unpredictable_VCMATCHHALF, // Debug Vector Catch: match on Data Abort // or Prefetch abort Unpredictable_VCMATCHDAPA, // Debug watchpoints: nonzero MASK and non-ones BAS Unpredictable_WPMASKANDBAS, // Debug watchpoints: non-contiguous BAS Unpredictable_WPBASCONTIGUOUS, // Debug watchpoints: reserved MASK Unpredictable_RESWPMASK, // Debug watchpoints: nonzero MASKed bits of address Unpredictable_WPMASKEDBITS, // Debug breakpoints and watchpoints: reserved control bits Unpredictable_RESBPWPCTRL, // Debug breakpoints: not implemented Unpredictable_BPNOTIMPL, // Debug breakpoints: reserved type Unpredictable_RESBPTYPE,
```

```
// Debug breakpoints and watchpoints: reserved MDSELR_EL1.BANK Unpredictable_RESMDSELR, // Debug breakpoints: not-context-aware breakpoint Unpredictable_BPNOTCTXCMP, // Debug breakpoints: match on 2nd halfword of instruction Unpredictable_BPMATCHHALF, // Debug breakpoints: mismatch on 2nd halfword of instruction Unpredictable_BPMISMATCHHALF, // Debug breakpoints: a breakpoint is linked to that is not // programmed with linking enabled Unpredictable_BPLINKINGDISABLED, // Debug breakpoints: reserved MASK Unpredictable_RESBPMASK, // Debug breakpoints: MASK is set for a Context matching // breakpoint or when DBGBCR_EL1[n].BAS != '1111' Unpredictable_BPMASK, // Debug breakpoints: nonzero MASKed bits of address Unpredictable_BPMASKEDBITS, // Debug breakpoints: A linked breakpoint is // linked to an address matching breakpoint Unpredictable_BPLINKEDADDRMATCH, // Debug: restart to a misaligned AArch32 PC value Unpredictable_RESTARTALIGNPC, // Debug: restart to a not-zero-extended AArch32 PC value Unpredictable_RESTARTZEROUPPERPC, // Zero top 32 bits of X registers in AArch32 state Unpredictable_ZEROUPPER, // Zero top 32 bits of PC on illegal return to // AArch32 state Unpredictable_ERETZEROUPPERPC, // Force address to be aligned when interworking // branch to A32 state Unpredictable_A32FORCEALIGNPC, // SMC disabled Unpredictable_SMD, // FF speculation Unpredictable_NONFAULT, // Zero top bits of Z registers in EL change Unpredictable_SVEZEROUPPER, // Load mem data in NF loads Unpredictable_SVELDNFDATA, // Write zeros in NF loads Unpredictable_SVELDNFZERO, // SP alignment fault when predicate is all zero Unpredictable_CHECKSPNONEACTIVE, // Zero top bits of ZA registers in EL change Unpredictable_SMEZEROUPPER, // Watchpoint match of last rounded up memory access in case of // 16 byte rounding Unpredictable_16BYTEROUNDEDUPACCESS, // Watchpoint match of first rounded down memory access in case of // 16 byte rounding Unpredictable_16BYTEROUNDEDDOWNACCESS, // HCR_EL2.<NV,NV1> == '01' Unpredictable_NVNV1, // Upper bits of a BADDR are not RESS Unpredictable_BADDR_RESS, // Reserved shareability encoding Unpredictable_Shareability, // Access Flag Update by HW Unpredictable_AFUPDATE, // Dirty Bit State Update by HW Unpredictable_DBUPDATE, // Consider SCTLR_ELx[].IESB in Debug state Unpredictable_IESBinDebug, // Bad settings for PMSFCR_EL1/PMSEVFR_EL1/PMSLATFR_EL1
```

```
Unpredictable_BADPMSFCR, // Zero saved BType value in SPSR_ELx/DPSR_EL0 Unpredictable_ZEROBTYPE, // Timestamp constrained to virtual or physical Unpredictable_EL2TIMESTAMP, Unpredictable_EL1TIMESTAMP, // Reserved MDCR_EL3.<NSTBE,NSTB> or MDCR_EL3.<NSPBE,NSPB> value Unpredictable_RESERVEDNSxB, Unpredictable_RESERVEDNSxB_Trap, // WFET or WFIT instruction in Debug state Unpredictable_WFxTDEBUG, // Address does not support LS64 instructions Unpredictable_LS64UNSUPPORTED, // Unaligned exclusives, atomics, acquire/release // to a region that is not to Normal inner write-back // outer write-back shareable generate an Alignment fault. Unpredictable_LSE2_ALIGNMENT_FAULT, // 128-bit Atomic or 128-bit RCW{S} transfer register overlap Unpredictable_LSE128OVERLAP, // Clearing DCC/ITR sticky flags when instruction is in flight Unpredictable_CLEARERRITEZERO, // ALUEXCEPTIONRETURN when in user/system mode in // A32 instructions Unpredictable_ALUEXCEPTIONRETURN, // Trap to register in debug state are ignored Unpredictable_IGNORETRAPINDEBUG, // Compare DBGBVR.RESS for BP/WP Unpredictable_DBGxVR_RESS, // Inaccessible event counter Unpredictable_PMUEVENTCOUNTER, // Reserved PMSCR.PCT behavior Unpredictable_PMSCR_PCT, // MDCR_EL2.HPMN or HDCR.HPMN is larger than PMCR.N or // FEAT_HPMN0 is not implemented and HPMN is 0. Unpredictable_RES_HPMN, // Chained PMU counters idx and idx+1 are not in same range Unpredictable_COUNT_CHAIN, // PMCCR.EPMN is larger than PMCR.N Unpredictable_RES_EPMN, // Generate BRB_FILTRATE event on BRB injection Unpredictable_BRBFILTRATE, // Generate PMU_SNAPSHOT event in Debug state Unpredictable_PMUSNAPSHOTEVENT, // Reserved MDCR_EL3.EPMSSAD value Unpredictable_RESEPMSSAD, // Reserved PMECR_EL1.SSE value Unpredictable_RESPMSSE, // Enable for PMU Profiling exception and PMUIRQ Unpredictable_RESPMEE, // Enables for SPE Profiling exceptions and PMSIRQ Unpredictable_RESPMSEE, // Enables for TRBE Profiling exceptions and PMSIRQ Unpredictable_RESTRFEE, // Operands for CPY*/SET* instructions overlap Unpredictable_MOPSOVERLAP, // Operands for CPY*/SET* instructions use 0b11111 // as a register specifier Unpredictable_MOPS_R31, // Chooses which value to return in a non failed Atomic Compare and Swap Unpredictable_CASRETURNOLDVALUE, // Enables write of the newvalue in a failed Atomic Compare and Swap Unpredictable_WRITEFAILEDCAS, // Store-only Tag checking on a failed Atomic Compare and Swap Unpredictable_STRONLYTAGCHECKEDCAS, // Store-only Tag checking on a failed RCW(S) checks // or RCW(S) Atomic Compare and Swap
```

};

## J1.3.3.514 AdvSIMDExpandImm

```
// AdvSIMDExpandImm() // ================== bits(64) AdvSIMDExpandImm(bit op, bits(4) cmode, bits(8) imm8) bits(64) imm64; case cmode<3:1> of when '000' imm64 = Replicate(Zeros(24):imm8, 2); when '001' imm64 = Replicate(Zeros(16):imm8:Zeros(8), 2); when '010' imm64 = Replicate(Zeros(8):imm8:Zeros(16), 2); when '011' imm64 = Replicate(imm8:Zeros(24), 2); when '100' imm64 = Replicate(Zeros(8):imm8, 4); when '101' imm64 = Replicate(imm8:Zeros(8), 4); when '110' if cmode<0> == '0' then imm64 = Replicate(Zeros(16):imm8:Ones(8), 2); else imm64 = Replicate(Zeros(8):imm8:Ones(16), 2); when '111' if cmode<0> == '0' && op == '0' then imm64 = Replicate(imm8, 8); if cmode<0> == '0' && op == '1' then imm8a = Replicate(imm8<7>, 8); imm8b = Replicate(imm8<6>, 8); imm8c = Replicate(imm8<5>, 8); imm8d = Replicate(imm8<4>, 8); imm8e = Replicate(imm8<3>, 8); imm8f = Replicate(imm8<2>, 8); imm8g = Replicate(imm8<1>, 8); imm8h = Replicate(imm8<0>, 8);
```

```
Unpredictable_STRONLYTAGCHECKEDRCWSCAS, // Reserved MDCR_EL3.ETBAD value Unpredictable_RES_ETBAD, // Invalid Streaming Mode filter bits Unpredictable_RES_PMU_VS, // Apply Checked Pointer Arithmetic on a sequential access to bytes // that cross the 0xXXFF_FFFF_FFFF_FFFF boundary. Unpredictable_CPACHECK, // Reserved PMEVTYPER<n>_EL0.{TC,TE,TC2} values Unpredictable_RESTC, // When FEAT_MTE is implemented, if Memory access mode is enabled // and PSTATE.TCO is 0, Reads and writes to the external debug // interface DTR registers are CONSTRAINED UNPREDICTABLE for tagcheck Unpredictable_NODTRTAGCHK, // Use the default PMG when the default PARTID is generated // due to MPAM error Unpredictable_USE_DEFAULT_PMG, // If the atomic instructions are not atomic in regard to other // agents that access memory, then the instruction can have one or // more of the following effects Unpredictable_Atomic_SYNC_ABORT, Unpredictable_Atomic_SERROR, Unpredictable_Atomic_NOP, Unpredictable_Atomic_MMU_IMPDEF_FAULT, // Accessing DBGDSCRint via MRC in debug state Unpredictable_MRC_APSR_TARGET, // Accessing Banked register not accessible from the PE mode Unpredictable_BankedRegister, // Accessing unimplemented Banked register Unpredictable_UnimplementedRegister,
```

```
imm64 = imm8a:imm8b:imm8c:imm8d:imm8e:imm8f:imm8g:imm8h; if cmode<0> == '1' && op == '0' then imm32 = imm64 = Replicate(imm32, 2); if cmode<0> == '1' && op == '1' then if UsingAArch32() then ReservedEncoding(); imm64 = return imm64;
```

```
imm8<7>:NOT(imm8<6>):Replicate(imm8<6>, 5):imm8<5:0>:Zeros(19); imm8<7>:NOT(imm8<6>):Replicate(imm8<6>, 8):imm8<5:0>:Zeros(48); J1.3.3.515 MatMulAdd // MatMulAdd() // =========== // // Signed or unsigned 8-bit integer matrix multiply and add to 32-bit integer matrix // result[2, 2] = addend[2, 2] + (op1[2, 8] * op2[8, 2]) bits(128) MatMulAdd(bits(128) addend, bits(128) op1, bits(128) op2, boolean op1_unsigned, boolean op2_unsigned) bits(128) result; bits(32) sum; integer prod; for i = 0 to 1 for j = 0 to 1 sum = Elem[addend, 2*i + j, 32]; for k = 0 to 7 constant bits(8) opelt1 = Elem[op1, 8*i + k, 8]; constant bits(8) opelt2 = Elem[op2, 8*j + k, 8]; constant integer element1 = if op1_unsigned then UInt(opelt1) else SInt(opelt1); constant integer element2 = if op2_unsigned then UInt(opelt2) else SInt(opelt2); prod = element1 * element2; sum = sum + prod; Elem[result, 2*i + j, 32] = sum; return result; J1.3.3.516 PolynomialMult // PolynomialMult() // ================ bits(M+N) PolynomialMult(bits(M) op1, bits(N) op2) result = Zeros(M+N); extended_op2 = ZeroExtend(op2, M+N); for i=0 to M-1 if op1<i> == '1' then result = result EOR LSL(extended_op2, i); return result; J1.3.3.517 SatQ // SatQ() // ====== (bits(N), boolean) SatQ(integer i, integer N, boolean unsigned) (result, sat) = if unsigned then UnsignedSatQ(i, N) else SignedSatQ(i, N); return (result, sat);
```

## J1.3.3.518 ShiftSat

```
// ShiftSat() // ========== integer ShiftSat(integer shift, integer esize) if shift > esize+1 then return esize+1; elsif shift < -(esize+1) then return -(esize+1); return shift;
```

## J1.3.3.519 SignedSat

```
// SignedSat() // =========== bits(N) SignedSat(integer i, integer N) (result, -) = SignedSatQ(i, N); return result;
```

## J1.3.3.520 SignedSatQ

```
// SignedSatQ() // ============ (bits(N), boolean) SignedSatQ(integer i, integer N) integer result; boolean saturated; if i > 2^(N-1) 1 then result = 2^(N-1) 1; saturated = TRUE; elsif i < -(2^(N-1)) then result = -(2^(N-1)); saturated = TRUE; else result = i; saturated = FALSE; return (result<N-1:0>, saturated);
```

## J1.3.3.521 UnsignedRSqrtEstimate

```
// UnsignedRSqrtEstimate() // ======================= bits(N) UnsignedRSqrtEstimate(bits(N) operand) assert N == 32; bits(N) result; if operand<N-1:N-2> == '00' then // Operands <= 0x3FFFFFFF produce 0xFFFFFFFF result = Ones(N); else // input is in the range 0x40000000 .. 0xffffffff representing [0.25 .. 1.0) // estimate is in the range 256 .. 511 representing [1.0 .. 2.0) increasedprecision = FALSE; estimate = RecipSqrtEstimate(UInt(operand<31:23>), increasedprecision); // result is in the range 0x80000000 .. 0xff800000 representing [1.0 .. 2.0) result = estimate<8:0> : Zeros(N-9); return result;
```

## J1.3.3.522 UnsignedRecipEstimate

```
// UnsignedRecipEstimate() // ======================= bits(N) UnsignedRecipEstimate(bits(N) operand) assert N == 32; bits(N) result; if operand<N-1> == '0' then // Operands <= 0x7FFFFFFF produce 0xFFFFFFFF result = Ones(N); else // input is in the range 0x80000000 .. 0xffffffff representing [0.5 .. 1.0) // estimate is in the range 256 to 511 representing [1.0 .. 2.0) increasedprecision = FALSE; estimate = RecipEstimate(UInt(operand<31:23>), increasedprecision); // result is in the range 0x80000000 .. 0xff800000 representing [1.0 .. 2.0) result = estimate<8:0> : Zeros(N-9); return result;
```

## J1.3.3.523 UnsignedSat

```
// UnsignedSat() // ============= bits(N) UnsignedSat(integer i, integer (result, -) = UnsignedSatQ(i, N); return result;
```

```
N)
```

## J1.3.3.524 UnsignedSatQ

```
// UnsignedSatQ() // ============== (bits(N), boolean) UnsignedSatQ(integer i, integer N) integer result; boolean saturated; if i > 2^N - 1 then result = 2^N - 1; saturated = TRUE; elsif i < 0 then result = 0; saturated = TRUE; else result = i; saturated = FALSE; return (result<N-1:0>, saturated);
```

## J1.3.4 shared/trace

This section includes the following pseudocode functions:

- DebugMemWrite
- DebugWriteExternalAbort
- DebugWriteFault
- GetTimestamp
- PhysicalOffsetIsValid
- TRBCRManStopWrite
- BranchNotTaken

- AllowExternalTraceBufferAccess
- CheckForTRBEException
- CheckMDCR\_EL3\_NSTBTrap
- CollectTrace
- DefaultTRBEEvent
- DetectedTraceTrigger
- EffectiveMDCR\_EL3\_NSTB
- EffectiveTRBLIMITR\_EL1\_nVM
- EffectiveTRFCR\_EL1\_EE
- EffectiveTRFCR\_EL2\_EE
- GetTRBSR\_EL1\_FSC
- GetTRBSR\_EL2\_FSC
- GetTRBSR\_EL3\_FSC
- HaveImpDefTraceOutput
- ImpDefTraceOutput
- OtherTRBEManagementEvent
- ReportTRBEEvent
- ReportTRBEManagementEvent
- TRBEInternalBufferFull
- TRBEInterruptEnabled
- TRBE\_TRBIDR\_P\_Read
- TRBSR\_EL
- TraceBufferEnabled
- TraceBufferOwner
- TraceBufferRunning
- TraceUnitFlushOnTriggerComplete
- TryAssertTRBIRQ
- TraceInstrumentationAllowed
- TraceUnitFlush
- EffectiveE0HTRE
- EffectiveE0TRE
- EffectiveE1TRE
- EffectiveE2TRE
- SelfHostedTraceEnabled
- TraceAllowed
- TraceContextIDR2
- TraceSynchronizationBarrier
- TraceTimeStamp
- IsTraceCorePowered

## J1.3.4.1 DebugMemWrite

```
// DebugMemWrite() // =============== // Write data to memory one byte at a time. Starting at the passed virtual address. // Used by SPE and TRBE. (PhysMemRetStatus, AddressDescriptor) DebugMemWrite(bits(64) vaddress, AccessDescriptor accdesc, boolean aligned, bits(8) data)
```

```
PhysMemRetStatus memstatus = PhysMemRetStatus UNKNOWN; // Translate virtual address AddressDescriptor addrdesc; constant integer size = 1; addrdesc = AArch64.TranslateAddress(vaddress, accdesc, aligned, size); if IsFault(addrdesc) then return (memstatus, addrdesc); memstatus = PhysMemWrite(addrdesc, 1, accdesc, data); return (memstatus, addrdesc);
```

## J1.3.4.2 DebugWriteExternalAbort

```
// DebugWriteExternalAbort() // ========================= // Populate the syndrome register for an External abort caused by a call of DebugMemWrite(). DebugWriteExternalAbort(PhysMemRetStatus memstatus, AddressDescriptor addrdesc, bits(64) start_vaddr) constant boolean iswrite = TRUE; boolean handle_as_SError = FALSE; case addrdesc.fault.accessdesc.acctype of when AccessType_SPE handle_as_SError = boolean IMPLEMENTATION_DEFINED "Report SPE ExtAbort as SError"; when AccessType_TRBE handle_as_SError = boolean IMPLEMENTATION_DEFINED "Report TRBE ExtAbort as SError"; otherwise Unreachable(); constant boolean ttw_abort = addrdesc.fault.statuscode IN {Fault_SyncExternalOnWalk, Fault_SyncParityOnWalk}; constant Fault statuscode = (if ttw_abort then addrdesc.fault.statuscode else memstatus.statuscode); if statuscode IN {Fault_AsyncExternal, Fault_AsyncParity} || handle_as_SError then // Report the abort as an SError FaultRecord fault = NoFault(); constant boolean parity = statuscode IN {Fault_SyncParity, Fault_AsyncParity, Fault_SyncParityOnWalk}; fault.statuscode = if parity then Fault_AsyncParity else Fault_AsyncExternal; if IsFeatureImplemented(FEAT_RAS) then fault.merrorstate = memstatus.merrorstate; constant bit extflag = if ttw_abort then addrdesc.fault.extflag else memstatus.extflag; fault.extflag = extflag; fault.accessdesc.acctype = addrdesc.fault.accessdesc.acctype; PendSErrorInterrupt(fault); return; // Generate a buffer management event, modifying the existing syndrome. boolean handle_async = FALSE; bits(64) syndrome; case addrdesc.fault.accessdesc.acctype of when AccessType_SPE handle_async = boolean IMPLEMENTATION_DEFINED "Report SPE ExtAbort asynchronously"; assert !IsFeatureImplemented(FEAT_SPE_EXC); syndrome = PMBSR_EL1; when AccessType_TRBE handle_async = boolean IMPLEMENTATION_DEFINED "Report TRBE ExtAbort asynchronously"; assert !IsFeatureImplemented(FEAT_TRBE_EXC);
```

```
syndrome = TRBSR_EL1; otherwise Unreachable(); bits(6) ec; if (IsFeatureImplemented(FEAT_RME) && addrdesc.fault.gpcf.gpf != GPCF_None && addrdesc.fault.gpcf.gpf != GPCF_Fail) then ec = '011110'; else ec = if addrdesc.fault.secondstage then '100101' else '100100'; constant bits(24) mss2 = Zeros(24); bits(16) mss = Zeros(16); if handle_async then // FSC bits mss<5:0> = '010001'; else mss<5:0> = EncodeLDFSC(statuscode, addrdesc.fault.level); // The following values are always updated in the syndrome register. if (addrdesc.fault.accessdesc.acctype == AccessType_SPE && (handle_async || start_vaddr != addrdesc.vaddress)) then syndrome<19> = '1'; // DL bit (SPE only) syndrome<18> = '1'; // EA bit // The following values are not modified if a previous buffer management event // has not been handled. Note that in this simple sequential model, this test // will never fail. if syndrome<17> == '0' then // Check previous 'S' bit. syndrome<55:32> = mss2; // MSS2 bits syndrome<31:26> = ec; // EC bits if addrdesc.fault.accessdesc.acctype == AccessType_TRBE then syndrome<22> = '1'; // IRQ bit (TRBE only) syndrome<17> = '1'; // S bit syndrome<15:0> = mss; // MSS bits case addrdesc.fault.accessdesc.acctype of when AccessType_SPE PMBSR_EL1 = syndrome; when AccessType_TRBE TRBSR_EL1 = syndrome; otherwise Unreachable();
```

## J1.3.4.3 DebugWriteFault

```
// DebugWriteFault() // ================= // Populate the syndrome register for a fault caused by a call of DebugMemWrite(). DebugWriteFault(bits(64) vaddress, FaultRecord fault) bits(6) ec; if (IsFeatureImplemented(FEAT_RME) && fault.gpcf.gpf != GPCF_None && fault.gpcf.gpf != GPCF_Fail) then ec = '011110'; else ec = if fault.secondstage then '100101' else '100100'; bits(24) mss2 = Zeros(24); if fault.statuscode == Fault_Permission then mss2<8> = if fault.toplevel then '1' else '0'; // TopLevel bit mss2<7> = if fault.assuredonly then '1' else '0'; // AssuredOnly bit mss2<6> = if fault.overlay then '1' else '0'; // Overlay bit mss2<5> = if fault.dirtybit then '1' else '0'; // DirtyBit
```

```
bits(16) mss = Zeros(16); if !(IsFeatureImplemented(FEAT_RME) && fault.gpcf.gpf != GPCF_None && fault.gpcf.gpf != GPCF_Fail) then mss<5:0> = EncodeLDFSC(fault.statuscode, fault.level); // FSC bits // Generate a buffer management event, modifying the existing syndrome. bits(2) target_el; bits(64) syndrome; case fault.accessdesc.acctype of when AccessType_SPE target_el = ReportSPEEvent(ec, mss<5:0>); syndrome = PMBSR_EL[target_el]; when AccessType_TRBE target_el = ReportTRBEEvent(ec, mss<5:0>); syndrome = TRBSR_EL[target_el]; otherwise Unreachable(); // The following values are not modified if a previous buffer management event // has not been handled. Note that in this simple sequential model, this test // will never fail. if syndrome<17> == '0' then // Check previous 'S' bit. syndrome<55:32> = mss2; // MSS2 bits syndrome<31:26> = ec; // EC bits if fault.accessdesc.acctype == AccessType_TRBE then syndrome<22> = '1'; // IRQ bit (TRBE only) syndrome<17> = '1'; // S bit syndrome<15:0> = mss; // MSS bits // For SPE, PMBPTR_EL1 points to the address that generated the fault, and writing // to memory never started. Therefore, there isno data loss and DL is unchanged. case fault.accessdesc.acctype of when AccessType_SPE PMBSR_EL[target_el] = syndrome; when AccessType_TRBE TRBSR_EL[target_el] = syndrome; otherwise Unreachable(); return;
```

## J1.3.4.4 GetTimestamp

```
// GetTimestamp() // ============== // Returns the Timestamp depending on the type bits(64) GetTimestamp(TimeStamp timeStampType) case timeStampType of when TimeStamp_Physical return PhysicalCountInt(); when TimeStamp_Virtual return PhysicalCountInt() -CNTVOFF_EL2; when TimeStamp_OffsetPhysical constant bits(64) physoff = if PhysicalOffsetIsValid() then CNTPOFF_EL2 else Zeros(64); return PhysicalCountInt() physoff; when TimeStamp_None return Zeros(64); when TimeStamp_CoreSight return bits(64) IMPLEMENTATION_DEFINED "CoreSight timestamp"; otherwise Unreachable();
```

## J1.3.4.5 PhysicalOffsetIsValid

```
// PhysicalOffsetIsValid() // ======================= // Returns whether the Physical offset for the timestamp is valid boolean PhysicalOffsetIsValid() if !HaveAArch64() then return FALSE; elsif !HaveEL(EL2) || !IsFeatureImplemented(FEAT_ECV_POFF) then return FALSE; elsif HaveEL(EL3) && EffectiveSCR_EL3_NS() == '1' && EffectiveSCR_EL3_RW() == '0' then return FALSE; elsif HaveEL(EL3) && SCR_EL3.ECVEn == '0' then return FALSE; elsif CNTHCTL_EL2.ECV == '0' then return FALSE; else return TRUE;
```

## J1.3.4.6 TRBCRManStopWrite

```
TRBCR.ManStop.
```

```
// TRBCRManStopWrite() // =================== // Called on a write of 1 to TRBCRManStopWrite() TraceUnitFlush(); OtherTRBEManagementEvent('000011'); TryAssertTRBIRQ();
```

## J1.3.4.7 BranchNotTaken

```
// BranchNotTaken() // ================ // Called when a branch is not taken. BranchNotTaken(BranchType branchtype, boolean branch_conditional) constant boolean branchtaken = FALSE; if IsFeatureImplemented(FEAT_SPE) then SPEBranch(bits(64) UNKNOWN, branchtype, branch_conditional, branchtaken); return;
```

## J1.3.4.8 AllowExternalTraceBufferAccess

```
// AllowExternalTraceBufferAccess() // ================================ // Returns TRUE if an external debug interface access to the Trace Buffer // registers is allowed for the given Security state, FALSE otherwise. // The access may also be subject to OS Lock, power-down, etc. boolean AllowExternalTraceBufferAccess(AddressDescriptor addrdesc) assert IsFeatureImplemented(FEAT_TRBE_EXT); // FEAT_Debugv8p4 is always implemented when FEAT_TRBE_EXT is implemented. assert IsFeatureImplemented(FEAT_Debugv8p4); bits(2) etbad = if HaveEL(EL3) then MDCR_EL3.ETBAD else '11';
```

```
// Check for reserved values if !IsFeatureImplemented(FEAT_RME) && etbad IN {'01','10'} then (-, etbad) = ConstrainUnpredictableBits(Unpredictable_RES_ETBAD, 2); // The value returned by ConstrainUnpredictableBits must be a // non-reserved value assert etbad IN {'00', '11'}; case etbad of when '00' if IsFeatureImplemented(FEAT_RME) then return addrdesc.paddress.paspace == PAS_Root; else return addrdesc.paddress.paspace == PAS_Secure; when '01' assert IsFeatureImplemented(FEAT_RME); return addrdesc.paddress.paspace IN {PAS_Root, PAS_Realm}; when '10' assert IsFeatureImplemented(FEAT_RME); return addrdesc.paddress.paspace IN {PAS_Root, PAS_Secure}; when '11' return TRUE;
```

## J1.3.4.9

```
CheckForTRBEException
```

```
// CheckForTRBEException() // ======================= // Take a TRBE Profiling exception if pending, permitted, and unmasked. CheckForTRBEException() if !IsFeatureImplemented(FEAT_TRBE_EXC) || !SelfHostedTraceEnabled() then return; if Halted() || Restarting() then return; boolean route_to_el3 = FALSE; boolean route_to_el2 = FALSE; boolean route_to_el1 = FALSE; if HaveEL(EL3) && MDCR_EL3.TRBEE == '1x' then constant boolean pending = TRBSR_EL3.IRQ == '1'; constant boolean masked = PSTATE.EL == EL3; route_to_el3 = pending && !masked; SecurityState owning_ss; bits(2) owning_el; (owning_ss, owning_el) = TraceBufferOwner(); constant boolean in_owning_ss = IsCurrentSecurityState(owning_ss); if EffectiveTRFCR_EL2_EE() IN {'1x'} then constant boolean pending = TRBSR_EL2.IRQ == '1'; constant boolean masked = (!in_owning_ss || PSTATE.EL == EL3 || (PSTATE.EL == EL2 && (TRFCR_EL2.EE != '11' || TRFCR_EL2.KE == '0' || PSTATE.PM == '1'))); route_to_el2 = pending && !masked; if EffectiveTRFCR_EL1_EE() == '11' then constant boolean pending = TRBSR_EL1.IRQ == '1'; constant boolean masked = (!in_owning_ss || PSTATE.EL IN {EL3, EL2} || (PSTATE.EL == EL1 && (TRFCR_EL1.KE == '0' || PSTATE.PM == '1'))); if EffectiveTGE() == '1' then route_to_el2 = route_to_el2 || (pending && !masked); else route_to_el1 = pending && !masked;
```

```
constant bits(5) fsc = '00010'; // TRBE exception constant boolean synchronous = FALSE; // The relative priorities of the following checks is IMPLEMENTATION DEFINED if route_to_el3 then TakeProfilingException(EL3, fsc, synchronous); if route_to_el2 then TakeProfilingException(EL2, fsc, synchronous); if route_to_el1 then TakeProfilingException(EL1, fsc, synchronous);
```

## J1.3.4.10 CheckMDCR\_EL3\_NSTBTrap

```
// CheckMDCR_EL3_NSTBTrap() // ======================== // Check if the register access is trappable by MDCR_EL3.<NSTBE, NSTB> boolean CheckMDCR_EL3_NSTBTrap() bits(3) state_bits; boolean reserved; (state_bits, reserved) = EffectiveMDCR_EL3_NSTB(); return ((reserved && ConstrainUnpredictableBool(Unpredictable_RESERVEDNSxB_Trap)) || state_bits[0] == '0' || state_bits[1] != SCR_EL3.NS || (IsFeatureImplemented(FEAT_RME) && state_bits[2] != SCR_EL3.NSE));
```

## J1.3.4.11 CollectTrace

```
// CollectTrace() // ============== // Called for each byte generated by the trace unit. // Returns TRUE if the Trace Buffer Unit accepts or discards the trace // data, and FALSE if the Trace Buffer Unit rejects the trace data. boolean CollectTrace(bits(8) datum) if !TraceBufferEnabled() then // Trace buffer disabled // 'datum' is discarded if HaveImpDefTraceOutput() then return ImpDefTraceOutput(datum); else return TRUE; // Discard the trace byte // If the TRBE cannot accept the trace data, it must return FALSE if TRBEInternalBufferFull() then return FALSE; if TraceBufferRunning() then // Accept the data constant bits(64) address = TRBPTR_EL1; boolean ttw_abort = FALSE; constant boolean ttw_abort_as_fault = (boolean IMPLEMENTATION_DEFINED "Report TRBE ExtAbort on TTW as fault"); AddressDescriptor addrdesc; PhysMemRetStatus memstatus; if !SelfHostedTraceEnabled() then // The Trace Buffer Unit is using External mode. if IsFeatureImplemented(FEAT_RME) && !ExternalRootInvasiveDebugEnabled() then if IsZero(GPCCR_EL3.<TBGPCD, GPC>) then return FALSE; constant bits(2) pas = TRBMAR_EL1.PAS; constant PASpace paspace = DecodePASpace('0', pas<1>, pas<0>); boolean valid_config = IsPASValid(pas) && InvasiveDebugPermittedPAS(paspace); if IsFeatureImplemented(FEAT_TRBE_MPAM) && TRBMPAM_EL1.EN == '1' then
```

```
constant bits(2) mpam_sp = TRBMPAM_EL1.MPAM_SP; constant PASpace mpam_pa = DecodePASpace('0', mpam_sp<1>, mpam_sp<0>); valid_config = (valid_config && IsPASValid(mpam_sp) && InvasiveDebugPermittedPAS(mpam_pa)); if !valid_config then OtherTRBEManagementEvent('000000'); TryAssertTRBIRQ(); return TRUE; constant bits(2) el = bits(2) UNKNOWN; constant SecurityState ss = SecurityState UNKNOWN; constant AccessDescriptor accdesc = CreateAccDescTRBE(ss, el); FullAddress pa; pa.address = address<55:0>; pa.paspace = paspace; constant MemoryAttributes memattrs = S1DecodeMemAttrs(TRBMAR_EL1.Attr, TRBMAR_EL1.SH, TRUE); addrdesc = CreateAddressDescriptor(pa, memattrs, accdesc); addrdesc.mecid = DEFAULT_MECID; if IsFeatureImplemented(FEAT_RME) && !ExternalRootInvasiveDebugEnabled() then constant GPCFRecord gpcf = GranuleProtectionCheck(addrdesc, accdesc); if gpcf.gpf == GPCF_None then memstatus = PhysMemWrite(addrdesc, 1, accdesc, datum); else addrdesc.fault.gpcf = gpcf; addrdesc.fault.statuscode = Fault_GPCFOnOutput; else memstatus = PhysMemWrite(addrdesc, 1, accdesc, datum); else // The Trace Buffer Unit is using Self-hosted mode. SecurityState owning_ss; bits(2) owning_el; (owning_ss, owning_el) = TraceBufferOwner(); constant AccessDescriptor accdesc = CreateAccDescTRBE(owning_ss, owning_el); constant boolean aligned = TRUE; (memstatus, addrdesc) = DebugMemWrite(address, accdesc, aligned, datum); ttw_abort = addrdesc.fault.statuscode IN {Fault_SyncExternalOnWalk, Fault_SyncParityOnWalk}; if IsFault(addrdesc.fault.statuscode) && (!ttw_abort || ttw_abort_as_fault) then DebugWriteFault(address, addrdesc.fault); TryAssertTRBIRQ(); return TRUE; elsif IsFault(memstatus) || (ttw_abort && !ttw_abort_as_fault) then DebugWriteExternalAbort(memstatus, addrdesc, address); TryAssertTRBIRQ(); return TRUE; // Check for Trigger Event constant bits(2) target_el = DefaultTRBEEvent(); constant boolean triggered = TRBSR_EL[target_el].TRG == '1'; if triggered && !IsZero(TRBTRG_EL1.TRG) then TRBTRG_EL1.TRG = (TRBTRG_EL1.TRG - 1)<31:0>; if IsZero(TRBTRG_EL1.TRG) && TRBLIMITR_EL1.TM != '11' then TraceUnitFlush(); TraceUnitFlushOnTriggerComplete(); // Increment the pointer next_address = TRBPTR_EL1 + 1; if next_address<63:12> == TRBLIMITR_EL1.LIMIT then next_address = TRBBASER_EL1.BASE:Zeros(12); TRBSR_EL[target_el].WRAP = '1';
```

```
CTI_SignalEvent(CrossTriggerIn_TRBEWrap); if TRBLIMITR_EL1.FM == '00' then // Fill mode constant bits(6) bsc = '000001'; // Buffer full event OtherTRBEManagementEvent(bsc); elsif TRBLIMITR_EL1.FM != '11' then // Not Circular Buffer mode if TRBSR_EL[target_el].IRQ == '0' then TRBSR_EL[target_el].IRQ = '1'; // Assert interrupt or exception CTI_SignalEvent(CrossTriggerIn_TRBEMgmt); TRBPTR_EL1 = next_address<63:0>; TryAssertTRBIRQ(); TRUE;
```

## return J1.3.4.12 DefaultTRBEEvent // DefaultTRBEEvent() // ================== // Return the target ELx for an indirect write to TRBSR\_ELx for an Other buffer management // event or anything other than a buffer management event. bits(2) DefaultTRBEEvent() return ReportTRBEEvent(Zeros(6), bits(6) UNKNOWN); J1.3.4.13 DetectedTraceTrigger // DetectedTraceTrigger() // ====================== // Called when the trace unit detects a trace trigger DetectedTraceTrigger() if TraceBufferRunning() then constant bits(2) target\_el = DefaultTRBEEvent(); if TRBSR\_EL[target\_el].TRG == '0' then TRBSR\_EL[target\_el].TRG = '1'; if IsZero(TRBTRG\_EL1.TRG) &amp;&amp; TRBLIMITR\_EL1.TM != '11' then TraceUnitFlush(); TraceUnitFlushOnTriggerComplete(); J1.3.4.14 EffectiveMDCR\_EL3\_NSTB

```
// EffectiveMDCR_EL3_NSTB() // ======================== // Return the Effective value of MDCR_EL3.{NSTBE, NSTB} field and whether it is a reserved value. (bits(3), boolean) EffectiveMDCR_EL3_NSTB() bits(3) state_bits; boolean reserved = FALSE; if IsFeatureImplemented(FEAT_RME) then state_bits = MDCR_EL3.<NSTBE, NSTB>; if state_bits == '10x' || (!IsFeatureImplemented(FEAT_Secure) && state_bits == '00x') then // Reserved value reserved = TRUE; (-, state_bits) = ConstrainUnpredictableBits(Unpredictable_RESERVEDNSxB, 3); else state_bits = '0' : MDCR_EL3.NSTB; return (state_bits, reserved);
```

## J1.3.4.15 EffectiveTRBLIMITR\_EL1\_nVM

```
// EffectiveTRBLIMITR_EL1_nVM() // ============================ bit EffectiveTRBLIMITR_EL1_nVM() if !SelfHostedTraceEnabled() then // If SelfHostedTraceEnabled() is FALSE, then this function is only called when // FEAT_TRBE_EXT is implemented. assert IsFeatureImplemented(FEAT_TRBE_EXT); return '1'; if IsFeatureImplemented(FEAT_TRBEv1p1) && HaveEL(EL2) then (owning_ss, owning_el) = TraceBufferOwner(); if ((owning_ss != SS_Secure || IsSecureEL2Enabled()) && owning_el == EL1 && TRFCR_EL2.DnVM == '1') then return '0'; return TRBLIMITR_EL1.nVM;
```

## J1.3.4.16 EffectiveTRFCR\_EL1\_EE

```
// EffectiveTRFCR_EL1_EE() // ======================= // Return the Effective value of TRFCR_EL1.EE for the purpose of controlling the // TRBE Profiling exception. bits(2) EffectiveTRFCR_EL1_EE() if EffectiveTRFCR_EL2_EE() == '00' then return '00'; bits(2) ee = TRFCR_EL1.EE; if ee IN {'01', '10'} then // Reserved value if IsFeatureImplemented(FEAT_NV) then ee<0> = ee<1>; else Constraint c; (c, ee) = ConstrainUnpredictableBits(Unpredictable_RESTRFEE, 2); assert c IN {Constraint_DISABLED, Constraint_UNKNOWN}; if c == Constraint_DISABLED then ee = '00'; // Otherwise the value returned by ConstrainUnpredictableBits must // a non-reserved value return ee;
```

```
be J1.3.4.17 EffectiveTRFCR_EL2_EE // EffectiveTRFCR_EL2_EE() // ======================= // Return the Effective value of TRFCR_EL2.EE. bits(2) EffectiveTRFCR_EL2_EE() if !IsFeatureImplemented(FEAT_TRBE_EXC) || !SelfHostedTraceEnabled() then return '00'; if HaveEL(EL3) && MDCR_EL3.TRBEE == '00' then return '00'; constant boolean check_el2 = HaveEL(EL2) && (EffectiveSCR_EL3_NS() == '1' || IsSecureEL2Enabled()); return if check_el2 then TRFCR_EL2.EE else '01';
```

## J1.3.4.18 GetTRBSR\_EL1\_FSC

```
// GetTRBSR_EL1_FSC() // ================== // Query the TRBSR_EL1.FSC field. bits(6) GetTRBSR_EL1_FSC() bits(6) FSC; FSC = TRBSR_EL1<5:0>; return FSC;
```

## J1.3.4.19 GetTRBSR\_EL2\_FSC

```
// GetTRBSR_EL2_FSC() // ================== // Query the TRBSR_EL2.FSC field. bits(6) GetTRBSR_EL2_FSC() bits(6) FSC; FSC = TRBSR_EL2<5:0>; return FSC;
```

## J1.3.4.20 GetTRBSR\_EL3\_FSC

```
// GetTRBSR_EL3_FSC() // ================== // Query the TRBSR_EL3.FSC field. bits(6) GetTRBSR_EL3_FSC() bits(6) FSC; FSC = TRBSR_EL3<5:0>; return FSC;
```

## J1.3.4.21 HaveImpDefTraceOutput

```
// HaveImpDefTraceOutput() // ======================= boolean HaveImpDefTraceOutput() return boolean IMPLEMENTATION_DEFINED "Has Enabled External Trace Port";
```

## J1.3.4.22 ImpDefTraceOutput

```
// ImpDefTraceOutput() // =================== boolean ImpDefTraceOutput(bits(8) datum) // Send 'datum' to an IMPLEMENTATION DEFINED trace output port // return TRUE if the byte is sent return FALSE;
```

## J1.3.4.23 OtherTRBEManagementEvent

```
// OtherTRBEManagementEvent() // ========================== // Report an Other buffer management event, with the status code 'bsc' OtherTRBEManagementEvent(bits(6) bsc) ReportTRBEManagementEvent('000000', bsc);
```

## J1.3.4.24 ReportTRBEEvent

```
// ReportTRBEEvent() // ================= // Return the target ELx for an indirect write to TRBSR_ELx. // When the indirect write is due to a buffer management event: // 'ec_bits' is the Event Class for the management event. // 'fsc_bits' is the Fault Status Code when this is a fault, ignored otherwise. // Otherwise, 'ec_bits' should be Zeros(). bits(2) ReportTRBEEvent(bits(6) ec_bits, bits(6) fsc_bits) bits(2) target_el; boolean route_to_el3 = FALSE; boolean route_to_el2 = FALSE; if IsFeatureImplemented(FEAT_TRBE_EXC) && SelfHostedTraceEnabled() then constant boolean s1fault = (ec_bits == '100100'); // Stage 1 fault constant boolean s2fault = (ec_bits == '100101'); // Stage 2 fault boolean gpcfault, gpfault; if IsFeatureImplemented(FEAT_RME) then // Granule Protection Check fault, other than GPF. That is, a GPT address size fault, // GPT walk fault, or synchronous External abort on GPT fetch. gpcfault = (ec_bits == '011110'); // Other Granule Protection Fault, reported as Stage 1 or Stage 2 fault. gpfault = ((s1fault || s2fault) && fsc_bits IN {'10001x', '1001xx', '101000'}); else gpcfault = FALSE; gpfault = FALSE; constant boolean sync_ext_abort = ((s1fault || s2fault) && fsc_bits IN {'010000', '01001x', '0101xx', '011011'}); SecurityState owning_ss; bits(2) owning_el; (owning_ss, owning_el) = TraceBufferOwner(); if HaveEL(EL3) && MDCR_EL3.TRBEE == '1x' then route_to_el3 = (MDCR_EL3.TRBEE == '11' || gpcfault || (gpfault && SCR_EL3.GPF == '1') || (sync_ext_abort && EffectiveEA() == '1')); if EffectiveTRFCR_EL2_EE() == '1x' then route_to_el2 = (TRFCR_EL2.EE == '11' || (s1fault && owning_el == EL2) || s2fault || gpcfault || (gpfault && HCR_EL2.GPF == '1') || (sync_ext_abort && EffectiveHCR_TEA() == '1')); if route_to_el3 then target_el = EL3; elsif route_to_el2 then target_el = EL2; else target_el = EL1; return target_el;
```

## J1.3.4.25 ReportTRBEManagementEvent

## // ReportTRBEManagementEvent() // =========================== // Report a buffer management event with the event class 'ec' and status code 'bsc' ReportTRBEManagementEvent(bits(6) ec, bits(6) bsc) constant bits(2) target\_el = DefaultTRBEEvent(); if TRBSR\_EL[target\_el].S == '0' then TRBSR\_EL[target\_el].S = '1'; // Stop collection if TRBSR\_EL[target\_el].IRQ == '0' then TRBSR\_EL[target\_el].IRQ = '1'; // Assert interrupt or exception CTI\_SignalEvent(CrossTriggerIn\_TRBEMgmt); TRBSR\_EL[target\_el].EC = ec; TRBSR\_EL[target\_el].MSS = ZeroExtend(bsc, 16); TRBSR\_EL[target\_el].MSS2 = Zeros(24); CTI\_SignalEvent(CrossTriggerIn\_TRBEStop); J1.3.4.26 TRBEInternalBufferFull // TRBEInternalBufferFull() // ======================== boolean TRBEInternalBufferFull() // In the simple sequential model, the internal buffer never fills return FALSE; J1.3.4.27 TRBEInterruptEnabled // TRBEInterruptEnabled() // ====================== // Return TRUE if the TRBE interrupt request (TRBIRQ) is enabled, FALSE otherwise. boolean TRBEInterruptEnabled() return EffectiveTRFCR\_EL1\_EE() == '00'; J1.3.4.28 TRBE\_TRBIDR\_P\_Read

```
// TRBE_TRBIDR_P_Read() // ==================== // Called when TRBIDR_EL1 is read, returns the value of TRBIDR_EL1.P bit TRBE_TRBIDR_P_Read() SecurityState owning_ss; bits(2) owning_el; (owning_ss, owning_el) = TraceBufferOwner(); // Reads as one if the Trace Buffer is owned by a higher Exception // Level or another Security state. if (UInt(owning_el) > UInt(PSTATE.EL) || (PSTATE.EL != EL3 && owning_ss != CurrentSecurityState())) then return '1'; else return '0';
```

## J1.3.4.29 TRBSR\_EL

```
// TRBSR_EL - setter // ================= TRBSRType TRBSR_EL[bits(2) el] bits(64) r; case el of when EL1 r = TRBSR_EL1; when EL2 r = TRBSR_EL2; when EL3 r = TRBSR_EL3; otherwise Unreachable(); return r; // TRBSR_EL - getter // ================= TRBSR_EL[bits(2) el] = bits(64) value constant bits(64) r = value; case el of when EL1 TRBSR_EL1 = r; when EL2 TRBSR_EL2 = r; when EL3 TRBSR_EL3 = r; otherwise Unreachable(); return;
```

## J1.3.4.30 TraceBufferEnabled

```
// TraceBufferEnabled() // ==================== boolean TraceBufferEnabled() if !IsFeatureImplemented(FEAT_TRBE) then return FALSE; elsif SelfHostedTraceEnabled() then if TRBLIMITR_EL1.E == '0' then return FALSE; bits(2) el; (-, el) = TraceBufferOwner(); return !ELUsingAArch32(el); elsif IsFeatureImplemented(FEAT_TRBE) then return TRBLIMITR_EL1.XE == '1'; else return FALSE;
```

## J1.3.4.31 TraceBufferOwner

```
// TraceBufferOwner() // ================== // Return the owning Security state and Exception level. Must only be called // when SelfHostedTraceEnabled() is TRUE. (SecurityState, bits(2)) TraceBufferOwner() assert IsFeatureImplemented(FEAT_TRBE); SecurityState owning_ss; bits(3) state_bits; if HaveEL(EL3) then (state_bits, -) = EffectiveMDCR_EL3_NSTB(); else state_bits = if SecureOnlyImplementation() then '001' else '011'; case state_bits of
```

```
when '00x' owning_ss = SS_Secure; when '01x' owning_ss = SS_NonSecure; when '11x' owning_ss = SS_Realm; bits(2) owning_el; if HaveEL(EL2) && (owning_ss != SS_Secure || IsSecureEL2Enabled()) then owning_el = if MDCR_EL2.E2TB == '00' then EL2 else EL1; else owning_el = EL1; return (owning_ss, owning_el);
```

## J1.3.4.32 TraceBufferRunning

```
// TraceBufferRunning() // ==================== boolean TraceBufferRunning() if !TraceBufferEnabled() then return FALSE; boolean stopped = TRBSR_EL1.S == '1'; if IsFeatureImplemented(FEAT_TRBE_EXC) && SelfHostedTraceEnabled() then if HaveEL(EL3) && MDCR_EL3.TRBEE == '1x' then stopped = stopped || (TRBSR_EL3.S == '1'); if EffectiveTRFCR_EL2_EE() == '1x' then stopped = stopped || (TRBSR_EL2.S == '1'); return !stopped;
```

## J1.3.4.33 TraceUnitFlushOnTriggerComplete

```
// TraceUnitFlushOnTriggerComplete() // ================================= // Called when a trace unit flush completes following a call to // TraceUnitFlush() due to a trace trigger. TraceUnitFlushOnTriggerComplete() if TRBLIMITR_EL1.TM == '00' then // Stop on trigger constant bits(6) bsc = '000010'; // Trigger event OtherTRBEManagementEvent(bsc); elsif TRBLIMITR_EL1.TM != '11' then // Not Ignore trigger constant bits(2) target_el = DefaultTRBEEvent(); TRBSR_EL[target_el].IRQ = '1'; // Assert interrupt or exception
```

## J1.3.4.34 TryAssertTRBIRQ

```
// TryAssertTRBIRQ() // ================= // Assert TRBIRQ pin when appropriate. TryAssertTRBIRQ() if TRBEInterruptEnabled() && TRBSR_EL1.IRQ == '1' then SetInterruptRequestLevel(InterruptID_TRBIRQ, HIGH); else SetInterruptRequestLevel(InterruptID_TRBIRQ, LOW); return;
```

## J1.3.4.35 TraceInstrumentationAllowed

```
// TraceInstrumentationAllowed() // ============================= // Returns TRUE if Instrumentation Trace is allowed // in the given Exception level and Security state. boolean TraceInstrumentationAllowed(SecurityState ss, bits(2) el) if !IsFeatureImplemented(FEAT_ITE) then return FALSE; if ELUsingAArch32(el) then return FALSE; if TraceAllowed(el) then bit ite_bit; case el of when EL3 ite_bit = '0'; when EL2 ite_bit = TRCITECR_EL2.E2E; when EL1 ite_bit = TRCITECR_EL1.E1E; when EL0 if EffectiveTGE() == '1' then ite_bit = TRCITECR_EL2.E0HE; else ite_bit = TRCITECR_EL1.E0E; if SelfHostedTraceEnabled() then return ite_bit == '1'; else bit el_bit; bit ss_bit; case el of when EL0 el_bit = TRCITEEDCR.E0; when EL1 el_bit = TRCITEEDCR.E1; when EL2 el_bit = TRCITEEDCR.E2; when EL3 el_bit = TRCITEEDCR.E3; case ss of when SS_Realm ss_bit = TRCITEEDCR.RL; when SS_Secure ss_bit = TRCITEEDCR.S; when SS_NonSecure ss_bit = TRCITEEDCR.NS; otherwise ss_bit = '1'; constant boolean ed_allowed = ss_bit == '1' && el_bit == '1'; if TRCCONFIGR.ITO == '1' then return ed_allowed; else return ed_allowed && ite_bit == '1'; else return FALSE;
```

## J1.3.4.36 TraceUnitFlush

```
// TraceUnitFlush() // ================ // Called when a trace unit flush is requested, to output previous recorded trace. TraceUnitFlush();
```

## J1.3.4.37 EffectiveE0HTRE

```
// EffectiveE0HTRE() // ================= // Returns effective E0HTRE value bit EffectiveE0HTRE()
```

## J1.3.4.38 EffectiveE0TRE

```
// EffectiveE0TRE() // ================ // Returns effective E0TRE value bit EffectiveE0TRE() return if ELUsingAArch32(EL1) then TRFCR.E0TRE else
```

## J1.3.4.39 EffectiveE1TRE

```
// EffectiveE1TRE() // ================ // Returns effective E1TRE value bit EffectiveE1TRE() return if UsingAArch32() then TRFCR.E1TRE else
```

## J1.3.4.40 EffectiveE2TRE

```
// EffectiveE2TRE() // ================ // Returns effective E2TRE value bit EffectiveE2TRE() return if UsingAArch32() then HTRFCR.E2TRE else
```

## J1.3.4.41 SelfHostedTraceEnabled

```
// SelfHostedTraceEnabled() // ======================== // Returns TRUE if Self-hosted Trace is enabled. boolean SelfHostedTraceEnabled() bit secure_trace_enable = '0'; if !(HaveTraceExt() && IsFeatureImplemented(FEAT_TRF)) then return FALSE; if EDSCR.TFO == '0' then return TRUE; if IsFeatureImplemented(FEAT_RME) then secure_trace_enable = if IsFeatureImplemented(FEAT_SEL2) then MDCR_EL3.STE else '0'; return ((secure_trace_enable == '1' && !ExternalSecureNoninvasiveDebugEnabled()) || (MDCR_EL3.RLTE == '1' && !ExternalRealmNoninvasiveDebugEnabled())); if HaveEL(EL3) then secure_trace_enable = if ELUsingAArch32(EL3) then SDCR.STE else MDCR_EL3.STE; else secure_trace_enable = if SecureOnlyImplementation() then '1' else '0'; if secure_trace_enable == '1' && !ExternalSecureNoninvasiveDebugEnabled() then return TRUE; return FALSE;
```

```
TRFCR_EL1.E0TRE;
```

```
TRFCR_EL1.E1TRE;
```

```
TRFCR_EL2.E2TRE;
```

## J1.3.4.42 TraceAllowed

```
// TraceAllowed() // ============== // Returns TRUE if Self-hosted Trace is allowed in the given Exception level. boolean TraceAllowed(bits(2) el) if !HaveTraceExt() then return FALSE; // If in Debug state then tracing is not allowed if Halted() && !Restarting() then return FALSE; if SelfHostedTraceEnabled() then boolean trace_allowed; ss = SecurityStateAtEL(el); // Detect scenarios where tracing in this Security state is never allowed. case ss of when SS_NonSecure trace_allowed = TRUE; when SS_Secure bit trace_bit; if HaveEL(EL3) then trace_bit = if ELUsingAArch32(EL3) then SDCR.STE else MDCR_EL3.STE; else trace_bit = '1'; trace_allowed = trace_bit == '1'; when SS_Realm trace_allowed = MDCR_EL3.RLTE == '1'; when SS_Root trace_allowed = FALSE; // Tracing is prohibited if the trace buffer owning security state is not the // current Security state or the owning Exception level is a lower Exception level. if IsFeatureImplemented(FEAT_TRBE) && TraceBufferEnabled() then (owning_ss, owning_el) = TraceBufferOwner(); if (ss != owning_ss || UInt(owning_el) < UInt(el) || (EffectiveTGE() == '1' && owning_el == EL1)) then trace_allowed = FALSE; bit TRE_bit; case el of when EL3 TRE_bit = if !HaveAArch64() then TRFCR.E1TRE else '0'; when EL2 TRE_bit = EffectiveE2TRE(); when EL1 TRE_bit = EffectiveE1TRE(); when EL0 if EffectiveTGE() == '1' then TRE_bit = EffectiveE0HTRE(); else TRE_bit = EffectiveE0TRE(); return trace_allowed && TRE_bit == '1'; else return ExternalNoninvasiveDebugAllowed(el);
```

## J1.3.4.43 TraceContextIDR2

```
// TraceContextIDR2() // ================== boolean TraceContextIDR2() if !TraceAllowed(PSTATE.EL)|| !HaveEL(EL2) then return (!SelfHostedTraceEnabled() || TRFCR_EL2.CX == '1');
```

```
return FALSE;
```

## J1.3.4.44 TraceSynchronizationBarrier

```
// TraceSynchronizationBarrier() // ============================= // Barrier instruction that preserves the relative order of accesses to System // registers due to trace operations and other accesses to the same registers. // When FEAT_TRBE is implemented, a TraceSynchronizationBarrier also acts as a memory // barrier operation to flush any trace data generated by the trace unit, such that // a subsequent Data Synchronization Barrier does not complete until the trace data // has been written to memory. TraceSynchronizationBarrier() if IsFeatureImplemented(FEAT_TRBE) && !TraceAllowed(PSTATE.EL) then TraceUnitFlush(); return;
```

## J1.3.4.45 TraceTimeStamp

```
// TraceTimeStamp() // ================ TimeStamp TraceTimeStamp() if SelfHostedTraceEnabled() then if HaveEL(EL2) then TS_el2 = TRFCR_EL2.TS; if !IsFeatureImplemented(FEAT_ECV) && TS_el2 == '10' then // Reserved value (-, TS_el2) = ConstrainUnpredictableBits(Unpredictable_EL2TIMESTAMP, 2); case TS_el2 of when '00' // Falls out to check TRFCR_EL1.TS when '01' return TimeStamp_Virtual; when '10' // Otherwise ConstrainUnpredictableBits removes this case assert IsFeatureImplemented(FEAT_ECV); return TimeStamp_OffsetPhysical; when '11' return TimeStamp_Physical; TS_el1 = TRFCR_EL1.TS; if TS_el1 == '00' || (!IsFeatureImplemented(FEAT_ECV) && TS_el1 == '10') then // Reserved value (-, TS_el1) = ConstrainUnpredictableBits(Unpredictable_EL1TIMESTAMP, 2); case TS_el1 of when '01' return TimeStamp_Virtual; when '10' assert IsFeatureImplemented(FEAT_ECV); return TimeStamp_OffsetPhysical; when '11' return TimeStamp_Physical; otherwise Unreachable(); // ConstrainUnpredictableBits removes this case else return TimeStamp_CoreSight;
```

## J1.3.4.46 IsTraceCorePowered

```
// IsTraceCorePowered() // ==================== // Returns TRUE if the trace unit Core power domain is powered up boolean IsTraceCorePowered();
```

## J1.3.5 shared/translation

This section includes the following pseudocode functions:

- at
- EncodePARAttrs
- PAREncodeShareability
- ReportedPARAttrs
- ReportedPARShareability
- DecodeDevice
- DecodeLDFAttr
- DecodeSDFAttr
- DecodeShareability
- EffectiveShareability
- IsTaggableMemAttr
- IsWBShareable
- NormalNCMemAttr
- S1ConstrainUnpredictableRESMAIR
- S1DecodeMemAttrs
- S2CombineS1AttrHints
- S2CombineS1Device
- S2CombineS1MemAttrs
- S2CombineS1Shareability
- S2DecodeCacheability
- S2DecodeMemAttrs
- S2MemTagType
- S2ResMemAttr
- WalkMemAttrs
- AlignmentFault
- ExclusiveFault
- NoFault
- AbovePPS
- DecodeGPTBlock
- DecodeGPTContiguous
- DecodeGPTGranules
- DecodeGPTTable
- DecodePGS
- DecodePGSRange
- DecodePPS
- GPCBW\_EL3BWSTRIDEValid
- GPCFault

- GPCNoFault
- GPCRegistersConsistent
- GPICheck
- GPIIndex
- GPIValid
- GPT
- GPTBlockDescriptorValid
- GPTContigDescriptorValid
- GPTEntry
- GPTGranulesDescriptorValid
- GPTL0Size
- GPTLevel0EntryValid
- GPTLevel0Index
- GPTLevel1EntryValid
- GPTLevel1Index
- GPTTable
- GPTTableDescriptorValid
- GPTWalk
- GranuleProtectionCheck
- IsGranuleProtectionCheckedAccess
- PAWithinGPCBypassWindow
- PGS
- Table
- S1TranslationRegime
- AddressDescriptor
- ContiguousSize
- CreateAddressDescriptor
- CreateFaultyAddressDescriptor
- DecodePASpace
- DescriptorType
- Domains
- FetchDescriptor
- HasUnprivileged
- Regime
- RegimeUsingAArch32
- S1TTWParams
- S2TTWParams
- SDFType
- SecurityStateForRegime
- StageOA
- TGx
- TGxGranuleBits
- TLBContext
- TLBRecord
- TTWState
- TranslationRegime
- TranslationSize
- UseASID
- UseVMID

## J1.3.5.1 at

```
enumeration TranslationStage TranslationStage_1, TranslationStage_12 }; enumeration ATAccess { ATAccess_Read, ATAccess_Write, ATAccess_Any, ATAccess_ReadPAN, ATAccess_WritePAN };
```

## J1.3.5.2 EncodePARAttrs

```
// EncodePARAttrs() // ================ // Convert orthogonal attributes and hints to 64-bit PAR ATTR field. bits(8) EncodePARAttrs(MemoryAttributes memattrs) bits(8) result; if IsFeatureImplemented(FEAT_MTE) && memattrs.tags == MemTag_AllocationTagged then if IsFeatureImplemented(FEAT_MTE_PERM) && memattrs.notagaccess then result<7:0> = '11100000'; else result<7:0> = '11110000'; return result; if memattrs.memtype == MemType_Device then result<7:4> = '0000'; case memattrs.device of when DeviceType_nGnRnE result<3:0> = '0000'; when DeviceType_nGnRE result<3:0> = '0100'; when DeviceType_nGRE result<3:0> = '1000'; when DeviceType_GRE result<3:0> = '1100'; otherwise Unreachable(); result<0> = NOT memattrs.xs; else if memattrs.xs == '0' then if (memattrs.outer.attrs == MemAttr_WT && memattrs.inner.attrs == MemAttr_WT && !memattrs.outer.transient && memattrs.outer.hints == MemHint_RA) then return '10100000'; elsif memattrs.outer.attrs == MemAttr_NC && memattrs.inner.attrs == MemAttr_NC then return '01000000'; if memattrs.outer.attrs == MemAttr_WT then result<7:6> = if memattrs.outer.transient then '00' else '10'; result<5:4> = memattrs.outer.hints; elsif memattrs.outer.attrs == MemAttr_WB then result<7:6> = if memattrs.outer.transient then '01' else '11'; result<5:4> = memattrs.outer.hints; else // MemAttr_NC result<7:4> = '0100'; if memattrs.inner.attrs == MemAttr_WT then result<3:2> = if memattrs.inner.transient then '00' else '10'; result<1:0> = memattrs.inner.hints; elsif memattrs.inner.attrs == MemAttr_WB then result<3:2> = if memattrs.inner.transient then '01' else '11'; result<1:0> = memattrs.inner.hints; else // MemAttr_NC
```

```
{
```

```
result<3:0> = '0100'; return result;
```

## J1.3.5.3 PAREncodeShareability

```
// PAREncodeShareability() // ======================= // Derive 64-bit PAR SH field. bits(2) PAREncodeShareability(MemoryAttributes memattrs) if (memattrs.memtype == MemType_Device || (memattrs.inner.attrs == MemAttr_NC && memattrs.outer.attrs == MemAttr_NC)) then // Force Outer-Shareable on Device and Normal Non-Cacheable memory return '10'; case memattrs.shareability of when Shareability_NSH return '00'; when Shareability_ISH return '11'; when Shareability_OSH return '10';
```

## J1.3.5.4 ReportedPARAttrs

```
// ReportedPARAttrs() // ================== // The value returned in this field can be the resulting attribute, as determined by any permitted // implementation choices and any applicable configuration bits, instead of the value that appears // in the translation table descriptor.
```

bits(8) ReportedPARAttrs(bits(8) parattrs);

## J1.3.5.5 ReportedPARShareability

```
// ReportedPARShareability() // ========================= // The value returned in SH field can be the resulting attribute, as determined by any // permitted implementation choices and any applicable configuration bits, instead of // the value that appears in the translation table descriptor. bits(2) ReportedPARShareability(bits(2) sh);
```

## J1.3.5.6 DecodeDevice

```
// DecodeDevice() // ============== // Decode output Device type DeviceType DecodeDevice(bits(2) device) case device of when '00' return DeviceType_nGnRnE; when '01' return DeviceType_nGnRE; when '10' return DeviceType_nGRE; when '11' return DeviceType_GRE;
```

## J1.3.5.7 DecodeLDFAttr

```
// DecodeLDFAttr() // =============== // Decode memory attributes using LDF (Long Descriptor Format) mapping MemAttrHints DecodeLDFAttr(bits(4) attr) MemAttrHints ldfattr; if attr == 'x0xx' then ldfattr.attrs = MemAttr_WT; // Write-through elsif attr == '0100' then ldfattr.attrs = MemAttr_NC; // Non-cacheable elsif attr == 'x1xx' then ldfattr.attrs = MemAttr_WB; // Write-back else Unreachable(); // Allocation hints are applicable only to cacheable memory. if ldfattr.attrs != MemAttr_NC then case attr<1:0> of when '00' ldfattr.hints = MemHint_No; // No allocation hints when '01' ldfattr.hints = MemHint_WA; // Write-allocate when '10' ldfattr.hints = MemHint_RA; // Read-allocate when '11' ldfattr.hints = MemHint_RWA; // Read/Write allocate // The Transient hint applies only to cacheable memory with some allocation if ldfattr.attrs != MemAttr_NC && ldfattr.hints != MemHint_No then ldfattr.transient = attr<3> == '0'; return ldfattr;
```

```
hints. J1.3.5.8 DecodeSDFAttr // DecodeSDFAttr() // =============== // Decode memory attributes using SDF (Short Descriptor Format) mapping MemAttrHints DecodeSDFAttr(bits(2) rgn) MemAttrHints sdfattr; case rgn of when '00' // Non-cacheable (no allocate) sdfattr.attrs = MemAttr_NC; when '01' // Write-back, Read and Write allocate sdfattr.attrs = MemAttr_WB; sdfattr.hints = MemHint_RWA; when '10' // Write-through, Read allocate sdfattr.attrs = MemAttr_WT; sdfattr.hints = MemHint_RA; when '11' // Write-back, Read allocate sdfattr.attrs = MemAttr_WB; sdfattr.hints = MemHint_RA; sdfattr.transient = FALSE; return sdfattr; J1.3.5.9 DecodeShareability
```

```
// DecodeShareability() // ==================== // Decode shareability of target memory region Shareability DecodeShareability(bits(2) sh) case sh of when '10' return Shareability_OSH;
```

```
when '11' return Shareability_ISH; when '00' return Shareability_NSH; otherwise case ConstrainUnpredictable(Unpredictable_Shareability) of when Constraint_OSH return Shareability_OSH; when Constraint_ISH return Shareability_ISH; when Constraint_NSH return Shareability_NSH;
```

## J1.3.5.10 EffectiveShareability

```
// EffectiveShareability() // ======================= // Force Outer Shareability on Device and Normal iNCoNC memory Shareability EffectiveShareability(MemoryAttributes memattrs) if (memattrs.memtype == MemType_Device || (memattrs.inner.attrs == MemAttr_NC && memattrs.outer.attrs == MemAttr_NC)) then return Shareability_OSH; else return memattrs.shareability;
```

## J1.3.5.11 IsTaggableMemAttr

```
// IsTaggableMemAttr() // =================== // Determine whether the current memory attributes support MTE boolean IsTaggableMemAttr(MemoryAttributes attrs) return ((attrs.memtype == MemType_Normal) && (attrs.inner.attrs == MemAttr_WB) && (attrs.inner.hints == MemHint_RWA) && (!attrs.inner.transient) && (attrs.outer.attrs == MemAttr_WB) && (attrs.outer.hints == MemHint_RWA) && (!attrs.outer.transient));
```

## J1.3.5.12 IsWBShareable

```
// IsWBShareable() // =============== // Determines whether the given memory attributes are iWBoWB Shareable boolean IsWBShareable(MemoryAttributes memattrs) return (memattrs.memtype == MemType_Normal && memattrs.inner.attrs == MemAttr_WB && memattrs.outer.attrs == MemAttr_WB && memattrs.shareability IN {Shareability_ISH, Shareability_OSH});
```

## J1.3.5.13 NormalNCMemAttr

```
// NormalNCMemAttr() // ================= // Normal Non-cacheable memory attributes MemoryAttributes NormalNCMemAttr() MemAttrHints non_cacheable; non_cacheable.attrs = MemAttr_NC;
```

```
MemoryAttributes nc_memattrs; nc_memattrs.memtype = MemType_Normal; nc_memattrs.outer = non_cacheable; nc_memattrs.inner = non_cacheable; nc_memattrs.shareability = Shareability_OSH; nc_memattrs.tags = MemTag_Untagged; nc_memattrs.notagaccess = FALSE; return nc_memattrs;
```

## J1.3.5.14 S1ConstrainUnpredictableRESMAIR

```
// S1ConstrainUnpredictableRESMAIR() // ================================= // Determine whether a reserved value occupies MAIR_ELx.AttrN boolean S1ConstrainUnpredictableRESMAIR(bits(8) attr, boolean s1aarch64) case attr of when '0000xx01' return !(s1aarch64 && IsFeatureImplemented(FEAT_XS)); when '0000xxxx' return attr<1:0> != '00'; when '01000000' return !(s1aarch64 && IsFeatureImplemented(FEAT_XS)); when '10100000' return !(s1aarch64 && IsFeatureImplemented(FEAT_XS)); when '11110000' return !(s1aarch64 && IsFeatureImplemented(FEAT_MTE2)); when 'xxxx0000' return TRUE; otherwise return FALSE;
```

## J1.3.5.15 S1DecodeMemAttrs

```
// S1DecodeMemAttrs() // ================== // Decode MAIR-format memory attributes assigned in stage 1 MemoryAttributes S1DecodeMemAttrs(bits(8) attr_in, bits(2) sh, boolean s1aarch64) bits(8) attr = attr_in; if S1ConstrainUnpredictableRESMAIR(attr, s1aarch64) then // Map reserved encodings to an allocated encoding (-, attr) = ConstrainUnpredictableBits(Unpredictable_RESMAIR, 8); MemoryAttributes memattrs; case attr of when '0000xxxx' // Device memory memattrs.memtype = MemType_Device; memattrs.device = DecodeDevice(attr<3:2>); memattrs.xs = if s1aarch64 then NOT attr<0> else '1'; when '01000000' assert s1aarch64 && IsFeatureImplemented(FEAT_XS); memattrs.memtype = MemType_Normal; memattrs.outer.attrs = MemAttr_NC; memattrs.inner.attrs = MemAttr_NC; memattrs.xs = '0'; when '10100000' assert s1aarch64 && IsFeatureImplemented(FEAT_XS); memattrs.memtype = MemType_Normal; memattrs.outer.attrs = MemAttr_WT; memattrs.outer.hints = MemHint_RA; memattrs.outer.transient = FALSE; memattrs.inner.attrs = MemAttr_WT; memattrs.inner.hints = MemHint_RA; memattrs.inner.transient = FALSE; memattrs.xs = '0'; when '11110000' // Tagged memory assert s1aarch64 && IsFeatureImplemented(FEAT_MTE2); memattrs.memtype = MemType_Normal;
```

```
memattrs.outer.attrs = MemAttr_WB; memattrs.outer.hints = MemHint_RWA; memattrs.outer.transient = FALSE; memattrs.inner.attrs = MemAttr_WB; memattrs.inner.hints = MemHint_RWA; memattrs.inner.transient = FALSE; memattrs.xs = '0'; otherwise memattrs.memtype = MemType_Normal; memattrs.outer = DecodeLDFAttr(attr<7:4>); memattrs.inner = DecodeLDFAttr(attr<3:0>); if (memattrs.inner.attrs == MemAttr_WB && memattrs.outer.attrs == MemAttr_WB) then memattrs.xs = '0'; else memattrs.xs = '1'; memattrs.shareability = DecodeShareability(sh); memattrs.tags = MemTag_Untagged; memattrs.notagaccess = FALSE; return memattrs; // S1DecodeMemAttrs() // ================== // Decode MAIR-format memory attributes assigned in stage 1 MemoryAttributes S1DecodeMemAttrs(bits(8) attr_in, bits(2) sh, boolean s1aarch64, S1TTWParams walkparams, AccessType acctype) MemoryAttributes memattrs = S1DecodeMemAttrs(attr_in, sh, s1aarch64); if s1aarch64 && attr_in == '11110000' then memattrs.tags = MemTag_AllocationTagged; elsif IsFeatureImplemented(FEAT_MTE_CANONICAL_TAGS) && s1aarch64 && walkparams.mtx == '1' then memattrs.tags = MemTag_CanonicallyTagged; return memattrs;
```

```
J1.3.5.16 S2CombineS1AttrHints s2_attrhints)
```

```
// S2CombineS1AttrHints() // ====================== // Determine resultant Normal memory cacheability and allocation hints from // combining stage 1 Normal memory attributes and stage 2 cacheability attributes. MemAttrHints S2CombineS1AttrHints(MemAttrHints s1_attrhints, MemAttrHints MemAttrHints attrhints; if s1_attrhints.attrs == MemAttr_NC || s2_attrhints.attrs == MemAttr_NC then attrhints.attrs = MemAttr_NC; elsif s1_attrhints.attrs == MemAttr_WT || s2_attrhints.attrs == MemAttr_WT then attrhints.attrs = MemAttr_WT; else attrhints.attrs = MemAttr_WB; // Stage 2 does not assign any allocation hints // Instead, they are inherited from stage 1 if attrhints.attrs != MemAttr_NC then attrhints.hints = s1_attrhints.hints; attrhints.transient = s1_attrhints.transient; return attrhints;
```

## J1.3.5.17 S2CombineS1Device

```
// S2CombineS1Device() // =================== // Determine resultant Device type from combining output memory attributes // in stage 1 and Device attributes in stage 2 DeviceType S2CombineS1Device(DeviceType s1_device, DeviceType s2_device) if s1_device == DeviceType_nGnRnE || s2_device == DeviceType_nGnRnE then return DeviceType_nGnRnE; elsif s1_device == DeviceType_nGnRE || s2_device == DeviceType_nGnRE return DeviceType_nGnRE; elsif s1_device == DeviceType_nGRE || s2_device == DeviceType_nGRE then return DeviceType_nGRE; else return DeviceType_GRE;
```

```
stage 2 with stage 1 memory attributes S2CombineS1MemAttrs(MemoryAttributes s1_memattrs, MemoryAttributes boolean s2aarch64) MemoryAttributes memattrs; if s1_memattrs.memtype == MemType_Device && s2_memattrs.memtype == MemType_Device then memattrs.memtype = MemType_Device; memattrs.device = S2CombineS1Device(s1_memattrs.device, s2_memattrs.device); elsif s1_memattrs.memtype == MemType_Device then // S2 Normal, S1 Device memattrs = s1_memattrs; elsif s2_memattrs.memtype == MemType_Device then // S2 Device, S1 Normal memattrs = s2_memattrs; else // S2 Normal, S1 Normal memattrs.memtype = MemType_Normal; memattrs.inner = S2CombineS1AttrHints(s1_memattrs.inner, s2_memattrs.inner); memattrs.outer = S2CombineS1AttrHints(s1_memattrs.outer, s2_memattrs.outer); memattrs.tags = S2MemTagType(memattrs, s1_memattrs.tags); if !IsFeatureImplemented(FEAT_MTE_PERM) then memattrs.notagaccess = FALSE; else memattrs.notagaccess = (s2_memattrs.notagaccess && s1_memattrs.tags == MemTag_AllocationTagged); memattrs.shareability = S2CombineS1Shareability(s1_memattrs.shareability, s2_memattrs.shareability); if (memattrs.memtype == MemType_Normal && memattrs.inner.attrs == MemAttr_WB && memattrs.outer.attrs == MemAttr_WB) then memattrs.xs = '0'; elsif s2aarch64 then memattrs.xs = s2_memattrs.xs AND s1_memattrs.xs; else memattrs.xs = s1_memattrs.xs; memattrs.shareability = EffectiveShareability(memattrs); return memattrs;
```

```
then J1.3.5.18 S2CombineS1MemAttrs // S2CombineS1MemAttrs() // ===================== // Combine MemoryAttributes s2_memattrs,
```

## J1.3.5.19 S2CombineS1Shareability

```
// S2CombineS1Shareability() // ========================= // Combine stage 2 shareability with stage 1 Shareability S2CombineS1Shareability(Shareability Shareability if (s1_shareability == Shareability_OSH || s2_shareability == Shareability_OSH) then return Shareability_OSH; elsif (s1_shareability == Shareability_ISH || s2_shareability == Shareability_ISH) then return Shareability_ISH; else return Shareability_NSH;
```

```
// S2DecodeMemAttrs() // ================== // Decode stage 2 memory attributes when FWB is 0 MemoryAttributes S2DecodeMemAttrs(bits(4) attr_in, bits(2) sh, boolean MemoryAttributes memattrs; bits(4) attr; if S2ResMemAttr(s2aarch64, attr_in) then // Map reserved encodings to an allocated encoding (-, attr) = ConstrainUnpredictableBits(Unpredictable_S2RESMEMATTR, 4); else attr = attr_in; case attr of when '00xx' // Device memory memattrs.memtype = MemType_Device; memattrs.device = DecodeDevice(attr<1:0>); when '0100' // Normal, Inner+Outer WB cacheable NoTagAccess memory assert s2aarch64 && IsFeatureImplemented(FEAT_MTE_PERM); memattrs.memtype = MemType_Normal;
```

```
s1_shareability, s2_shareability) J1.3.5.20 S2DecodeCacheability // S2DecodeCacheability() // ====================== // Determine the stage 2 cacheability for Normal memory MemAttrHints S2DecodeCacheability(bits(2) attr) MemAttrHints s2attr; case attr of when '01' s2attr.attrs = MemAttr_NC; // Non-cacheable when '10' s2attr.attrs = MemAttr_WT; // Write-through when '11' s2attr.attrs = MemAttr_WB; // Write-back otherwise Unreachable(); // Stage 2 does not assign hints or the transient property // They are inherited from stage 1 if the result of the combination allows it s2attr.hints = bits(2) UNKNOWN; s2attr.transient = boolean UNKNOWN; return s2attr; J1.3.5.21 S2DecodeMemAttrs s2aarch64)
```

## memattrs.outer = S2DecodeCacheability('11'); // Write-back memattrs.inner = S2DecodeCacheability('11'); // Write-back otherwise // Normal memory memattrs.memtype = MemType\_Normal; memattrs.outer = S2DecodeCacheability(attr&lt;3:2&gt;); memattrs.inner = S2DecodeCacheability(attr&lt;1:0&gt;); memattrs.shareability = DecodeShareability(sh); if s2aarch64 &amp;&amp; IsFeatureImplemented(FEAT\_MTE\_PERM) then memattrs.notagaccess = attr == '0100'; else memattrs.notagaccess = FALSE; return memattrs; J1.3.5.22 S2MemTagType // S2MemTagType() // ============== // Determine whether the combined output memory attributes of stage 1 and // stage 2 indicate tagged memory MemTagType S2MemTagType(MemoryAttributes s2\_memattrs, MemTagType s1\_tagtype) if !IsFeatureImplemented(FEAT\_MTE2) then return MemTag\_Untagged; if s1\_tagtype == MemTag\_AllocationTagged &amp;&amp; IsTaggableMemAttr(s2\_memattrs) then return MemTag\_AllocationTagged; // Return what stage 1 asked for if we can, otherwise Untagged. if s1\_tagtype != MemTag\_AllocationTagged then return s1\_tagtype; return MemTag\_Untagged; J1.3.5.23 S2ResMemAttr // S2ResMemAttr() // ============== // Determine whether a reserved value occupies stage 2 MemAttr field when FWB is 0 boolean S2ResMemAttr(boolean s2aarch64, bits(4) attr) case attr of when '0100' return !(s2aarch64 &amp;&amp; IsFeatureImplemented(FEAT\_MTE\_PERM)); when '1x00' return TRUE; otherwise return FALSE; J1.3.5.24 WalkMemAttrs // WalkMemAttrs() // ============== // Retrieve memory attributes of translation table walk MemoryAttributes WalkMemAttrs(bits(2) sh, bits(2) irgn, bits(2) orgn) MemoryAttributes walkmemattrs; walkmemattrs.memtype = MemType\_Normal; walkmemattrs.shareability = DecodeShareability(sh); walkmemattrs.inner = DecodeSDFAttr(irgn);

```
walkmemattrs.outer = DecodeSDFAttr(orgn); walkmemattrs.tags = MemTag_Untagged; if (walkmemattrs.inner.attrs == MemAttr_WB && walkmemattrs.outer.attrs == walkmemattrs.xs = '0'; else walkmemattrs.xs = '1'; walkmemattrs.notagaccess = FALSE; return walkmemattrs;
```

```
// NoFault() // ========= // Return a clear fault record indicating no faults have FaultRecord NoFault() FaultRecord fault; fault.vaddress = bits(64) UNKNOWN; fault.statuscode = Fault_None; fault.accessdesc = AccessDescriptor UNKNOWN; fault.secondstage = FALSE; fault.s2fs1walk = FALSE; fault.dirtybit = FALSE; fault.overlay = FALSE; fault.toplevel = FALSE; fault.assuredonly = FALSE; fault.s1tagnotdata = FALSE; fault.tagaccess = FALSE; fault.gpcfs2walk = FALSE; fault.gpcf = GPCNoFault(); fault.hdbssf = FALSE; return fault;
```

## MemAttr\_WB) then J1.3.5.25 AlignmentFault // AlignmentFault() // ================ // Return a fault record indicating an Alignment fault not due to memory type has occured // for a specific access FaultRecord AlignmentFault(AccessDescriptor accdesc, bits(64) vaddress) FaultRecord fault = NoFault(accdesc, vaddress); fault.statuscode = Fault\_Alignment; return fault; J1.3.5.26 ExclusiveFault // ExclusiveFault() // ================ // Return a fault record indicating a fault for an unsupported Exclusive access FaultRecord ExclusiveFault(AccessDescriptor accdesc, bits(64) vaddress) FaultRecord fault = NoFault(accdesc, vaddress); fault.statuscode = Fault\_Exclusive; return fault; J1.3.5.27 NoFault occured

```
// NoFault() // ========= // Return a clear fault record indicating no faults have occured for a specific access FaultRecord NoFault(AccessDescriptor accdesc) FaultRecord fault; fault.statuscode = Fault_None; fault.accessdesc = accdesc; fault.secondstage = FALSE; fault.s2fs1walk = FALSE; fault.dirtybit = FALSE; fault.overlay = FALSE; fault.toplevel = FALSE; fault.assuredonly = FALSE; fault.s1tagnotdata = FALSE; fault.tagaccess = FALSE; fault.write = !accdesc.read && accdesc.write; fault.gpcfs2walk = FALSE; fault.gpcf = GPCNoFault(); fault.hdbssf = FALSE; return fault; // NoFault() // ========= FaultRecord NoFault(AccessDescriptor accdesc, bits(64) vaddress) FaultRecord fault = NoFault(); fault.accessdesc = accdesc; fault.write = !accdesc.read && accdesc.write; fault.vaddress = vaddress; return fault; J1.3.5.28 AbovePPS // AbovePPS() // ========== // Returns TRUE if an address exceeds the range configured in GPCCR_EL3.PPS. boolean AbovePPS(bits(56) address) constant integer pps = DecodePPS(); if pps >= 56 then return FALSE; return !IsZero(address<55:pps>); J1.3.5.29 DecodeGPTBlock // DecodeGPTBlock() // ================ // Decode a GPT Block descriptor. GPTEntry DecodeGPTBlock(PGSe pgs, bits(64) gpt_entry) assert gpt_entry<3:0> == GPT_Block; GPTEntry result; result.gpi = gpt_entry<7:4>; result.level = 0; // GPT information from a level 0 GPT Block descriptor is permitted // to be cached in a TLB as though the Block is a contiguous region
```

```
// of granules each of the size configured in GPCCR_EL3.PGS. case pgs of when PGS_4KB result.size = GPTRange_4KB; when PGS_16KB result.size = GPTRange_16KB; when PGS_64KB result.size = GPTRange_64KB; otherwise Unreachable(); result.contig_size = GPTL0Size(); return result;
```

## J1.3.5.30 DecodeGPTContiguous

```
// DecodeGPTContiguous() // ===================== // Decode a GPT Contiguous descriptor. GPTEntry DecodeGPTContiguous(PGSe pgs, bits(64) gpt_entry) assert gpt_entry<3:0> == GPT_Contig; GPTEntry result; result.gpi = gpt_entry<7:4>; case pgs of when PGS_4KB result.size = GPTRange_4KB; when PGS_16KB result.size = GPTRange_16KB; when PGS_64KB result.size = GPTRange_64KB; otherwise Unreachable(); case gpt_entry<9:8> of when '01' result.contig_size = GPTRange_2MB; when '10' result.contig_size = GPTRange_32MB; when '11' result.contig_size = GPTRange_512MB; otherwise Unreachable(); result.level = 1; return result;
```

## J1.3.5.31 DecodeGPTGranules

```
// DecodeGPTGranules() // =================== // Decode a GPT Granules descriptor. GPTEntry DecodeGPTGranules(PGSe pgs, integer index, bits(64) gpt_entry) GPTEntry result; result.gpi = gpt_entry<index*4 +:4>; case pgs of when PGS_4KB result.size = GPTRange_4KB; when PGS_16KB result.size = GPTRange_16KB; when PGS_64KB result.size = GPTRange_64KB; otherwise Unreachable(); result.contig_size = result.size; // No contiguity result.level = 1; return result;
```

## J1.3.5.32 DecodeGPTTable

```
// DecodeGPTTable() // ================ // Decode a GPT Table descriptor. GPTTable DecodeGPTTable(PGSe pgs, bits(64) gpt_entry) assert gpt_entry<3:0> == GPT_Table; GPTTable result; case pgs of when PGS_4KB result.address when PGS_16KB result.address = when PGS_64KB result.address = otherwise Unreachable(); return result;
```

## = gpt\_entry&lt;55:17&gt;:Zeros(17); gpt\_entry&lt;55:15&gt;:Zeros(15); gpt\_entry&lt;55:13&gt;:Zeros(13); J1.3.5.33 DecodePGS // DecodePGS() // =========== PGSe DecodePGS(bits(2) pgs) case pgs of when '00' return PGS\_4KB; when '10' return PGS\_16KB; when '01' return PGS\_64KB; otherwise Unreachable(); J1.3.5.34 DecodePGSRange // DecodePGSRange() // ================ AddressSize DecodePGSRange(PGSe pgs) case pgs of when PGS\_4KB return GPTRange\_4KB; when PGS\_16KB return GPTRange\_16KB; when PGS\_64KB return GPTRange\_64KB; otherwise Unreachable(); J1.3.5.35 DecodePPS // DecodePPS() // =========== // Size of region protected by the GPT, in bits. AddressSize DecodePPS() case GPCCR\_EL3.&lt;PPS3, PPS&gt; of when '0000' return 32; when '0001' return 36; when '0010' return 40; when '0011' return 42; when '0100' return 44; when '0101' return 48; when '0110' return 52; when '0111' assert IsFeatureImplemented(FEAT\_RME\_GPC3); return 56; when '1000' assert IsFeatureImplemented(FEAT\_RME\_GPC3); return 46; when '1001' assert IsFeatureImplemented(FEAT\_RME\_GPC3); return 47; otherwise Unreachable();

## J1.3.5.36 GPCBW\_EL3BWSTRIDEValid

```
// GPCBW_EL3BWSTRIDEValid() // ======================== // Returns whether the current GPCBW_EL3.BWSTRIDE value is valid boolean GPCBW_EL3BWSTRIDEValid() assert IsFeatureImplemented(FEAT_RME_GPC3); return GPCBW_EL3.BWSTRIDE IN { '00000', '00010', '00100', '00110', '00111', '01000', '01001', '01010', '10000' };
```

## J1.3.5.37 GPCFault

```
// GPCFault() // ========== // Constructs and returns a GPCF GPCFRecord GPCFault(GPCF gpf, integer level) GPCFRecord fault; fault.gpf = gpf; fault.level = level; return fault;
```

## J1.3.5.38 GPCNoFault

```
// GPCNoFault() // ============ // Returns the default properties of a GPCF that does not represent a fault GPCFRecord GPCNoFault() GPCFRecord result; result.gpf = GPCF_None; return result;
```

## J1.3.5.39 GPCRegistersConsistent

```
// GPCRegistersConsistent() // ======================== // Returns whether the GPT registers are configured correctly. // This returns false if any fields select a Reserved value. boolean GPCRegistersConsistent() // Check for Reserved register values if IsFeatureImplemented(FEAT_RME_GPC3) then if ! GPCCR_EL3.<PPS3, PPS> IN {'0xxx', '100x'} then return FALSE; if GPCCR_EL3.GPCBW == '1' then if ! GPCBW_EL3.BWSIZE IN {'00x', '1x0', '010'} then return FALSE; if !GPCBW_EL3BWSTRIDEValid() then
```

```
return FALSE; constant integer bwstride = 1 << (40 + UInt(GPCBW_EL3.BWSTRIDE)); constant integer bwaddr = UInt(GPCBW_EL3.BWADDR) << 30; if bwstride <= bwaddr then return FALSE; if !IsAligned(GPCBW_EL3.BWADDR, 1 << UInt(GPCBW_EL3.BWSIZE)) then return FALSE; else if GPCCR_EL3.PPS == '111' then return FALSE; if DecodePPS() > AArch64.PAMax() then return FALSE; if GPCCR_EL3.PGS == '11' then return FALSE; if GPCCR_EL3.SH == '01' then return FALSE; // Inner and Outer Non-cacheable requires Outer Shareable if GPCCR_EL3.<ORGN, IRGN> == '0000' && GPCCR_EL3.SH != '10' then return FALSE; return TRUE;
```

```
J1.3.5.40 GPICheck // GPICheck() // ========== // Returns whether an access to a given physical address space is permitted // given the configured GPI value. // paspace: Physical address space of the access // gpi: Value read from GPT for the access // ss: Security state of the access boolean GPICheck(PASpace paspace, bits(4) gpi, SecurityState ss) case gpi of when GPT_NoAccess return FALSE; when GPT_Secure assert IsFeatureImplemented(FEAT_SEL2); return paspace == PAS_Secure; when GPT_NonSecure return paspace == PAS_NonSecure; when GPT_Root return paspace == PAS_Root; when GPT_Realm return paspace == PAS_Realm; when GPT_NonSecureOnly assert IsFeatureImplemented(FEAT_RME_GPC2); return paspace == PAS_NonSecure && (ss IN {SS_Root, SS_NonSecure}); when GPT_SystemAgent assert IsFeatureImplemented(FEAT_RME_GDI); return paspace == PAS_SystemAgent; when GPT_NonSecureProtected assert IsFeatureImplemented(FEAT_RME_GDI); return paspace == PAS_NonSecureProtected; when GPT_NA6 assert IsFeatureImplemented(FEAT_RME_GDI); return FALSE; when GPT_NA7 assert IsFeatureImplemented(FEAT_RME_GDI); return FALSE; when GPT_Any
```

```
return TRUE; otherwise Unreachable();
```

## J1.3.5.41 GPIIndex

```
// GPIIndex() // ========== integer GPIIndex(bits(56) pa) case DecodePGS(GPCCR_EL3.PGS) of when PGS_4KB return UInt(pa<15:12>); when PGS_16KB return UInt(pa<17:14>); when PGS_64KB return UInt(pa<19:16>); otherwise Unreachable();
```

## J1.3.5.42 GPIValid

```
// GPIValid() // ========== // Returns whether a given value is a valid encoding for a GPI value boolean GPIValid(bits(4) gpi) case gpi of when GPT_NoAccess return TRUE; when GPT_NonSecureProtected return IsFeatureImplemented(FEAT_RME_GDI) && GPCCR_EL3.NSP == '1'; when GPT_SystemAgent return IsFeatureImplemented(FEAT_RME_GDI) && GPCCR_EL3.SA == '1'; when GPT_NA6 return IsFeatureImplemented(FEAT_RME_GDI) && GPCCR_EL3.NA6 == '1'; when GPT_NA7 return IsFeatureImplemented(FEAT_RME_GDI) && GPCCR_EL3.NA7 == '1'; when GPT_Secure return IsFeatureImplemented(FEAT_SEL2); when GPT_NonSecure return TRUE; when GPT_Realm return TRUE; when GPT_Root return TRUE; when GPT_NonSecureOnly return IsFeatureImplemented(FEAT_RME_GPC2) && GPCCR_EL3.NSO == '1'; when GPT_Any return TRUE; otherwise return FALSE;
```

## J1.3.5.43 GPT

```
// GPT dimensions // ============== constant AddressSize GPTRange_4KB = 12; constant AddressSize GPTRange_16KB = 14; constant AddressSize GPTRange_64KB = 16; constant AddressSize GPTRange_2MB = 21; constant AddressSize GPTRange_32MB = 25; constant AddressSize GPTRange_512MB = 29; constant AddressSize GPTRange_1GB = 30;
```

```
constant AddressSize GPTRange_16GB = 34; constant AddressSize GPTRange_64GB = 36; constant AddressSize GPTRange_512GB = 39;
```

## J1.3.5.44 GPTBlockDescriptorValid

```
// GPTBlockDescriptorValid() // ========================= // Returns TRUE if the given GPT Block descriptor is valid, and FALSE otherwise. boolean GPTBlockDescriptorValid(bits(64) level_0_entry) assert level_0_entry<3:0> == GPT_Block; return IsZero(level_0_entry<63:8>) && GPIValid(level_0_entry<7:4>);
```

## J1.3.5.45 GPTContigDescriptorValid

```
// GPTContigDescriptorValid() // ========================== // Returns TRUE if the given GPT Contiguous descriptor is valid, and FALSE otherwise. boolean GPTContigDescriptorValid(bits(64) level_1_entry) assert level_1_entry<3:0> == GPT_Contig; return (IsZero(level_1_entry<63:10>) && !IsZero(level_1_entry<9:8>) && GPIValid(level_1_entry<7:4>));
```

## J1.3.5.46 GPTEntry

```
// GPTEntry // ======== type GPTEntry is ( bits(4) gpi, // GPI value for this region AddressSize size, // Region size AddressSize contig_size, // Contiguous region size integer level, // Level of GPT lookup bits(56) pa // PA uniquely identifying the GPT entry )
```

## J1.3.5.47 GPTGranulesDescriptorValid

```
// GPTGranulesDescriptorValid() // ============================ // Returns TRUE if the given GPT Granules descriptor is valid, and FALSE otherwise. boolean GPTGranulesDescriptorValid(bits(64) level_1_entry) for i = 0 to 15 if !GPIValid(level_1_entry<i*4 +:4>) then return FALSE; return TRUE;
```

## J1.3.5.48 GPTL0Size

```
// GPTL0Size() // =========== // Returns number of bits covered by a level 0 GPT entry AddressSize GPTL0Size() case GPCCR_EL3.L0GPTSZ of when '0000' return GPTRange_1GB; when '0100' return GPTRange_16GB; when '0110' return GPTRange_64GB; when '1001' return GPTRange_512GB; otherwise Unreachable(); return 30;
```

## J1.3.5.49 GPTLevel0EntryValid

```
// GPTLevel0EntryValid() // ===================== // Returns TRUE if the given level 0 gpt descriptor is valid, and FALSE boolean GPTLevel0EntryValid(bits(64) gpt_entry) case gpt_entry<3:0> of when GPT_Block return GPTBlockDescriptorValid(gpt_entry); when GPT_Table return GPTTableDescriptorValid(gpt_entry); otherwise return FALSE;
```

```
J1.3.5.50 GPTLevel0Index PA.
```

```
// GPTLevel0Index() // ================ // Compute the level 0 index based on input integer GPTLevel0Index(bits(56) pa) // Input address and index bounds constant integer pps = DecodePPS(); constant integer l0sz = GPTL0Size(); if pps <= l0sz then return 0; return UInt(pa<pps-1:l0sz>);
```

## J1.3.5.51 GPTLevel1EntryValid

```
// GPTLevel1EntryValid() // ===================== // Returns TRUE if the given level 1 gpt descriptor is valid, and FALSE boolean GPTLevel1EntryValid(bits(64) gpt_entry) case gpt_entry<3:0> of when GPT_Contig return GPTContigDescriptorValid(gpt_entry); otherwise return GPTGranulesDescriptorValid(gpt_entry);
```

```
otherwise.
```

```
otherwise.
```

## J1.3.5.52 GPTLevel1Index

```
// GPTLevel1Index() // ================ // Compute the level 1 index based on input PA. integer GPTLevel1Index(bits(56) pa) // Input address and index bounds constant integer l0sz = GPTL0Size(); case DecodePGS(GPCCR_EL3.PGS) of when PGS_4KB return when PGS_16KB return when PGS_64KB return otherwise Unreachable();
```

```
// GPTWalk() // ========= // Get the GPT entry for a given physical address, pa (GPCFRecord, GPTEntry) GPTWalk(bits(56) pa, AccessDescriptor accdesc) // GPT base address bits(56) base; pgs = DecodePGS(GPCCR_EL3.PGS); // The level 0 GPT base address is aligned to the greater of: // * the size of the level 0 GPT, determined by GPCCR_EL3.{PPS, // * 4KB base = ZeroExtend(GPTBR_EL3.BADDR:Zeros(12), 56); pps = DecodePPS(); l0sz = GPTL0Size(); constant integer alignment = Max((pps l0sz) + 3, 12); base<alignment-1:0> = Zeros(alignment); constant AccessDescriptor gptaccdesc = CreateAccDescGPTW(accdesc); // Access attributes and address for GPT fetches AddressDescriptor gptaddrdesc;
```

```
UInt(pa<l0sz-1:16>); UInt(pa<l0sz-1:18>); UInt(pa<l0sz-1:20>); J1.3.5.53 GPTTable // GPTTable // ======== type GPTTable is ( bits(56) address // Base address of next table ) J1.3.5.54 GPTTableDescriptorValid // GPTTableDescriptorValid() // ========================= // Returns TRUE if the given GPT Table descriptor is valid, and FALSE otherwise. boolean GPTTableDescriptorValid(bits(64) level_0_entry) assert level_0_entry<3:0> == GPT_Table; constant integer l0sz = GPTL0Size(); constant PGSe pgs = DecodePGS(GPCCR_EL3.PGS); constant integer p = DecodePGSRange(pgs); return IsZero(level_0_entry<63:52,11:4>) && IsZero(level_0_entry<(l0sz-p)-2:12>); J1.3.5.55 GPTWalk L0GPTSZ}.
```

```
gptaddrdesc.memattrs = WalkMemAttrs(GPCCR_EL3.SH, GPCCR_EL3.IRGN, GPCCR_EL3.ORGN); gptaddrdesc.fault = NoFault(gptaccdesc); gptaddrdesc.paddress.paspace = PAS_Root; gptaddrdesc.paddress.address = base + GPTLevel0Index(pa) * 8; // Fetch L0GPT entry bits(64) level_0_entry; PhysMemRetStatus memstatus; (memstatus, level_0_entry) = PhysMemRead(gptaddrdesc, 8, gptaccdesc); if IsFault(memstatus) then return (GPCFault(GPCF_EABT, 0), GPTEntry UNKNOWN); if !GPTLevel0EntryValid(level_0_entry) then return (GPCFault(GPCF_Walk, 0), GPTEntry UNKNOWN); GPTEntry result; GPTTable table; case level_0_entry<3:0> of when GPT_Block // Decode the GPI value and return that result = DecodeGPTBlock(pgs, level_0_entry); result.pa = pa; return (GPCNoFault(), result); when GPT_Table // Decode the table entry and continue walking table = DecodeGPTTable(pgs, level_0_entry); // The address must be within the range covered by the GPT if AbovePPS(table.address) then return (GPCFault(GPCF_AddressSize, 0), GPTEntry UNKNOWN); otherwise // An invalid encoding would be caught by GPTLevel0EntryValid() Unreachable(); // Must be a GPT Table entry assert level_0_entry<3:0> == GPT_Table; // Address of level 1 GPT entry offset = GPTLevel1Index(pa) * 8; bits(64) level_1_entry; if IsFeatureImplemented(FEAT_RME_GDI) then // When FEAT_RME_GDI is implemented, the descriptor validation checks are performed // on a pair of descriptors within a naturally aligned 16-byte region of memory. gptaddrdesc.paddress.address = Align(table.address + offset, 16); bits(64) level_1_entry_lower; (memstatus, level_1_entry_lower) = PhysMemRead(gptaddrdesc, 8, gptaccdesc); if IsFault(memstatus) then return (GPCFault(GPCF_EABT, 1), GPTEntry UNKNOWN); gptaddrdesc.paddress.address = gptaddrdesc.paddress.address + 8; bits(64) level_1_entry_upper; (memstatus, level_1_entry_upper) = PhysMemRead(gptaddrdesc, 8, gptaccdesc); if IsFault(memstatus) then return (GPCFault(GPCF_EABT, 1), GPTEntry UNKNOWN); // An individual GPT descriptor is valid when both descriptors within the pair are valid. if (!GPTLevel1EntryValid(level_1_entry_upper) || !GPTLevel1EntryValid(level_1_entry_lower)) then return (GPCFault(GPCF_Walk, 1), GPTEntry UNKNOWN); if offset<3> == '1' then level_1_entry = level_1_entry_upper; else level_1_entry = level_1_entry_lower;
```

```
else gptaddrdesc.paddress.address = table.address + offset; // Fetch L1GPT entry (memstatus, level_1_entry) = PhysMemRead(gptaddrdesc, 8, gptaccdesc); if IsFault(memstatus) then return (GPCFault(GPCF_EABT, 1), GPTEntry UNKNOWN); if !GPTLevel1EntryValid(level_1_entry) then return (GPCFault(GPCF_Walk, 1), GPTEntry UNKNOWN); case level_1_entry<3:0> of when GPT_Contig result = DecodeGPTContiguous(pgs, level_1_entry); otherwise gpi_index = GPIIndex(pa); result = DecodeGPTGranules(pgs, gpi_index, level_1_entry); result.pa = pa; return (GPCNoFault(), result); J1.3.5.56 GranuleProtectionCheck accdesc)
```

```
// GranuleProtectionCheck() // ======================== // Returns whether a given access is permitted, according to the // granule protection check. // addrdesc and accdesc describe the access to be checked. GPCFRecord GranuleProtectionCheck(AddressDescriptor addrdesc, AccessDescriptor assert IsFeatureImplemented(FEAT_RME); // The address to be checked address = addrdesc.paddress; // Bypass mode - all accesses pass if GPCCR_EL3.GPC == '0' then return GPCNoFault(); // Configuration consistency check if !GPCRegistersConsistent() then return GPCFault(GPCF_Walk, 0); if IsFeatureImplemented(FEAT_RME_GPC2) then boolean access_disabled; case address.paspace of when PAS_Secure access_disabled = GPCCR_EL3.SPAD == '1'; when PAS_NonSecure access_disabled = GPCCR_EL3.NSPAD == '1'; when PAS_Realm access_disabled = GPCCR_EL3.RLPAD == '1'; when PAS_Root access_disabled = FALSE; otherwise Unreachable(); if access_disabled then return GPCFault(GPCF_Fail, 0); // Input address size check if AbovePPS(address.address) then if (address.paspace == PAS_NonSecure || (IsFeatureImplemented(FEAT_RME_GPC2) && GPCCR_EL3.APPSAA == '1')) then return GPCNoFault(); else return GPCFault(GPCF_Fail, 0); if (IsFeatureImplemented(FEAT_RME_GPC3) && GPCCR_EL3.GPCBW == '1' && PAWithinGPCBypassWindow(address.address)) then
```

```
return GPCNoFault(); // GPT base address size check constant bits(56) gpt_base = ZeroExtend(GPTBR_EL3.BADDR:Zeros(12), 56); if AbovePPS(gpt_base) then return GPCFault(GPCF_AddressSize, 0); // GPT lookup (gpcf, gpt_entry) = GPTWalk(address.address, accdesc); if gpcf.gpf != GPCF_None then return gpcf; // Check input physical address space against GPI permitted = GPICheck(address.paspace, gpt_entry.gpi, accdesc.ss); if !permitted then gpcf = GPCFault(GPCF_Fail, gpt_entry.level); return gpcf; // Check passed return GPCNoFault(); J1.3.5.57 IsGranuleProtectionCheckedAccess // IsGranuleProtectionCheckedAccess() // ================================== // Check if the access should be subject to Granule protection check returns // true if it is, false otherwise boolean IsGranuleProtectionCheckedAccess(AccessDescriptor accdesc) if accdesc.acctype == AccessType_DC then return boolean IMPLEMENTATION_DEFINED "GPC Fault on DC operations"; return TRUE; J1.3.5.58 PAWithinGPCBypassWindow // PAWithinGPCBypassWindow() // ========================= // Check if the supplied address is within a GPC Bypass window. boolean PAWithinGPCBypassWindow(bits(56) pa_in) // Only check the top 26 bits as the minimum window size is 1GB constant bits(26) pa = pa_in<55:30>; constant integer gpcbwl = UInt(GPCBW_EL3.BWSIZE); constant integer gpcbwu = 9 + UInt(GPCBW_EL3.BWSTRIDE); return pa<gpcbwu:gpcbwl> == GPCBW_EL3.BWADDR<gpcbwu:gpcbwl>; J1.3.5.59 PGS
```

```
// PGS // === // Physical granule size enumeration PGSe { PGS_4KB, PGS_16KB, PGS_64KB };
```

## J1.3.5.60 Table

```
// Table format information // ======================== // Granule Protection Table constants constant bits(4) GPT_NoAccess = '0000'; constant bits(4) GPT_Table = '0011'; constant bits(4) GPT_Block = '0001'; constant bits(4) GPT_Contig = '0001'; constant bits(4) GPT_SystemAgent = '0100'; constant bits(4) GPT_NonSecureProtected constant bits(4) GPT_NA6 = '0110'; constant bits(4) GPT_NA7 = '0111'; constant bits(4) GPT_Secure = '1000'; constant bits(4) GPT_NonSecure = '1001'; constant bits(4) GPT_Root = '1010'; constant bits(4) GPT_Realm = '1011'; constant bits(4) GPT_NonSecureOnly = '1101'; constant bits(4) GPT_Any = '1111';
```

```
// S1TranslationRegime() // ===================== // Stage 1 translation regime for the given Exception level bits(2) S1TranslationRegime(bits(2) el) if el != EL0 then return el; elsif HaveEL(EL3) && ELUsingAArch32(EL3) && SCR.NS == '0' then return EL3; elsif IsFeatureImplemented(FEAT_VHE) && ELIsInHost(el) then return EL2; else return EL1; // S1TranslationRegime() // ===================== // Returns the Exception level controlling the current Stage 1 translation regime. For the most // part this is unused in code because the System register accessors (SCTLR_ELx, etc.) implicitly // return the correct value. bits(2) S1TranslationRegime() return S1TranslationRegime(PSTATE.EL);
```

```
= '0101'; J1.3.5.61 S1TranslationRegime J1.3.5.62 AddressDescriptor
```

```
constant integer FINAL_LEVEL = 3; // AddressDescriptor // ================= // Descriptor used to access the underlying memory array. type AddressDescriptor is ( FaultRecord fault, // fault.statuscode indicates whether the address is valid MemoryAttributes memattrs, FullAddress paddress, boolean s1assured, // Stage 1 Assured Translation Property boolean s2fs1mro, // Stage 2 MRO permission for Stage 1 bits(16) mecid, // FEAT_MEC: Memory Encryption Context ID
```

```
bits(64) vaddress
```

)

## J1.3.5.63 ContiguousSize

```
// ContiguousSize() // ================ // Return the number of entries log 2 marking a contiguous output range integer ContiguousSize(bit d128, TGx tgx, integer level) if d128 == '1' then case tgx of when TGx_4KB assert level IN {1, 2, 3}; return if level == 1 then 2 else 4; when TGx_16KB assert level IN {1, 2, 3}; if level == 1 then return 2; elsif level == 2 then return 4; else return 6; when TGx_64KB assert level IN {2, 3}; return if level == 2 then 6 else 4; else case tgx of when TGx_4KB assert level IN {1, 2, 3}; return 4; when TGx_16KB assert level IN {2, 3}; return if level == 2 then 5 else 7; when TGx_64KB assert level IN {2, 3}; return 5;
```

## J1.3.5.64 CreateAddressDescriptor

```
// CreateAddressDescriptor() // ========================= // Set internal members for address descriptor type to valid values AddressDescriptor CreateAddressDescriptor(FullAddress pa, MemoryAttributes memattrs, AccessDescriptor accdesc) AddressDescriptor addrdesc; addrdesc.paddress = pa; addrdesc.memattrs = memattrs; addrdesc.fault = NoFault(accdesc); return addrdesc; // CreateAddressDescriptor() // ========================= // Set internal members for address descriptor type to valid values AddressDescriptor CreateAddressDescriptor(bits(64) va, FullAddress pa, MemoryAttributes memattrs, AccessDescriptor accdesc) AddressDescriptor addrdesc; addrdesc.paddress = pa; addrdesc.vaddress = va;
```

```
addrdesc.memattrs = memattrs; addrdesc.fault = NoFault(accdesc); addrdesc.s1assured = FALSE; return addrdesc;
```

## J1.3.5.65 CreateFaultyAddressDescriptor

```
// CreateFaultyAddressDescriptor() // =============================== // Set internal members for address descriptor type with values indicating error AddressDescriptor CreateFaultyAddressDescriptor(FaultRecord fault) AddressDescriptor addrdesc; addrdesc.vaddress = fault.vaddress; addrdesc.fault = fault; return addrdesc;
```

## J1.3.5.66 DecodePASpace

```
// DecodePASpace() // =============== // Decode the target PA Space PASpace DecodePASpace(bit nse2, bit nse, bit ns) case nse2:nse:ns of when '000' return PAS_Secure; when '001' return PAS_NonSecure; when '010' return PAS_Root; when '011' return PAS_Realm; when '100' return PAS_SystemAgent; when '101' return PAS_NonSecureProtected; when '110' return PAS_NA6; when '111' return PAS_NA7; otherwise Unreachable();
```

## J1.3.5.67 DescriptorType

```
// DescriptorType // ============== // Translation table descriptor formats enumeration DescriptorType { DescriptorType_Table, DescriptorType_Leaf, DescriptorType_Invalid };
```

## J1.3.5.68 Domains

```
// Domains // ======= // Short-descriptor format Domains constant bits(2) Domain_NoAccess = '00'; constant bits(2) Domain_Client = '01'; constant bits(2) Domain_Manager = '11';
```

## J1.3.5.69 FetchDescriptor

```
// FetchDescriptor() // ================= // Fetch a translation table descriptor (FaultRecord, bits(N)) FetchDescriptor(bit ee, AddressDescriptor walkaddress, AccessDescriptor walkaccess, FaultRecord fault_in, integer N) // 32-bit descriptors for AArch32 Short-descriptor format // 64-bit descriptors for AArch64 or AArch32 Long-descriptor format // 128-bit descriptors for AArch64 when FEAT_D128 is set and {V}TCR_ELx.d128 is set assert N == 32 || N == 64 || N == 128; bits(N) descriptor; FaultRecord fault = fault_in; if IsFeatureImplemented(FEAT_RME) then fault.gpcf = GranuleProtectionCheck(walkaddress, walkaccess); if fault.gpcf.gpf != GPCF_None then fault.statuscode = Fault_GPCFOnWalk; fault.paddress = walkaddress.paddress; fault.gpcfs2walk = fault.secondstage; return (fault, bits(N) UNKNOWN); PhysMemRetStatus memstatus; (memstatus, descriptor) = PhysMemRead(walkaddress, N DIV 8, walkaccess); if IsFault(memstatus) then constant boolean iswrite = FALSE; fault = HandleExternalTTWAbort(memstatus, iswrite, walkaddress, walkaccess, N DIV 8, fault); if IsFault(fault.statuscode) then return (fault, bits(N) UNKNOWN); if ee == '1' then descriptor = BigEndianReverse(descriptor); return (fault, descriptor);
```

## J1.3.5.70

```
// HasUnprivileged() // ================= // Returns whether a translation regime serves EL0 as well as a higher EL boolean HasUnprivileged(Regime regime) return (regime IN { Regime_EL20, Regime_EL30, Regime_EL10 });
```

## J1.3.5.71 Regime

```
// Regime // ====== // Translation regimes enumeration Regime { Regime_EL3, // EL3 Regime_EL30, // EL3&0 (PL1&0 when EL3 Regime_EL2, // EL2 Regime_EL20, // EL2&0 Regime_EL10 // EL1&0
```

```
HasUnprivileged is AArch32)
```

};

## J1.3.5.72 RegimeUsingAArch32

```
// RegimeUsingAArch32() // ==================== // Determine if the EL controlling the regime executes in AArch32 state boolean RegimeUsingAArch32(Regime regime) case regime of when Regime_EL10 return ELUsingAArch32(EL1); when Regime_EL30 return TRUE; when Regime_EL20 return FALSE; when Regime_EL2 return ELUsingAArch32(EL2); when Regime_EL3 return FALSE; J1.3.5.73 S1TTWParams '1' '1' '1'
```

```
// S1TTWParams // =========== // Register fields corresponding to stage 1 translation // For A32-VMSA, if noted, they correspond to A32-LPAE (Long descriptor format) type S1TTWParams is ( // A64-VMSA exclusive parameters bit ha, // TCR_ELx.HA bit hd, // TCR_ELx.HD bit tbi, // TCR_ELx.TBI{x} bit tbid, // TCR_ELx.TBID{x} bit nfd, // TCR_EL1.NFDx or TCR_EL2.NFDx when HCR_EL2.E2H == '1' bit e0pd, // TCR_EL1.E0PDx or TCR_EL2.E0PDx when HCR_EL2.E2H == '1' bit d128, // TCR_ELx.D128 bit aie, // (TCR2_ELx/TCR_EL3).AIE MAIRType mair2, // MAIR2_ELx bit ds, // TCR_ELx.DS bits(3) ps, // TCR_ELx.{I}PS bits(6) txsz, // TCR_ELx.TxSZ bit epan, // SCTLR_EL1.EPAN or SCTLR_EL2.EPAN when HCR_EL2.E2H == bit dct, // HCR_EL2.DCT bit nv1, // HCR_EL2.NV1 bit cmow, // SCTLR_EL1.CMOW or SCTLR_EL2.CMOW when HCR_EL2.E2H == bit pnch, // TCR{2}_ELx.PnCH bit disch, // TCR{2}_ELx.DisCH bit haft, // TCR{2}_ELx.HAFT bit mtx, // TCR_ELx.MTX{y} bits(2) skl, // TTBRn_ELx.SKL bit pie, // TCR2_ELx.PIE or TCR_EL3.PIE S1PIRType pir, // PIR_ELx S1PIRType pire0, // PIRE0_EL1 or PIRE0_EL2 when HCR_EL2.E2H == '1' bit emec, // SCTLR2_EL2.EMEC or SCTLR2_EL3.EMEC bit amec, // TCR2_EL2.AMEC0 or TCR2_EL2.AMEC1 when HCR_EL2.E2H == bit fng, // TCR2_EL1.FNGx or TCR2_EL2.FNGx when HCR_EL2.E2H == '1' bit fngna, // TCR2_EL1.FNGx // A32-VMSA exclusive parameters bits(3) t0sz, // TTBCR.T0SZ bits(3) t1sz, // TTBCR.T1SZ bit uwxn, // SCTLR.UWXN // Parameters common to both A64-VMSA & A32-VMSA (A64/A32) TGx tgx, // TCR_ELx.TGx / Always TGx_4KB bits(2) irgn, // TCR_ELx.IRGNx / TTBCR.IRGNx or HTCR.IRGN0 bits(2) orgn, // TCR_ELx.ORGNx / TTBCR.ORGNx or HTCR.ORGN0
```

```
bits(2) sh, // TCR_ELx.SHx / TTBCR.SHx or HTCR.SH0 bit hpd, // TCR_ELx.HPD{x} / TTBCR2.HPDx or HTCR.HPD bit ee, // SCTLR_ELx.EE / SCTLR.EE or HSCTLR.EE bit wxn, // SCTLR_ELx.WXN / SCTLR.WXN or HSCTLR.WXN bit ntlsmd, // SCTLR_ELx.nTLSMD / SCTLR.nTLSMD bit dc, // HCR_EL2.DC / HCR.DC bit sif, // SCR_EL3.SIF / SCR.SIF MAIRType mair // MAIR_ELx / MAIR1:MAIR0 or HMAIR1:HMAIR0
```

```
or HSCTLR.nTLSMD )
```

## J1.3.5.74 S2TTWParams

```
// S2TTWParams // =========== // Register fields corresponding to stage 2 translation. type S2TTWParams is ( // A64-VMSA exclusive parameters bit ha, // VTCR_EL2.HA bit hd, // VTCR_EL2.HD bit sl2, // V{S}TCR_EL2.SL2 bit ds, // VTCR_EL2.DS bit d128, // VTCR_ELx.D128 bit sw, // VSTCR_EL2.SW bit nsw, // VTCR_EL2.NSW bit sa, // VSTCR_EL2.SA bit nsa, // VTCR_EL2.NSA bits(3) ps, // VTCR_EL2.PS bits(6) txsz, // V{S}TCR_EL2.T0SZ bit fwb, // HCR_EL2.FWB bit cmow, // HCRX_EL2.CMOW bits(2) skl, // VTTBR_EL2.SKL bit s2pie, // VTCR_EL2.S2PIE S2PIRType s2pir, // S2PIR_EL2 bit tl0, // VTCR_EL2.TL0 bit tl1, // VTCR_EL2.TL1 bit assuredonly,// VTCR_EL2.AssuredOnly bit haft, // VTCR_EL2.HAFT bit emec, // SCTLR2_EL2.EMEC bit hdbss, // VTCR_EL2.HDBSS // A32-VMSA exclusive parameters bit s, // VTCR.S bits(4) t0sz, // VTCR.T0SZ // Parameters common to both A64-VMSA & A32-VMSA if implemented (A64/A32) TGx tgx, // V{S}TCR_EL2.TG0 / Always TGx_4KB bits(2) sl0, // V{S}TCR_EL2.SL0 / VTCR.SL0 bits(2) irgn, // VTCR_EL2.IRGN0 / VTCR.IRGN0 bits(2) orgn, // VTCR_EL2.ORGN0 / VTCR.ORGN0 bits(2) sh, // VTCR_EL2.SH0 / VTCR.SH0 bit ee, // SCTLR_EL2.EE / HSCTLR.EE bit ptw, // HCR_EL2.PTW / HCR.PTW bit vm // HCR_EL2.VM / HCR.VM )
```

## J1.3.5.75 SDFType

```
// SDFType // ======= // Short-descriptor format type enumeration SDFType {
```

```
SDFType_Table, SDFType_Invalid, SDFType_Supersection, SDFType_Section, SDFType_LargePage, SDFType_SmallPage };
```

## J1.3.5.76 SecurityStateForRegime

```
// SecurityStateForRegime() // ======================== // Return the Security State of the given translation regime SecurityState SecurityStateForRegime(Regime regime) case regime of when Regime_EL3 return SecurityStateAtEL(EL3); when Regime_EL30 return SS_Secure; // A32 EL3 is always Secure when Regime_EL2 return SecurityStateAtEL(EL2); when Regime_EL20 return SecurityStateAtEL(EL2); when Regime_EL10 return SecurityStateAtEL(EL1);
```

## J1.3.5.77 StageOA

```
// StageOA() // ========= // Given the final walk state (a page or block descriptor), map the untranslated // input address bits to the output address FullAddress StageOA(bits(64) ia, bit d128, TGx tgx, TTWState walkstate) // Output Address FullAddress oa; constant integer tsize = TranslationSize(d128, tgx, walkstate.level); constant integer csize = (if walkstate.contiguous == '1' then ContiguousSize(d128, tgx, walkstate.level) else 0); constant AddressSize ia_msb = tsize + csize; oa.paspace = walkstate.baseaddress.paspace; oa.address = walkstate.baseaddress.address<55:ia_msb>:ia<ia_msb-1:0>; return oa;
```

## J1.3.5.78 TGx

```
// TGx // === // Translation granules sizes enumeration TGx { TGx_4KB, TGx_16KB, TGx_64KB };
```

## J1.3.5.79 TGxGranuleBits

```
// TGxGranuleBits() // ================ // Retrieve the address size, in bits, of a AddressSize TGxGranuleBits(TGx tgx) case tgx of when TGx_4KB return 12; when TGx_16KB return 14; when TGx_64KB return 16;
```

```
granule
```

```
// TLBContext // ========== // Translation context compared on TLB lookups and invalidations, promoting a TLB hit on match type TLBContext is ( SecurityState ss, Regime regime, bits(16) vmid, bits(16) asid, bit nG, PASpace ipaspace, // Used in stage 2 lookups & invalidations only boolean includes_s1, boolean includes_s2, boolean use_vmid, boolean includes_gpt, bits(64) ia, // Input Address TGx tg, bit cnp, integer level, // Assist TLBI level hints (FEAT_TTL) boolean isd128, bit xs // XS attribute (FEAT_XS) )
```

```
// TLBRecord // ========= // Translation output as a TLB payload type TLBRecord is ( TLBContext context, TTWState walkstate, AddressSize blocksize, // Number of bits directly mapped from IA to OA integer contigsize,// Number of entries log 2 marking a contiguous output range bits(128) s1descriptor, // Stage 1 leaf descriptor in memory (valid if the TLB caches stage 1) bits(128) s2descriptor // Stage 2 leaf descriptor in memory (valid if the TLB caches stage 2) )
```

```
J1.3.5.80 TLBContext J1.3.5.81 TLBRecord J1.3.5.82 TTWState // TTWState // ======== // Translation table walk state type TTWState is ( boolean istable, integer level,
```

```
FullAddress baseaddress, bit contiguous, boolean s1assured, // Stage 1 Assured Translation Property bit s2assuredonly, // Stage 2 AssuredOnly attribute bit disch, // Stage 1 Disable Contiguous Hint bit nG, bit guardedpage, SDFType sdftype, // AArch32 Short-descriptor format walk only bits(4) domain, // AArch32 Short-descriptor format walk only MemoryAttributes memattrs, Permissions permissions
```

```
) J1.3.5.83 TranslationRegime // TranslationRegime() // =================== // Select the translation regime given the target EL and PE state Regime TranslationRegime(bits(2) el) if el == EL3 then return if ELUsingAArch32(EL3) then Regime_EL30 else Regime_EL3; elsif el == EL2 then return if ELIsInHost(EL2) then Regime_EL20 else Regime_EL2; elsif el == EL1 then return Regime_EL10; elsif el == EL0 then if CurrentSecurityState() == SS_Secure && ELUsingAArch32(EL3) then return Regime_EL30; elsif ELIsInHost(EL0) then return Regime_EL20; else return Regime_EL10; else Unreachable(); J1.3.5.84 TranslationSize // TranslationSize() // ================= // Compute the number of bits directly mapped from the input address // to the output address AddressSize TranslationSize(bit d128, TGx tgx, integer level) granulebits = TGxGranuleBits(tgx); descsizelog2 = if d128 == '1' then 4 else 3; blockbits = (FINAL_LEVEL -level) * (granulebits - descsizelog2); return granulebits + blockbits; J1.3.5.85 UseASID
```

```
// UseASID() // ========= // Determine whether the translation context for the access requires ASID or is a global entry boolean UseASID(TLBContext accesscontext) return HasUnprivileged(accesscontext.regime);
```

## J1.3.5.86 UseVMID

```
// UseVMID() // ========= // Determine whether the translation context for the access requires VMID to match a TLB entry boolean UseVMID(Regime regime) return regime == Regime_EL10 && EL2Enabled();
```