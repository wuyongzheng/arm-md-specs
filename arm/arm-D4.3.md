## D4.3 Trace elements

IFNFWZ

Trace elements form an AST which is used to describe the control flow of program execution. Different sequences of the trace elements can be used to imply the same operation. In this way FEAT\_ETE can be used by different micro-architectures. This is similar to the approach used in previous trace protocols. For more information, see the Arm® Embedded Trace Macrocell Architecture Specification, ETMv4 (ARM IHI 0064) .

IXXBMZ

Atrace unit compresses the information on the execution of the PE and outputs a trace byte stream that comprises of multiple packets of encoded data. The compression techniques that are used include:

## Not having a trace element for every executed instruction in the instruction trace element stream

Instead, the trace unit generates P0 elements in the trace element stream when certain types of instruction are executed. These certain types of instructions are known as P0 instructions . A P0 element acts as a signpost in the program flow, indicating that execution is proceeding along a given path.

Consequently, the stream of P0 elements implies the execution of a greater number of instructions, and a trace analyzer can reconstruct the stream of instructions that are executed between P0 elements by using the P0 element stream and the program image.

## Multiple trace elements in single packets

Common sequences of trace elements are encoded into single packets.

## Removal of program addresses from the trace element stream

The trace analyzer can infer the addresses from the program image and previous history. This includes the targets of direct branch instructions, where the target address is encoded in the instruction itself.

## Removal of predictable trace elements

Some trace elements can be removed from the AST representation if the contents of the trace element can be predicted by previous control flow choices in the software flow. For example the Target Address element for returning from a subroutine might not be required if the branch to the subroutine has been traced.

## D4.3.1 Layer model

IXMFJT

IGLPQZ

Transport Layer

The transport layer either provides either:

- Apath off chip.
- Apath to a memory buffer for trace to be stored.

Layer 1

Layer 1 provides compression by:

FEAT\_ETE is based on a layer model. Each layer deals with a unique aspect of tracing the PE.

Figure D4-4 Layer model for compression and decompression

<!-- image -->

- Grouping trace elements together to form packets.
- Removing trace elements that can be implied.
- Compression against previous values.
- Leading zero compression.
- Reordering of trace elements.

## Layer 2

## Layer 2 provides:

- Speculation resolution.
- Transactional Memory resolution.

## Layer 3

## At layer 3:

- PE behavior is converted into trace elements.
- Compression is achieved by removing the trace elements which can be predicted using the program image:
- -Direct branch target addresses.
- -Return stack optimization.
- Knowledge of the application is required in order to decompress. Processes that modify the instruction opcodes require additional information to allow debugging.

## D4.3.2 Trace protocol synchronization

| I CLTCM   | The trace byte stream of a trace unit is typically stored in a circular buffer where, if the buffer is full, newer trace overwrites older trace. To ensure that a trace stream can be analyzed when the trace has been stored in a circular buffer, trace unit must periodically generate trace protocol synchronization points in the trace byte stream.   |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I BPNSY   | The following trace elements or packets are used to provide synchronization information in the different layers.                                                                                                                                                                                                                                            |

## Table D4-3 Control of each layer

| Layer           | Control                                    |
|-----------------|--------------------------------------------|
| Layer 3         | Context element and Target Address element |
| Layer 2         | Trace Info element                         |
| Layer 1         | Trace Info packet                          |
| Transport Layer | Alignment Synchronization packet           |

ISFXXD

Whenever a trace analyzer receives a Trace Info packet, the trace analyzer receives information about the current state of the trace. However, the trace analyzer cannot begin analysis of program execution until it knows the context in which instructions are being executed and it has an instruction address to start analysis from.

RPGHPW

RQZRMQ

RTTLJC

When a Trace Info element is generated, the trace unit generates a Context element and a Target Address element soon after the Trace Info element .

Note

There are common use cases where the ratio between the number of bytes associated with trace protocol synchronization and other trace bytes increases significantly, resulting in a degradation of the usability of the trace. Therefore Arm recommends that trace protocol synchronization only occurs when required.

## D4.3.2.1 Non-periodic trace protocol synchronization

When the trace unit becomes operative, non-periodic trace protocol synchronization occurs.

When non-periodic trace protocol synchronization occurs, the trace unit generates an Alignment Synchronization packet in the trace byte stream before any other trace packets are generated.

RHMDGL

When non-periodic trace protocol synchronization occurs, the trace unit generates a Trace Info element in the trace element stream before any other trace elements are generated, except Event elements and Instrumentation elements .

IMQNBT

Arm recommends that if a trace protocol synchronization request occurs while ViewInst() is inactive , the Alignment Synchronization packet is not output in the trace byte stream until just before any of the following:

