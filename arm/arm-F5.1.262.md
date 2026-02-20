## F5.1.262 TSB

Trace Synchronization Barrier. This instruction is a barrier that synchronizes the trace operations of instructions, see Trace Synchronization Barrier (TSB).

If FEAT\_TRF is not implemented, this instruction executes as a NOP .

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

(FEAT\_TRF)

<!-- image -->

## Encoding

TSB{&lt;c&gt;}{&lt;q&gt;} CSYNC

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_TRF) then ExecuteAsNOP(); end if cond != '1110' then UNPREDICTABLE; end // TSB must be encoded with AL condition
```

## CONSTRAINED UNPREDICTABLE behavior

If cond != '1110' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes unconditionally.
- The instruction executes conditionally.

T1

(FEAT\_TRF)

<!-- image -->

## Encoding

TSB{&lt;c&gt;}{&lt;q&gt;} CSYNC

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_TRF) then ExecuteAsNOP(); end if InITBlock() then UNPREDICTABLE; end
```

Listing F5-83

Listing F5-84

## CONSTRAINED UNPREDICTABLE behavior

If InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes unconditionally.
- The instruction executes conditionally.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

<!-- image -->

See Standard assembler syntax fields.

## Operation

if ConditionPassed() then EncodingSpecificOperations(); TraceSynchronizationBarrier();

end

Listing F5-85