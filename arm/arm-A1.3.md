## A1.3 Arm architectural concepts

This section introduces architectural concepts and the associated terminology.

The following subsections describe key architectural concepts. Each section introduces the corresponding terms that are used to describe the architecture:

- Execution state.
- The instruction sets.
- System registers.
- Arm Debug.

## A1.3.1 Execution state

The Execution state defines the PE execution environment, including:

- The supported register widths.
- The supported instruction sets.
- Significant aspects of:
- -The Exception model.
- -The Virtual Memory System Architecture (VMSA).
- -The programmers' model.

The Execution states are:

- AArch64 The 64-bit Execution state. This Execution state:
- Provides 31 64-bit general-purpose registers, of which X30 is used as the procedure link register.
- Provides a 64-bit Program Counter (PC), stack pointers (SPs), and Exception Link Registers (ELRs).
- Provides 32 128-bit registers for Advanced SIMD vector and scalar floating-point support.
- Provides a single instruction set, A64. For more information, see The instruction sets.
- Defines the Armv8 Exception model, with up to four Exception levels, EL0 - EL3, that provide an execution privilege hierarchy, see Exception levels.
- Provides support for 64-bit virtual addressing . For more information, including the limits on address ranges, see The AArch64 Virtual Memory System Architecture.
- Defines a number of Process state (PSTATE) elements that hold PE state. The A64 instruction set includes instructions that operate directly on various PSTATE elements.
- Names each System register using a suffix that indicates the lowest Exception level at which the register can be accessed.
- AArch32 The 32-bit Execution state. This Execution state:
- Provides 13 32-bit general-purpose registers, and a 32-bit PC, SP, and Link Register (LR). The LR is used as both an ELR and a procedure link register. Some of these registers have multiple banked instances for use in different PE modes .
- Provides a single ELR, for exception returns from Hyp mode.
- Provides 32 64-bit registers for Advanced SIMD vector and scalar floating-point support.
- Provides two instruction sets, T32 and A32. For more information, see The instruction sets.
- Supports the Armv7-A Exception model, based on PE modes , and maps this onto the Armv8 Exception model, that is based on the Exception levels.
- Provides support for 32-bit virtual addressing.
- Defines a number of Process state (PSTATE) elements that hold PE state. The T32 and A32 instruction sets include instructions that operate directly on various PSTATE elements, and instructions that access PSTATE by using the Application Program Status Register (APSR) or the Current Program Status Register (CPSR).

Later subsections give more information about the different properties of the Execution states.

Transferring control between the AArch64 and AArch32 Execution states is known as interprocessing . The PE can move between Execution states only on a change of Exception level, and subject to the rules given in Interprocessing. This means different software layers, such as an application, an operating system kernel, and a hypervisor, executing at different Exception levels, can execute in different Execution states.

## A1.3.2 The instruction sets

The possible instruction sets depend on the Execution state:

| AArch64   | AArch64 state supports a single instruction set, called A64. This is a fixed-length instruction set that uses 32-bit instruction encodings. For information on the A64 instruction set, see A64 Instruction Set Overview. If FEAT_SVE is implemented, the A64 instruction set supports scalable vector instructions. See About the SVE instructions. If FEAT_SME is implemented, the A64 instruction set supports scalable matrix instructions. See About the SMEinstructions.   |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AArch32   | AArch32 state supports the following instruction sets: A32 This is a fixed-length instruction set that uses 32-bit instruction encodings.                                                                                                                                                                                                                                                                                                                                        |

The instruction sets support SIMD and scalar floating-point instructions. See Floating-point support.

## A1.3.3 System registers

System registers provide control and status information of architected features.

The System registers use a standard naming format: &lt;register\_name&gt;.&lt;bit\_field\_name&gt; to identify specific registers as well as control and status bits within a register.

Bits can also be described by their numerical position in the form &lt;register\_name&gt;[x:y] or the generic form bits[x:y].

In addition, in AArch64 state, most register names include the lowest Exception level that can access the register as a suffix to the register name:

- &lt;register\_name&gt;\_ELx, where x is 0, 1, 2, or 3.

For information about Exception levels, see Exception levels.

The System registers comprise:

- The following registers that are described in this Manual:
- -General system control registers.
- -Debug registers.
- -RAS registers.
- -Generic Timer registers.
- -Optionally, Performance Monitor registers.
- -Optionally, the Activity Monitors registers.
- -Optionally, the Scalable Vector Extension registers.

- -Optionally, in Armv9, Trace System registers.
- Optionally, one or more of the following groups of registers that are defined in other Arm architecture specifications:
- -Trace System registers, as defined in the Arm ® Embedded Trace Macrocell Architecture Specification, ETMv4 .
- -Generic Interrupt Controller (GIC) System registers, see The Arm Generic Interrupt Controller System registers.

For information about the AArch64 System registers, see AArch64 System Register Descriptions.

For information about the AArch32 System registers, see AArch32 System Register Descriptions.

## A1.3.3.1 The Arm Generic Interrupt Controller System registers

From version 3 of the Arm Generic Interrupt Controller architecture, GICv3, the GIC architecture specification defines a System register interface to some of its functionality. The System register summaries in this Manual include these registers, see:

- About the GIC System registers, for more information about the AArch64 GIC System registers.
- About the GIC System registers, for more information about the AArch32 GIC System registers.

These sections give only short overviews of the GIC System registers. For more information, including descriptions of the registers, see the ARM ® Generic Interrupt Controller Architecture Specification, GIC architecture version 3 and version 4 (ARM IHI 0069).

Note

The programmers' model for earlier versions of the GIC architecture is wholly memory-mapped.

## A1.3.4 Arm Debug

Armv8 and later architectures support the following:

## Self-hosted debug

In this model, the PE generates debug exceptions . Debug exceptions are part of the Armv8 Exception model.

## External debug

In this model, debug events cause the PE to enter Debug state . In Debug state, the PE is controlled by an external debugger.

All Armv8 and later implementations support both models. The model chosen by a particular user depends on the debug requirements during different stages of the design and development life cycle of the product. For example, external debug might be used during debugging of the hardware implementation and OS bring-up, and self-hosted debug might be used during application development.

For more information about self-hosted debug:

- In AArch64 state, see AArch64 Self-hosted Debug.
- In AArch32 state, see AArch32 Self-hosted Debug.

For more information about external debug, see External Debug.