- ViewInst() becomes active.

- An Event packet is output.

- An Instrumentation packet is output.

IMHGVF The generation of Instrumentation packets is independent of the ViewInst() function. Instrumentation packets can therefore be generated when ViewInst() indicates instruction tracing is inactive.

## D4.3.2.2 Periodic trace protocol synchronization

IYPRYM The trace unit can be programmed to generate trace protocol synchronization requests on a periodic basis, so that the trace element streams and the trace byte streams can be analyzed when stored in a circular trace buffer. TRCSYNCPR.PERIOD controls periodic trace protocol synchronization requests.

INTFYC Periodic trace protocol synchronization can also be requested by the trace capture infrastructure, for example if a trace protocol synchronization request is received on an Arm AMBA ATB interface. For more information on the Arm AMBAATBinterface, see the AMBA®ATBProtocol Specification (ARM IHI 0032) .

RQHHSY When periodic trace protocol synchronization is requested, either by TRCSYNCPR.PERIOD or by other sources, the trace unit performs periodic trace protocol synchronization.

RVMPYW When periodic trace protocol synchronization occurs, the trace unit generates an Alignment Synchronization packet. The trace unit then generates a Trace Info element to indicate a point where program execution trace analysis can start. A Trace Info element is not required if only Event elements and Instrumentation elements are output.

IQYQRY Arm recommends that an Alignment Synchronization packet is only output in the trace byte stream if other trace packets have been output since the previous Alignment Synchronization packet. This reduces the risk of a circular buffer filling and overwriting trace.

INQYXW

If two or more periodic trace protocol synchronization requests occur, and no trace is generated between these two requests, then Arm recommends that a non-periodic trace protocol synchronization occurs before any further trace is generated. This ensures that when tracing has been inactive for a long period of time, the trace stream is fully synchronized when tracing is re-activated.

## D4.3.2.3 Synchronization of instruction trace

RKKQGK When non-periodic trace protocol synchronization occurs, the trace unit generates a Context element and a Target Address element before any P0 elements are generated, to provide the trace analyzer with Context information and Address information .

RSVGNN

When periodic trace protocol synchronization occurs, and ViewInst() is active when the corresponding Trace Info element is generated, the trace unit generates a Context element and a Target Address element which provide the Context information and Address information for the target of the most recent non-canceled P0 elements .

Note

If the trace unit generates the Context element and Target Address element immediately after the Trace Info element , then the most recent non-canceled P0 elements might have occurred before the Trace Info element .

RDLPYX

Figure D4-5 Example of Target Address element after Trace Info element.

<!-- image -->

When periodic trace protocol synchronization occurs, and ViewInst() is inactive when the corresponding Trace Info element is generated, when ViewInst() becomes active and a Trace On element is generated, the trace unit generates a Context element and a Target Address element before any Atom elements , Qelements , or Exception elements are generated. This provides the trace analyzer with Context information and Address information .

Figure D4-6 Example of Target Address element after Trace Info element in a filtered region.

<!-- image -->

IYZPCB If a Cancel element cancels any P0 elements before a Trace Info element , then the trace analyzer discards all of the following:

- The canceled P0 elements .
- The Trace Info element .
- All elements after the Trace Info element , up to and including the Cancel element . This includes any Context elements or Target Address elements .

Note

In this scenario, information from the canceled Trace Info element can still be used.

Figure D4-7 Example of Target Address element after Trace Info element in a mispredicted region.

<!-- image -->

RKGPTB When a Cancel element is generated which cancels any P0 elements before a Trace Info element , the trace unit generates a new Context element and a new Target Address element , which indicate the target of the most recent P0

element that has not been canceled.

ICHTFM

The Target Address element and Context element might indicate the target of a P0 element from before the Trace Info element , or might be delayed until after the next P0 element , and therefore indicate the target of that P0 element .

Note

If the trace unit generates the new Context element and Target Address element prior to the next new P0 element , then this might prevent the indication of execution of some instructions before the Trace Info element .

INSWTK

If the Cancel element cancels all P0 elements after a Trace Info element , but no P0 elements prior to the Trace Info element , then it might be necessary for the trace unit to immediately generate a Context element and Target Address element . This is because a Context element and Target Address element might have been present in the trace element stream after the Trace Info element , and those Context element and Target Address element are now discarded.

## D4.3.3 Speculation in the trace element stream

INVBWS

IRTJNK

FEAT\_ETE supports the correction of trace. This might be because of:

- The tracing of speculative execution of instructions by a PE.
- For some implementations, the tracing of the Transactional Memory Extension.

