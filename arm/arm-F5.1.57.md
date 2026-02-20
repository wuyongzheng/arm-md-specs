## F5.1.57 IT

If-Then makes up to four following instructions (the IT block) conditional. The conditions for the instructions in the IT block are the same as, or the inverse of, the condition the IT instruction specifies for the first instruction in the block.

The IT instruction itself does not affect the condition flags, but the execution of the instructions in the IT block can change the condition flags.

16-bit instructions in the IT block, other than CMP , CMN and TST , do not set the condition flags. An IT instruction with the AL condition can change the behavior without conditional execution.

The architecture permits exception return to an instruction in the IT block only if the restoration of the CPSR restores PSTATE.IT to a state consistent with the conditions specified by the IT instruction. Any other exception return to an instruction in an IT block is UNPREDICTABLE. Any branch to a target instruction in an IT block is not permitted, and if such a branch is made it is UNPREDICTABLE what condition is used when executing that target instruction and any subsequent instruction in the IT block.

Many uses of the IT instruction are deprecated for performance reasons, and an implementation might include ITD controls that can disable those uses of IT, making them UNDEFINED.

For more information see Conditional execution and Conditional instructions. The first of these sections includes more information about the ITD controls.

<!-- image -->

## Encoding

```
IT{<x>{<y>{<z>}}}{<q>} <cond>
```

## Decode for this encoding

```
if mask == '0000' then SEE "Related encodings"; if firstcond == '1111' || (firstcond == '1110' && BitCount(mask) != 1) then UNPREDICTABLE; if InITBlock() then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If firstcond == '1111' || (firstcond == '1110' &amp;&amp; BitCount(mask) != 1) , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The '1111' condition is treated as being the same as the '1110' condition, meaning always, and the ITSTATE state machine is progressed in the same way as for any other cond\_base value.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

Related encodings: Miscellaneous 16-bit instructions.

## Assembler Symbols

&lt;x&gt;

The condition for the second instruction in the IT block. If omitted, the 'mask' field is set to 0b1000 . If present it is encoded in the 'mask[3]' field:

T

```
firstcond[0] NOTfirstcond[0]
```

E

<!-- image -->

<!-- image -->

<!-- image -->

See Standard assembler syntax fields.

## &lt;cond&gt;

The condition for the first instruction in the IT block, encoded in the 'firstcond' field. See Condition codes for the range of conditions available, and the encodings.

The conditions specified in an IT instruction must match those specified in the syntax of the instructions in its IT block. When assembling to A32 code, assemblers check IT instruction syntax for validity but do not generate assembled instructions for them. See Conditional instructions.

## Operation

```
EncodingSpecificOperations(); AArch32.CheckITEnabled(mask); PSTATE.IT<7:0> = firstcond:mask; ShouldAdvanceIT = FALSE;
```

The condition for the third instruction in the IT block. If omitted and &lt;x&gt; is present, the 'mask[2:0]' field is set to 0b100 . If &lt;y&gt; is present it is encoded in the 'mask[2]' field:

- T firstcond[0]
- E NOTfirstcond[0]

The condition for the fourth instruction in the IT block. If omitted and &lt;y&gt; is present, the 'mask[1:0]' field is set to 0b10 . If &lt;z&gt; is present, the 'mask[0]' field is set to 1, and it is encoded in the 'mask[1]' field:

- T firstcond[0]
- E NOTfirstcond[0]