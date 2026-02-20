## D6.2 The trace buffer

RSDCKT

The Trace Buffer Unit uses one of the following:

- If self-hosted trace is enabled, then Self-hosted mode. See Trace buffer Self-hosted mode.
- If FEAT\_TRBE\_EXT is implemented and self-hosted trace is disabled, then External mode. See Trace buffer External mode.

If and only if one of the following is true, then the Trace Buffer Unit is enabled:

- The Trace Buffer Unit is using Self-hosted mode and TRBLIMITR\_EL1.E is 1.
- The Trace Buffer Unit is using External mode and TRBLIMITR\_EL1.XE is 1.

Otherwise, the Trace Buffer Unit is disabled. See Trace Buffer Unit disabled.

The pseudocode function TraceBufferEnabled() describes this.

If and only if all of the following are true, then the Trace Buffer Unit is running :

- The Trace Buffer Unit is enabled.
- TRBSR\_EL1.S is 0.
- FEAT\_TRBE\_EXC is not implemented, or self-hosted trace is disabled, or all of the following are true:
- -Any of the following are true:
- -EL2 is not implemented.
- -The Effective value of SCR\_EL3.{NS, EEL2} is {0, 0}.
- -TRBSR\_EL2.S is 0.
- -EL3 is implemented and MDCR\_EL3.TRBEE is 0b00 .
- -TRFCR\_EL2.EE is either 0b00 or 0b01 .
- -Any of the following are true:
- -EL3 is not implemented.
- -TRBSR\_EL3.S is 0.
- -MDCR\_EL3.TRBEE is either 0b00 or 0b01 .

The pseudocode function TraceBufferRunning() shows this.

If and only if all of the following are true, then collection is stopped :

- The Trace Buffer Unit is enabled.
- The Trace Buffer Unit is not running.

The pseudocode function TraceBufferRunning() shows this.

Table D6-1 shows whether the Trace Buffer Unit is running when all of the following apply:

- The PE is executing in the trace buffer owning Security state.
- The PE is executing at either the owning Exception level or a lower Exception level.
- Self-hosted trace is enabled.

Each column in the left side of the table refers to the Effective value of a field in a System register.

Table D6-1 Trace Buffer running when self-hosted trace is enabled

| TRBLIMITR_EL1.E   | TRBSR_EL1.S   | MDCR_EL3.TRBEE   | TRBSR_EL3.S   | TRFCR_EL2.EE   | TRBSR_EL2.S   | Running   |
|-------------------|---------------|------------------|---------------|----------------|---------------|-----------|
| 0b0               | X             | XX               | X             | XX             | X             | False     |
| 0b1               | 0b0           | 0b00             | X             | XX             | X             | True      |
| 0b1               | 0b0           | 0b01             | X             | 0b0X           | X             | True      |
| 0b1               | 0b0           | 0b01             | X             | 0b1X           | 0b0           | True      |
| 0b1               | 0b0           | 0b01             | X             | 0b1X           | 0b1           | False     |
| 0b1               | 0b0           | 0b1X             | 0b0           | 0b0X           | X             | True      |

RYCHKJ

RBGLHT

RFRHXV

IYPSDY

| TRBLIMITR_EL1.E   | TRBSR_EL1.S   | MDCR_EL3.TRBEE   | TRBSR_EL3.S   | TRFCR_EL2.EE   | TRBSR_EL2.S   | Running   |
|-------------------|---------------|------------------|---------------|----------------|---------------|-----------|
| 0b1               | 0b0           | 0b1X             | 0b0           | 0b1X           | 0b0           | True      |
| 0b1               | 0b0           | 0b1X             | 0b0           | 0b1X           | 0b1           | False     |
| 0b1               | 0b0           | 0b1X             | 0b1           | XX             | X             | False     |
| 0b1               | 0b1           | XX               | X             | XX             | X             | False     |

IJYSQZ

While the Trace Buffer Unit is enabled, it collects trace data from the trace unit and does one of the following:

- Accepts the trace data and writes it to the trace buffer in memory.