AFEAT\_ETE trace unit traces speculatively-executed instructions in the same way as all other instructions, so that both speculatively-executed instructions and architecturally-executed instructions appear in the instruction trace element stream. This means that some of the program execution information that is shown in the trace element stream might be incorrect, because some of the speculatively executed instructions might be mis-speculated.

Note

The level of speculation that is revealed in the trace is IMPLEMENTATION SPECIFIC.

| I XLLKT   | The trace unit resolves this speculation by generating trace elements to confirm the status of each instruction in the instruction trace element stream. That is, the trace unit generates trace elements to show whether each instruction has been committed for execution, or canceled because of mis-speculation. This means that a trace analyzer does not know the status of a traced instruction until the trace analyzer receives a trace element that indicates whether the instruction has been committed for execution, or canceled because the instruction was mis-speculated.   |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R ZJJKY   | When speculatively-executed instructions are traced, the trace unit subsequently generates trace elements that indicate whether the instructions have been committed for execution, or have been canceled.                                                                                                                                                                                                                                                                                                                                                                                  |
| I KYXKZ   | Atrace analyzer takes the appropriate action, which might involve canceling some trace elements, to determine the actual program execution.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| I GGFML   | Trace elements that resolve the status of a traced instruction are called speculation resolution elements . For more information on speculation elements, see Speculation Resolution Elements.                                                                                                                                                                                                                                                                                                                                                                                              |
| R KYGRF   | When trace is generated for speculative execution, for mis-speculated execution, the trace unit does not trace any information that cannot be accessed by software executing at the same or at a lower level of privilege than the mis-speculated execution.                                                                                                                                                                                                                                                                                                                                |
| R QHQLY   | When a Context synchronization event is speculated as being taken or executed, the trace unit does not generate trace for any speculative execution after the Context synchronization event until the Context synchronization event is resolved.                                                                                                                                                                                                                                                                                                                                            |
| R LWJCQ   | When a speculated Context synchronization event is resolved as being not taken or not executed, the trace unit does not generate trace for mis-speculated execution that occurred after the Context synchronization event.                                                                                                                                                                                                                                                                                                                                                                  |
| R YGSGJ   | When an exit from a Trace Prohibited region is speculated as being taken, the trace unit does not generate trace for any speculative execution after the exit from the Trace Prohibited region, until the exit from the Trace Prohibited region is resolved.                                                                                                                                                                                                                                                                                                                                |
| R SRLCG   | When a speculated exit from a Trace Prohibited region is resolved as being not taken, the trace unit does not generate trace for mis-speculated execution that occurred after the exit from a Trace Prohibited region.                                                                                                                                                                                                                                                                                                                                                                      |
|           | D4.3.3.1 Tracing transactions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| I KBTHL   | The Transactional Memory Extension defines the Transactional state . For instructions executed in Transactional state, the trace stream indicates which instructions are executed in Transactional state, and provides indicators for a trace analyzer to determine whether the transaction was successful or failed.                                                                                                                                                                                                                                                                       |
| I FWGBM   | If the instruction is executed in Transactional state then the result of the instruction is not known until the transaction succeeds or fails. Transactions can be of an arbitrary length and can be nested, so the ETE architecture does not guarantee an entire transaction is traced, if any of the transactions is traced.                                                                                                                                                                                                                                                              |
| I VJTLG   | The execution of transactions is represented in the trace element stream by 3 elements: • Transaction Start element . • Transaction Commit element . • Transaction Failure element . These provide markers in the trace element stream to indicate the sections which represent transactions. The Transaction Start element indicates that any following instructions are executed in Transactional state. When the PE                                                                                                                                                                      |
| I QZNBZ   | An entry to Transactional state might be traced using a Transaction Start element and the subsequent exit from Transactional state might be traced, without tracing any execution in Transactional state. There might have been no execution in Transactional state, or the trace unit might have been programmed to not trace such execution.                                                                                                                                                                                                                                              |
| R VVFQZ   | D4.3.3.1.1 Implementation flexibility If no speculation in the trace element stream is implemented, TRCIDR8.MAXSPEC == 0x0 and TRCIDR0.COMMTRANS indicates that the Transaction Start element is a P0 element .                                                                                                                                                                                                                                                                                                                                                                             |

## D4.3.3.1.2 Filtering of trace

IZYNHF

The ETE architecture supports filtering of the trace within a transaction.

IBRWSS

Filtering of a transaction can be due to any of the following:

- The ViewInst function.

- Prohibited regions.

- Asynchronous events.

IZNYSY Due to filtering the start of the transaction might not necessarily be traced. See the Transaction Start element for details.

IVXTQS Due to filtering the end of a transaction might not necessarily be traced. See the Transaction Commit element and Transaction Failure element for details.

