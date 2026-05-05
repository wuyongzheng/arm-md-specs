## C6.2.423 STSHH

Store shared hint

This instruction signals to the memory system that if the next instruction in program order generates an explicit write effect, then it is to a location that one or more other threads of execution will observe, and there is a performance benefit to ensuring that the updated value from the write to that location propagates to those other observers with minimal latency.

The thread of execution on the other observers might be polling the location using load or load-exclusive instructions, or may have executed a PRFM IR instruction targeting the location.

## System

(FEAT\_PCDPHINT)

<!-- image -->

## Encoding

```
STSHH <policy>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_PCDPHINT) then EndOfDecode(Decode_NOP); constant boolean stream = op2<0> == '1';
```

## Assembler Symbols

## &lt;policy&gt;

&lt;policy&gt; is one of:

KEEP Signals to the memory system that there may be a performance benefit to retaining the updated location in the local cache of the updating PE.

STRM Signals to the memory system that there may be a performance benefit to ensuring the updated location is not retained in the local cache of the updating PE.

|   op2<0> | <policy>   |
|----------|------------|
|        0 | KEEP       |
|        1 | STRM       |

## Operation

Hint\_StoreShared(stream);