- Discards the trace data. The trace data is lost.

- Rejects the trace data.

RYMYQX When the Trace Buffer Unit is enabled and running , and the Trace Buffer Unit is able to accept the trace data, the Trace Buffer Unit accepts the trace data from the trace unit and writes it into the trace buffer.

RLNTVR

When the Trace Buffer Unit is enabled and running , and the Trace Buffer Unit is not able to accept the trace data, the Trace Buffer Unit rejects the trace data from the trace unit. The trace data might be retained by the trace unit until the Trace Buffer Unit accepts the trace data.

ISQYCT

For example, the Trace Buffer Unit might not be able to accept trace data while its internal buffers are full.

ITRCDR

If the Trace Buffer Unit rejects trace data and the trace unit is not able to retain the trace data, then the trace unit discards it and enters an Overflow state. Details of Overflow state and how the trace unit recovers from Overflow state are defined by the trace unit. See Trace unit behavior on a trace unit buffer overflow.

RYMVZL

When the Trace Buffer Unit is enabled and collection is stopped, the Trace Buffer Unit discards trace data from the trace unit. The trace data is lost.

RPHSKP

When used with a trace unit that implements FEAT\_ETE, the Trace Buffer Unit ignores the value of the ETE TRCTRACEIDR register.

## D6.2.1 Trace Buffer Unit disabled

| R HNTLG   | When the Trace Buffer Unit is disabled, the Trace Buffer Unit discards trace data from the trace unit.                                                                                                                                                                 |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R BSMLW   | The Trace Buffer Unit does not prefetch and cache address translations when the Trace Buffer Unit is disabled.                                                                                                                                                         |
| I YHJDQ   | When the Trace Buffer Unit is disabled the trace unit might send trace data to an IMPLEMENTATION DEFINED trace bus.                                                                                                                                                    |
| R JYTYH   | The trace unit does not send trace data to the IMPLEMENTATION DEFINED trace bus when the Trace Buffer Unit is enabled.                                                                                                                                                 |
| I FPXHD   | Figure D6-1 shows this IMPLEMENTATION DEFINED trace bus as a dotted line to an external trace Sink .                                                                                                                                                                   |
|           | Details of this bus are outside the scope of this architecture, and might require further configuration. For example, if the trace unit implements FEAT_ETE and the trace bus is AMBAATB,the ATID value is configured through the trace unit external trace registers. |

## D6.2.2 Restrictions on programming the Trace Buffer Unit

RMSPSD

A current write pointer value is out-of-range if any of the following are true:

- The current write pointer is less-than the Base pointer , treating both pointers as unsigned integers.
- The current write pointer is greater-than-or-equal-to the Limit pointer , treating both pointers as unsigned integers.
- Bits [63:56] of the current write pointer are not equal to bits [63:56] of the Base pointer .
- Bits [63:56] of the current write pointer are not equal to bits [63:56] of the Limit pointer .

Note: RMSPSD means the current write pointer is out-of-range if the Base pointer is not less-than the Limit pointer or bits [63:56] of the Base pointer are not equal to bits [63:56] of the Limit pointer .

value is misaligned if it is not a multiple of an IMPLEMENTATION DEFINED

- RXXZHM A current write pointer or Trigger Counter alignment specified by TRBIDR\_EL1.Align.
- RHXZZM A current write pointer or Trigger Counter value is a valid restart value if it was previously initialized with a value that was not out-of-range and not misaligned and later read from the applicable register when all of the following are true:
- The Trace Buffer Unit is disabled.
- All trace operations are complete. See RNSFRQ for the definition of complete.
- No External abort has been reported to the Trace Buffer Unit. See The External abort is reported to the Trace Buffer Unit.
- No write by the Trace Buffer Unit has generated an Alignment fault.
- No write by the Trace Buffer Unit has generated an asynchronous SError exception.
- RXZWXQ A current write pointer or Trigger Counter value is a fault value if it was previously initialized with a value that was not out-of-range and not misaligned or a value that was a valid restart value, and later read from the applicable register when all of the following are true:
- The Trace Buffer Unit is disabled.
- All trace operations are complete. See RNSFRQ for the definition of complete.
- One of the following is true:
- -An External abort has been reported to the Trace Buffer Unit. See The External abort is reported to the Trace Buffer Unit.
- -Awrite by the Trace Buffer Unit has generated an Alignment fault.
- -Awrite by the Trace Buffer Unit has generated an asynchronous SError exception.
- ICRSGP An MMU fault does not generate a fault value. If software is able to fix the fault, then the Trace Buffer Unit can restart using the current write pointer and Trigger Counter values.