IPCSKD

If an instruction is traced which was executed in Transactional state, then the trace analyzer must be aware, so that the effect of the instructions executed in the Transactional state can be determined.

RNMWFJ When an instruction is traced and the PE is in Transactional state, the trace unit traces the result of the transaction unless

any of the following occur:

- The trace unit becomes disabled.

- Atrace unit buffer overflow occurs.

- The PE enters a Trace Prohibited region.

In the above scenarios, the trace unit generates a Transaction Failure element , and the resolution of the transaction is UNKNOWN.

## D4.3.4 Trace element stream

ILTBWR

ILBSZF

A Trace element stream is a sequence of elements which describe:

- The software control path of PE execution traced by the trace unit.
- Event-based trace.
- Temporal information.

ATrace Info element provides a point in the trace element stream where analysis of the trace element stream can begin. Trace Info elements include setup information about:

- The static trace programming that does not change during a trace session, including:
- -Whether cycle counting is enabled, and if enabled, the cycle count threshold.
- Dynamic information that might change during a trace session, such as:
- -The speculation depth. This indicates how many unresolved P0 elements were traced before the Trace Info element.
- -Whether the trace unit has traced that the PE is executing in Transactional state.

## D4.3.5 P0 element

| I LLDBJ   | P0 elements imply the execution of instructions.                                                                                                                     |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I XPZXL   | P0 elements are generated speculatively and must be either committed or canceled. For more information on speculation elements, see Speculation Resolution Elements. |
| R XVHWG   | P0 elements must be generated in sequential execution order.                                                                                                         |

IXPFJG

RPRNZH

ICYMYM

IYVMSC

RMKPFJ

## IJLZPY

RDXJBQ

RYPPRH

RPZRFL

## D4.3.5.1 Atom element

An Atom element implies that one or more instructions have been executed, up to and including the next P0 instruction . Only certain instructions generate an Atom element . See Instruction and exception classification for more information on these instructions.

The Atom element is one of the following types:

- E Atom.
- NAtom.

The meaning of the type of an

Atom element are represented as an E

Atom element depends on the instruction it is encoding. For example, branch instructions

if the branch was taken and an N

## D4.3.5.2 Exception element

An Exception element indicates a change in program flow which cannot be calculated by the analysis of the program image, or which is caused by an instruction which is not a P0 instruction . Such a change in program flow is described as an Exceptional occurrence.

An Exceptional occurrence consists of the following:

- PE Architectural exceptions.
- ETE defined exceptions.
- IMPLEMENTATION DEFINED exceptions.

Note

Transaction failure is not classified as an Exceptional occurrence, although it is traced using an Exception packet.

An Exception element indicates:

- That an Exceptional occurrence has occurred.
- The type of Exceptional occurrence.
- The virtual address where the Exceptional occurrence was taken from, also known as the preferred exception return address.

The instruction set for the preferred exception return address for an Exception element is one of the following:

- AArch64 A64.
- AArch32 A32.
- AArch32 T32.

An Exception element is a P0 element .

## D4.3.5.2.1 PE Architectural exceptions

The following exception types are used to indicate PE Architectural exceptions:

- IRQ.
- FIQ.
- Trap.
- Call.
- Inst fault.
- Data fault.
- Inst debug.
- Data debug.
- Alignment.
- System Error.
- Debug halt.

See Instruction and exception classification for information on the mapping between the PE Architectural exceptions and these exception types.

Atom element if not taken.

RSFYMW

Table D4-4 defines the preferred exception return address for each exception type for PE Architectural exceptions.

## Table D4-4 Preferred exception return address for PE Architectural exceptions

