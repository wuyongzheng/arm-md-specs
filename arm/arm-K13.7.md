## K13.7 Miscellaneous helper procedures and functions

This section lists the prototypes of miscellaneous helper procedures and functions used by the pseudocode, together with a brief description of the effect of the procedure or function. The pseudocode does not define the operation of these helper procedures and functions.

Note

A-profile Architecture Pseudocode also has an entry for each of these functions, but currently these entries do not say anything about the effect of the function. When this information is added in A-profile Architecture Pseudocode, this section will be removed from the manual.

## K13.7.1 EndOfInstruction()

This procedure terminates processing of the current instruction.

EndOfInstruction();

## K13.7.2 Hint\_Debug()

This procedure supplies a hint to the debug system.

Hint\_Debug(bits(4) option);

## K13.7.3 Hint\_PreloadData()

This procedure performs a preload data hint.

Hint\_PreloadData(bits(32) address);

## K13.7.4 Hint\_PreloadDataForWrite()

This procedure performs a preload data hint with a probability that the use will be for a write.

Hint\_PreloadDataForWrite(bits(32) address);

## K13.7.5 Hint\_PreloadInstr()

This procedure performs a preload instructions hint.

Hint\_PreloadInstr(bits(32) address);

## K13.7.6 Hint\_Yield()

This procedure performs a Yield hint.

Hint\_Yield();

## K13.7.7 IsExternalAbort()

This function returns TRUE if the abort currently being processed is an External abort and FALSE otherwise. It is used only in exception entry pseudocode.

```
type)
```

```
boolean IsExternalAbort(Fault assert type != Fault_None;
```

boolean IsExternalAbort(FaultRecord fault);

## K13.7.8 IsAsyncAbort()

This function returns TRUE if the abort currently being processed is an asynchronous abort, and FALSE otherwise. It is used only in exception entry pseudocode.

```
boolean IsAsyncAbort(Fault type) assert type != Fault_None;
```

boolean IsAsyncAbort(FaultRecord

## K13.7.9 LSInstructionSyndrome()

This function returns the extended syndrome information for a fault reported in the HSR.

bits(11) LSInstructionSyndrome();

## K13.7.10 ProcessorID()

This function returns an integer that uniquely identifies the executing PE in the system.

integer ProcessorID();

## K13.7.11 RemapRegsHaveResetValues()

This function returns TRUE if the remap registers PRRR and NMRR have their IMPLEMENTATION DEFINED reset values, and FALSE otherwise.

boolean RemapRegsHaveResetValues();

## K13.7.12 ResetControlRegisters()

This function resets the System registers and memory-mapped control registers that have architecturally defined reset values to those values. For more information about the affected registers, see:

- Reset behavior.
- PE state on reset into AArch32 state.

AArch64.ResetControlRegisters(boolean ResetIsCold)

AArch32.ResetControlRegisters(boolean ResetIsCold)

## K13.7.13 ThisInstr()

This function returns the bitstring encoding of the currently executing instruction.

bits(32) ThisInstr();

Note

Currently, this function is used only on 32-bit instruction encodings.

## K13.7.14 ThisInstrLength()

This function returns the length, in bits, of the current instruction. This means it returns 32 or 16:

integer ThisInstrLength();

```
fault);
```