However, following an MMU fault:

- RYMVZL means the Trace Buffer Unit discards trace because collection is stopped. That is, trace will be lost.
- RBQTGW means that the Trigger Counter might be incorrect if a Detected Trigger has occurred.

See also SGTLCY.

- ISFTPM Following a trace buffer management event, or on a context switch, the current write pointer and Trigger Counter might be misaligned. If TRBIDR\_EL1.Align is nonzero, software should treat bits [ M :0] as SBZP when writing to the applicable register, where M is (TRBIDR\_EL1.Align-1) in each of the following situations:
- When first creating a trace buffer, software sets bits [ M :0] to zero, meaning the registers are set to an aligned value.
- On a context switch, the definitions of a restart value and fault value mean software does not have to validate or modify the value read from hardware.

A current write pointer restart value or fault value will not be out-of-range.

- IVRFQC Afault value is for error handling purposes only. Software must not cause the Trace Buffer Unit to become enabled and running with the current write pointer having a fault value.

Software context switching the Trace Buffer Unit will avoid this issue because the trace buffer management event sets TRBSR\_ELx.S to 1, meaning the Trace Buffer Unit will not become running following the context switch.

- RJWWWM If the current write pointer is written by a direct write with a misaligned value that is not a restart value and not a fault value, the value returned by a subsequent direct read of the current write pointer is UNKNOWN.
- RMGZWR If the current write pointer has an out-of-range value, or a misaligned value that is not a restart value when the Trace Buffer Unit attempts to write to the trace buffer, then any of the following might occur:
- If the value is out-of-range, the current write pointer might be wrapped before or after the write, and the TRB\_WRAPevent might be generated.
- If the value is misaligned, the write might generate an Alignment fault.
- The Trace Buffer Unit might write the trace data to any address in memory that is writable by a privileged access in the owning translation regime. These addresses are:

- -For Self-hosted mode:
- -Virtual addresses in the owning translation regime if the Effective value of TRBLIMITR\_EL1.nVM is 0.
- -Intermediate physical addresses in the owning Security state if the Effective value of
- TRBLIMITR\_EL1.nVM is 1 and the owning translation regime has stage 2 translations.
- -Physical addresses in the owning Security state if the Effective value of TRBLIMITR\_EL1.nVM is 1, and either the owning translation regime has no stage 2 translation or stage 2 translation is disabled.
- -For External mode, any addresses in the physical address space specified by TRBMAR\_EL1.PAS.
- The write might generate a trace buffer management event and the TRB\_WRAP event might be generated:
- -If FEAT\_TRBE\_EXC is not implemented, a buffer management event for an UNKNOWN reason:
- -TRBSR\_EL1.S is either set to 1 or unchanged.
- -TRBSR\_EL1.WRAP is either set to 1 or unchanged.
- -TRBSR\_EL1.EC is set to an UNKNOWN value.
- -TRBSR\_EL1.MSS is set to an UNKNOWN value.
- -If FEAT\_TRBE\_EXC is implemented, a buffer management event for one of the following reasons:
- -ABuffer full buffer management event.
- -ABuffer wrap buffer management event.
- -An Access not allowed buffer management event.
- -Any MMU fault buffer management event.

The management event is recorded as described by RBNQRP.