| Exception type   | Preferred exception return address                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IRQ              | Instruction after the last executed instruction                                                                                                                                                                                                                                                                                                                                                                                                                          |
| FIQ              | Instruction after the last executed instruction                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Trap             | For a trapped instruction or UNDEFINED instruction, the preferred exception return address is the address of the instruction. For a trapped exception, the preferred exception return address is the address of the instruction that caused the exception.                                                                                                                                                                                                               |
| Call             | Instruction after the call instruction                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Inst fault       | Instruction that caused the exception                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Data fault       | Instruction that caused the exception                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Inst debug       | Instruction that caused the exception                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Data debug       | Instruction that caused the exception                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Alignment        | Instruction that caused the alignment exception                                                                                                                                                                                                                                                                                                                                                                                                                          |
| System Error     | Instruction after the last executed instruction                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Debug halt       | The instruction after the last executed instruction, that is, the value loaded into the DLRregister.                                                                                                                                                                                                                                                                                                                                                                     |
| I GZKGC          | The nature of System Error means that execution might not complete up to the preferred exception return address, or it might perform some operations after the preferred exception return address. This behavior is IMPLEMENTATION DEFINED and might vary depending on the cause of the exception.                                                                                                                                                                       |
| R GFJZF          | When an imprecise System Error exception occurs, the preferred exception return address is the address stored in the relevant ELR when the exception is taken.                                                                                                                                                                                                                                                                                                           |
| S GKMTH          | When a System Error exception occurs, the trace analyzer must be aware that the preferred exception return address might not indicate the exact point at which program execution was interrupted. The trace analyzer should not rely on the preferred exception return address for inferring exactly which instructions were executed. This behavior only occurs for imprecise System Error exceptions.                                                                  |
| R LBLWT          | When an imprecise Debug halt exception occurs, the preferred exception return address is the address stored in DLRor DLR_EL0 when the exception is taken.                                                                                                                                                                                                                                                                                                                |
| S RDJXM          | When an imprecise Debug halt exception occurs, the trace analyzer must be aware that the preferred exception return address might not indicate the exact point at which program execution was interrupted. The trace analyzer should not rely on the preferred exception return address for inferring exactly which instructions were executed. An imprecise Debug halt exception can only occur under direct control of a debugger, usually by controlling EDRCR.CBRRQ. |
| R MZJTJ          | In addition to the Arm Architectural exceptions, the ETE specifies the following Exceptional occurrences that are traced using Exception elements : • PE Reset, which indicates that a PE Warm reset has occurred.                                                                                                                                                                                                                                                       |
| R NRJGC          | Table D4-5 defines the preferred exception return address for each exception type for ETE defined exceptions.                                                                                                                                                                                                                                                                                                                                                            |

## Table D4-5 Preferred exception return address for ETE defined exceptions

| Exception type   | Preferred exception return address                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PE Reset         | UNKNOWN                                                                                                                                                                                                                                                                                                                                                                                                                                |
| I QJYYZ          | When an Exception element indicating a PE Reset occurs: • The target address and target context of the previous P0 element might be UNKNOWN. • If there are no P0 elements between a Trace On element and the Exception element , then the initial address and context after the previous Trace On element might be UNKNOWN.                                                                                                           |
| I XHFLL          | • Generic replay of program execution. The use of the IMPLEMENTATION DEFINED exceptions is optional and IMPLEMENTATION DEFINED. IMPLEMENTATION exceptions are not required to be traced but are intended to be used to simplify tracing of certain micro-architectural situations.                                                                                                                                                     |
| I DFLDJ          | DEFINED In general, the preferred exception return address is the address of the instruction after the last executed instruction,                                                                                                                                                                                                                                                                                                      |
|                  | before the exception occurs. D4.3.5.3 Source Address element                                                                                                                                                                                                                                                                                                                                                                           |
| I DJTGL          | The Source Address element indicates execution up to and including a provided P0 instruction address, and indicates the P0 instruction is taken. All P0 instructions except the final P0 instruction are not taken, which means that explicit N Atom elements are not required to be traced for those P0 instructions . A Source Address element indicates both of the following for the final P0 instruction : • The instruction set. |
| R HVVRK          | The instruction set for a Source Address element is one of the following: • AArch64 A64.                                                                                                                                                                                                                                                                                                                                               |
| R WTRBB R JRFYT  | A Source Address element is a P0 element . D4.3.5.4 Q element A Qelement belongs to the P0 element group in the instruction trace element stream, and must be explicitly resolved or                                                                                                                                                                                                                                                   |
| I XPNWS          | A Qelement can optionally include a number, M. The number is a count of the instructions that are executed since the most recent P0 element , which might be a Qelement . If it does not include a count of instructions, then the number of instructions that are executed since the most recent P0 element is UNKNOWN.                                                                                                               |
| R XWBMW          | The trace unit generates Qelements in the program order in which they occur, and the trace protocol encode and decode process maintains this order.                                                                                                                                                                                                                                                                                    |
| R JBYXC          | A Qelement does not imply Exceptional occurrences.                                                                                                                                                                                                                                                                                                                                                                                     |
| R                | When a Qelement implies an Exception return instruction which is taken, that instruction is the last instruction that is implied by the Qelement .                                                                                                                                                                                                                                                                                     |
| KPNGG            |                                                                                                                                                                                                                                                                                                                                                                                                                                        |