- All trace data is silently discarded without being written to memory.
- The Trace Buffer Unit behaves as if the trace buffer is disabled.
- RCPDDM If the Trigger Counter is written by a direct write with a misaligned value that is not a restart value, then all of the following apply:
- If the value is not a fault value, the value returned by a subsequent direct read of the Trigger Counter register is UNKNOWN.
- The generation of a Trigger Event while the Trace Buffer Unit remains enabled and running is UNPREDICTABLE.
- IYSXXN RXXZHM and RCPDDM mean an implementation that always keeps the current write pointer and/or Trigger Counter aligned to the IMPLEMENTATION DEFINED alignment specified by TRBIDR\_EL1.Align, where TRBIDR\_EL1.Align is greater-than-zero (byte alignment), can implement bits [ M :0] of the applicable register(s) as RAZ/WI bits, where M is (TRBIDR\_EL1.Align-1).

RHXZZM allows an implementation where an External abort is reported to the Trace Buffer Unit and handled synchronously to implement TRBPTR\_EL1[ M : N ], where N is IMPLEMENTATION SPECIFIC and typically determined by the minimum memory access granule, as read/write bits for the purpose of reporting an External abort fault address, but otherwise ignore the value in these bits. If N&gt;0 , bits [( N-1) :0] can be implemented as RAZ/WI.

- RDJMDD When the following conditions apply, the PE might ignore a direct or external write to any of certain Trace Buffer Unit registers, other than a direct write or external write to TRBLIMITR\_EL1 that clears the conditions:
- TRBLIMITR\_EL1.E is 1, and either FEAT\_TRBE\_EXT is not implemented or the Trace Buffer Unit is using Self-hosted mode.
- TRBLIMITR\_EL1.XE is 1, FEAT\_TRBE\_EXT is implemented, and the Trace Buffer Unit is using External mode.

The Trace Buffer Unit registers affected are:

- The current write pointer , TRBPTR\_EL1.
- The Base pointer , TRBBASER\_EL1.
- The Limit pointer , TRBLIMITR\_EL1.
- The Trigger Counter , TRBTRG\_EL1.
- TRBSR\_EL1.
- TRBSR\_EL2 and TRBSR\_EL3, if FEAT\_TRBE\_EXC is implemented.
- TRBMAR\_EL1.
- TRBMPAM\_EL1, if FEAT\_TRBE\_MPAM is implemented.
- TRBITCTRL, if implemented as part of FEAT\_TRBE\_EXT.

Writes to TRBCR are not affected.

SDSSHH

Software must use appropriate Context synchronization operations to order a direct write that modifies TRBLIMITR\_EL1.E with respect to other direct writes to Trace Buffer Unit registers. This includes a write to enable the Trace Buffer Unit by setting TRBLIMITR\_EL1.E to 1.

See also:

- Synchronization and the Trace Buffer Unit.
- UNPREDICTABLE behavior.
- Context switching.

## D6.2.3 Effect on the exclusive monitors and transactions

| R DCVBN   | If an operation between Load-Exclusive and Store-Exclusive instructions is traced, and the trace data is written to an unrelated address, then the write has no effect on the exclusive monitors.                                                                                                           |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R MDJNK   | If an operation inside a transaction is traced, and the trace data is written to an unrelated address, then the write has no effect on the transaction.                                                                                                                                                     |
| R NWSKV   | If the Trace Buffer Unit writes to the marked address of an exclusives monitor in the Exclusive Access state, then there is a CONSTRAINED UNPREDICTABLE choice of one of the following occuring:                                                                                                            |
| R FVRXJ   | If the Trace Buffer Unit writes to the working set of a transaction, then there is a CONSTRAINED UNPREDICTABLE choice of one of the following occuring: • The write has the same effect on the transaction as a store by any other Observer to that address. • The write has no effect on this transaction. |

## D6.2.4 Effect of MTE

RYGMLW

If FEAT\_MTE is implemented, then the Trace Buffer Unit generates an Unchecked access for each access to the trace buffer.

Note: This is the case even when a Tagged Normal memory type is accessed.

See also The Memory Tagging Extension.