| R YRLJR   | When a Qelement implies an executed ISB instruction, this is the last instruction implied by the Qelement if execution continues from a new context after the ISB .                                                                                                                                               |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R LZLDH   | When execution continues from a new context after a Qelement is generated, the trace unit generates a Context element after the Qelement .                                                                                                                                                                        |
| I BTNZC   | The Context element might be generated before or after the Target Address element that is also required after the Q element .                                                                                                                                                                                     |
|           | If a context change occurs at a point that is not a Context synchronization event, then the last instruction that is implied by a Qelement must be the last instruction that is executed with the old context. The trace unit can then generate a Context element after the Qelement to indicate the new context. |
|           | D4.3.5.5 Transaction Start Element                                                                                                                                                                                                                                                                                |
| R CTLXL   | TRCIDR0.COMMTRANS indicates whether the Transaction Start element is a P0 element . See Transaction Start element for more information about the Transaction Start element .                                                                                                                                      |

## D4.3.6 Virtual Address Space Element

## D4.3.6.1 Trace On element

A Trace On element indicates a discontinuity in the trace element stream. The trace unit inserts a Trace On element after a gap in the generation of the trace element stream:

- When the trace generation becomes operative and before any P0 elements .
- If some instructions are filtered out of the trace.
- The first traced instructions after:
- -ATrace Prohibited region.
- -The PE leaves Debug state.
- When instruction trace is lost because a trace unit buffer overflow occurs.

RKMFKP When a Trace On element is generated, the trace unit generates a Target Address element before the next P0 element .

RTJLYH

When a Trace On element is generated, the trace unit generates a Context element before the next Atom element , Exception element or Qelement , to indicate where tracing starts, unless the context has not changed since the previous Context element was output.

RJKFBS

RQWBLT

RJYKHH

RHMWHY

IXCKNM

When the first

.

P0 element

## D4.3.6.2 Target Address element

A Target Address element indicates both of the following for the next instruction to be executed:

- The instruction set.
- The virtual address of the instruction.

The instruction set for a Target Address element is one of the following:

- AArch64 A64.
- AArch32 A32.
- AArch32 T32.

The trace unit generates Target Address elements in program order relative to other P0 elements .

Target Address element values can be corrected by another Target Address element if both Target Address elements are generated before the next P0 element or Trace On element .

Trace On element is generated, the trace unit outputs the corresponding

Context element before the first

RNHDCF

ILKDJM

IBLBJX

RBRJJF

IVTLTF

IYQJDR

## D4.3.6.3 Context element

IKQKFF

The Context element indicates the execution context for the next instruction to be executed.

RVHQYV

The Context element provides the following Context information :

- The Security state.

- The Exception level.

- The Execution state of the PE.

RWSVRL

The Context element can optionally provide the following Context information :

- The Context identifier.

- The Virtual context identifier.

RWJDWF

The trace unit generates Context elements in program order relative to P0 elements .

## D4.3.7 Temporal elements

IHHXND

Temporal elements provide information about the passage of time within the trace element stream. The following temporal elements are supported by ETE:

## The Cycle Count element

Indicates the passage of PE clock cycles within the trace element stream.

## The Timestamp element

Indicates the passage of time within the trace element stream.

## The Timestamp Marker element

Indicates that the most recent P0 element , Event element , Instrumentation element has been timestamped and that a subsequent Timestamp element contains the timestamp value.

## D4.3.7.1 Cycle Count element

| I NVGJP   | Each Cycle Count element is associated with a Commit element , and when a Commit element is generated, a Cycle Count element might also be generated.        |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R BZQWX   | Each Cycle Count element is associated with the most recent Commit element .                                                                                 |
| R VZXNN   | A Cycle Count element indicates the number of PE clock cycles between the two most recent Commit elements that both have an associated Cycle Count element . |
| I FHGKM   | Not every Commit element is required to have an associated Cycle Count element .                                                                             |
| R VNYMN   | Cycle Count elements are generated in order relative to Commit elements .                                                                                    |

## D4.3.7.2 Timestamp element

The Timestamp element inserts a global timestamp value into the trace element stream.

The source for timestamp reported in the timestamp element is controlled by:

- TRFCR\_EL1.TS.
- TRFCR\_EL2.TS.

Atimestamp value of zero indicates that the timestamp value is UNKNOWN.

An UNKNOWN timestamp value might occur if the system does not support timestamping or if the timestamp is temporarily unavailable.

The source for the payload of Timestamp elements is controlled by the TRFCR registers and the virtual timers. It is expected that these registers will be changed by context switch software. As a result it is possible that payloads of Timestamp elements might appear to have discontinuities, and even go backwards, if the source of the timestamp changes, or any context switching changes the System registers which control the timestamp value.

| R MCSGX         | If FEAT_ETEv1p1 is implemented, then when there has been a Timestamp Marker element before the Timestamp element , the Timestamp element contains the timestamp value of the most recent of the following before the Timestamp Marker element :                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R DGTJZ         | If FEAT_ETEv1p1 is not implemented or if there has not been a Timestamp Marker element before the Timestamp element , the Timestamp element contains the timestamp value of the most recent of the following before the Timestamp element : • P0 element. • Event element. • Instrumentation element. If TRCIDR0.TSMARK is 1 and there is no previous Timestamp Marker element , the Timestamp element is for a P0                                                                                                                                                                                                                                                                              |
| I PXZVX         | element , Event element , or Instrumentation element which is before the start of the trace. This scenario might occur when trace analysis starts at a Trace Info element which is not the first Trace Info element , and the Timestamp Marker element was generated before the Trace Info element .                                                                                                                                                                                                                                                                                                                                                                                            |
| I CSZYW         | The requirement for a Timestamp Marker element for every Timestamp element is to avoid needing to indicate if there has been a Timestamp Marker element at a Trace Info point. This allows a trace analyzer to assume there is a Timestamp Marker element (or not) before the Trace Info, based on a static piece of information.                                                                                                                                                                                                                                                                                                                                                               |
|                 | The Timestamp Marker element indicates the most recent P0 element , Event element , or Instrumentation element has been timestamped, and that a Timestamp element will follow containing the timestamp value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| R RFYPT         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| R SZRHP         | Timestamp Marker element s are generated in order with respect to P0 element s, Event element s, and Instrumentation element .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| R DCRVK         | Timestamp Marker element s are not canceled by Cancel elements .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| I DLCLX R VWJVC | A Cancel element might cause a P0 element to be canceled and if there is a Timestamp Marker element that is associated with that P0 element then the Timestamp Marker element is not associated with any P0 element . The Timestamp element which is associated with the Timestamp Marker element is unaffected, and is still usable for timestamping the approximate position in the trace stream. If 2 Timestamp Marker element s occur without a Timestamp element between them, the oldest Timestamp Marker element is ignored. If an Overflow element or Discard element occurs after a Timestamp Marker element and before a Timestamp element , the Timestamp Marker element is ignored. |
| R               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| JNWJY           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| R               | Timestamp Marker element s are generated by the trace unit, every Timestamp element must have a Marker element generated before the Timestamp element .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| LWZXK           | If corresponding Timestamp                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| I JGKZJ         | The generation of Timestamp Marker element s is indicated in TRCIDR0.TSMARK.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## D4.3.8 Speculation Resolution Elements

IYYMXT

The ETE architecture allows trace to be generated speculatively and then later committed or removed by the decompression process. Each P0 element is traced and is considered speculative until either committed by a Commit element or canceled by a Cancel element . This method of generating speculative trace allows for the tracing of speculative execution, including the tracing of transactions when the Transactional Memory Extension is implemented in the PE.

ISRRZZ

Speculation resolution elements provide a trace analyzer with information about which trace elements were correctly or incorrectly generated, and ensure the trace analyzer can reconstruct the program execution. The following speculation resolution elements are supported by ETE:

## The Mispredict element

Corrects the most recent Atom element .

## The Cancel element

Indicates that one or more P0 elements are canceled.

## The Commit element

Indicates that one or more P0 elements are resolved for execution.

## The Discard element

Removes all speculative P0 elements .

IXLHWT TRCIDR8.MAXSPEC specifies the maximum number of uncommitted P0 elements which can be discarded at a later stage using Cancel elements .

## D4.3.8.1 Commit element

IKQQML A Commit element indicates that a number of unresolved P0 elements have been resolved for execution. The resolved P0 elements are the oldest P0 elements .

RPNBGQ

The Commit element resolves all types of P0 element

.

IKHYLN

Commit elements might be merged if the total number of P0 elements resolved is less than TRCIDR8.MAXSPEC. Commit elements are merged by adding their respective commit count values together.

Figure D4-8 shows an example operation for a Commit element :

Figure D4-8 Commit Operation Example

<!-- image -->

## D4.3.8.2 Cancel element

IMRGLC

The Cancel element indicates the number of youngest unresolved and uncanceled P0 elements that are canceled from execution. A trace unit might cancel elements because of many reasons, including but not limited to:

- A P0 instruction is mis-speculated.

- An exception occurs.

RWLTNX

The Cancel element cancels all types of P0 element .

INDQKN

Cancel elements might be merged if no P0 elements have been generated in between. Cancel elements are merged by adding their respective cancel numbers together.

Figure D4-9 shows an example operation for a Cancel element :

## D4.3.8.3 Discard element

ITCWCN

A Discard element is generated if uncommitted P0 elements remain when trace generation becomes inoperative or if the resolution of uncommitted P0 elements cannot be output by the trace unit.

ISTXQZ

If trace generation remains inoperative, the outcomes of instructions that are traced by P0 elements , such as conditional P0 instructions , cannot be resolved, and therefore a Discard element indicates that all uncommitted P0 elements must be discarded.

## D4.3.8.4 Mispredict element

IGBKKQ

The Mispredict element indicates that the most recent non-canceled Atom element has the incorrect E or N status.

IRGVGL

For example, if a branch instruction is predicted as taken, it is traced with an E Atom element . If the prediction becomes incorrect, then a Mispredict element is traced to indicate to a trace analyzer that the E Atom element changes to an N Atom element .

## D4.3.9 Instrumentation element

| I ZLFFN   | The Instrumentation element indicates execution of a TRCIT instruction.                                                                                                                                                                                                                            |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R BXTXK   | If Instrumentation tracing is prohibited, then no trace is generated by the TRCIT instruction, and TRCIT behaves as a NOP .                                                                                                                                                                        |
| R JJZXW   | If tracing is prohibited, then no ETE trace is generated by the TRCIT instruction, and TRCIT behaves as a NOP . TraceAllowed() defines when tracing is prohibited.                                                                                                                                 |
| R BWHCS   | If Instrumentation tracing is not prohibited and tracing is enabled and not prohibited, then execution of the TRCIT instruction requests an Instrumentation element to be generated in the ETE trace stream. TraceInstrumentationAllowed() defines when Instrumentation tracing is not prohibited. |
| R NHJLQ   | When an Instrumentation element is requested, the Instrumentation element is generated if and only if the TRCIT instruction is architecturally executed.                                                                                                                                           |
| R VPFGH   | If the Instrumentation element cannot be generated when required, then a trace unit buffer overflow occurs.                                                                                                                                                                                        |
| R CJRNL   | Instrumentation elements are not discarded by Cancel elements.                                                                                                                                                                                                                                     |

Figure D4-9 Cancel Operation Example

<!-- image -->

## D4.3.10 Other elements

## D4.3.10.1 Event element

| I RBKYZ   | The Event element indicates when a programmed ETEEvent occurs and its payload contains a number to identify the ETEEvent number. See TRCEVENTCTL0R, and TRCEVENTCTL1R, for information about the programming of arbitrary ETEEvents .   |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R SMLVB   | Event elements maintain order relative to other Event elements .                                                                                                                                                                        |
|           | D4.3.10.2 Overflow element                                                                                                                                                                                                              |
| I RFQKZ   | The Overflow element indicates that the trace unit buffer has overflowed, and at least one trace element might have been lost.                                                                                                          |

## D4.3.11 Transactional Memory

| R LLCQG   | The TSTART instruction is a P0 instruction .                                                                                                                                                                                                                                                                                                                |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I QNFVH   | The Transaction Start element indicates that subsequent elements are within a transaction, until any of the following are traced:                                                                                                                                                                                                                           |
| R KMNXW   | When the PE enters Transactional state, a Transaction Start element is generated before any instructions are traced. This indicates to the trace analyzer that subsequent elements have been executed in Transactional state.                                                                                                                               |
| R MMCQD   | Only a single Transaction Start element is generated for each outer transaction, unless the trace unit indicated the transaction had finished by generating a Transaction Failure element .                                                                                                                                                                 |
| I MQZZY   | An example of when the trace unit generates a Transaction Failure element without the PE leaving Transactional state is when a trace unit buffer overflow occurs. In this example, tracing might resume after the trace unit buffer overflow, and if the PE is still in the same outer transaction then a new Transaction Start element would be generated. |
| R DPNGP   | The Transaction Start element appears in program order relative to other P0 elements .                                                                                                                                                                                                                                                                      |
| R CYHKB   | When a TSTART instruction for an outer transaction is traced and tracing continues in Transactional state, the trace unit generates a Transaction Start element after the P0 element that is generated by the TSTART instruction, and before any subsequent P0 element .                                                                                    |
| R RKGLY   | When a TSTART instruction for an outer transaction is not traced and tracing becomes active while the PE is in Transactional state, the trace unit generates a Transaction Start element after the Trace On element and before any P0 elements .                                                                                                            |
| I XTXHN   | D4.3.11.2 Transaction Commit element The Transaction Commit element indicates that the PE has exited Transactional state, that the transaction has completed                                                                                                                                                                                                |
| I XHLPG   | D4.3.11.3 Transaction Failure element The Transaction Failure element indicates that the transaction did not complete successfully and the trace analyzer discards all the execution since the most recent Transaction Start element , including any P0 elements which have been committed by Commit elements .                                             |
| I HLQGS   | Asophisticated trace analyzer might be able to use the discarded elements to create a heuristic on why the transaction failed.                                                                                                                                                                                                                              |