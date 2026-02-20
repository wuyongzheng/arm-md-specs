## G1.21 Advanced SIMD and floating-point support

Advanced SIMD and floating-point instructions introduces:

- The scalar floating-point instructions in the T32 and A32 instruction sets.
- The Advanced SIMD integer and floating-point vector instructions in the T32 and A32 instruction sets.
- The SIMD and floating-point register file, which can be viewed as:
- -Singleword registers S0 - S31.
- -Doubleword registers D0 - D31.
- -Quadword registers Q0 - Q15.
- The Floating-Point Status and Control Register (FPSCR).
- Floating-point exceptions and exception traps.

For more information about the System registers for the Advanced SIMD and floating-point operation, see Advanced SIMD and floating-point System registers. Software can interrogate these registers to discover the implemented Advanced SIMD and floating-point support.

AArch32 implications of not including support for Advanced SIMD and floating-point summarizes the effects of not supporting these instructions, and the following subsections give more information about the Advanced SIMD and Floating-point support:

- Enabling Advanced SIMD and floating-point support.
- Advanced SIMD and floating-point System registers.
- Context switching when using Advanced SIMD and floating-point functionality.

## G1.21.1 AArch32 implications of not including support for Advanced SIMD and floating-point

The architecture generally requires the inclusion of the Advanced SIMD and floating-point instructions in all instruction sets. However, for implementations targeting specialized markets, Arm might produce or license implementations that do not provide any support for Advanced SIMD and floating-point instructions. In such an implementation, in AArch32 state:

- The CPACR.{ASEDIS, cp11, cp10} fields are RES0.
- The NSACR.{NSASEDIS, cp11, cp10} fields are RES0.
- The HCPTR.{TASE, TCP11, TCP10} fields are RES1.
- The FPEXC, FPSCR, FPSID, MVFR0, MVFR1, and MVFR2 registers are not implemented and their encodings are UNDEFINED.
- Attempted accesses to Advanced SIMD and floating-point functionality are UNDEFINED. This means:
- -All Advanced SIMD and floating-point instructions are UNDEFINED.
- -Attempts to access the Advanced SIMD and floating-point System registers are UNDEFINED.

## G1.21.2 Enabling Advanced SIMD and floating-point support

Software must ensure that the required access to the Advanced SIMD and floating-point features is enabled. Most of those controls are described in Configurable instruction controls, and this section:

- Summarizes those controls.
- Provides additional information in the following subsections:
- -FPEXC control of access to Advanced SIMD and floating-point functionality.
- -EL0 access to Advanced SIMD and floating-point functionality.

Note

This section shows the controls when the controlling Exception levels are using AArch32. Similar controls are provided when the Exception levels are using AArch64, and then apply to lower Exception levels that are using AArch32.

The controls of access to Advanced SIMD and floating-point functionality are:

## General {cp10, cp11} or {TCP10, TCP11} controls

This relates to the CPACR.{cp10, cp11}, NSACR.{cp10, cp11}, and HCPTR.{TCP10, TCP11} controls.

Note

Background to the System register interface explains the naming of these controls.

The {cp10, cp11} controls provide general control of the use of Advanced SIMD and floating-point functionality, as follows:

- CPACR.{cp10, cp11} control access from PE modes other than Hyp mode. These fields have no effect on accesses to Advanced SIMD and floating-point functionality from Hyp mode.
- In an implementation that includes EL3, NSACR.{cp10, cp11} control access from Non-secure state.
- In an implementation that includes EL2, if NSACR.{cp10, cp11} permit Non-secure accesses, or if EL3 is not implemented, HCPTR.{TCP10, TCP11} provide an additional control on those accesses.

In each case, the {cp10, cp11} controls must be programmed to the same value, otherwise operation is CONSTRAINED UNPREDICTABLE. The CONSTRAINED UNPREDICTABLE behavior is that, for all purposes other than reading the value of the register field, behavior is as if the cp11 field has the same value as the cp10 field. For more information, see Handling of System register control fields for Advanced SIMD and floating-point operation.

For more information about these controls, see:

- FPEXC.
- CPACR.
- HCPTR.
- NSACR.

## Control of accesses to the CPACR from Non-secure PL1 modes

As stated in General {cp10, cp11} or {TCP10, TCP11} controls, the CPACR controls access to Advanced SIMD and floating-point functionality from PE modes other than Hyp mode. Accesses to the CPACR from Non-secure PL1 modes can be trapped to EL2.

## Additional controls of Advanced SIMD functionality

- If implemented as an RW field, CPACR.ASEDIS can make all Advanced SIMD instructions UNDEFINED in all modes other than Hyp mode.
- In an implementation that includes EL3, when CPACR.ASEDIS permits use of the Advanced SIMD instructions or if the CPACR.ASEDIS control is not implemented, NSACR.NSASEDIS can make all Advanced SIMD instructions UNDEFINED in Non-secure state.
- In an implementation that includes EL2, when the CPACR and NSACR settings permit Non-secure use of the Advanced SIMD instructions, if HCPTR.TASE is implemented as an RWfield it can make these instructions UNDEFINED in Hyp mode, and trap to Hyp mode any use of these instructions in a Non-secure PL0 or PL1 mode.

Pseudocode description of enabling SIMD and floating-point functionality provides links to the pseudocode descriptions of all of these controls.

## G1.21.2.1 FPEXC control of access to Advanced SIMD and floating-point functionality

In addition, FPEXC.EN is an enable bit for most Advanced SIMD and floating-point operations. When FPEXC.EN is 0, all Advanced SIMD and floating-point instructions are treated as UNDEFINED except for:

- A VMSR to the FPEXC or FPSID register.
- A VMRS from the FPEXC, FPSID, MVFR0, MVFR1, or MVFR2 register.

These instructions can be executed only at EL1 or higher.

Note

- When the FPSID is accessible, any write access to the FPSID is ignored.

- When FPEXC.EN is 0, these operations are treated as UNDEFINED :

- A VMSR to the FPSCR.

- A VMRS from the FPSCR.

When executing at EL0, the PE behaves as if the value of FPEXC.EN is 1 if either:

- EL1 is using AArch64.
- EL2 is enabled in the current Security state and is using AArch64. and the value of HCR\_EL2.TGE is 1.

Note

In Non-secure state, if the value of HCR\_EL2.RW is 0 then it is permitted for the value of FPEXC32\_EL2.EN to control whether Advanced SIMD and floating-point functionality is enabled. However, Arm deprecates using the value of FPEXC32\_EL2.EN to determine behavior.

## G1.21.2.2 EL0 access to Advanced SIMD and floating-point functionality

When the access controls summarized in this section permit EL0 access to the Advanced SIMD and floating-point functionality, this applies only to the subset of functionality that is available at EL0. In particular:

- Only Advanced SIMD and Floating-point System register that is accessible is the FPSCR.
- The Advanced SIMD and floating-point instructions are available.

Execution at EL0 corresponds to the application level view of the Advanced SIMD and floating-point functionality, as described in Advanced SIMD and floating-point System registers.

## G1.21.3 Advanced SIMD and floating-point System registers

AArch32 state provides a common set of System registers for the Advanced SIMD and floating-point functionality. This section gives general information about this set of registers, and indicates where each register is described in detail. It contains the following subsections:

- Register map of the Advanced SIMD and floating-point System registers.
- Accessing the Advanced SIMD and floating-point System registers.

## G1.21.3.1 Register map of the Advanced SIMD and floating-point System registers

Table G1-21 shows the register map of the Advanced SIMD and Floating-point registers. Each register is 32 bits wide.

## Table G1-21 Floating-point registers

| Name   | Permitted access   |
|--------|--------------------|
| FPEXC  | RW                 |
| FPSCR  | RW                 |
| FPSID  | RW a               |

| Name   | Permitted access   |
|--------|--------------------|
| MVFR0  | RO                 |
| MVFR1  | RO                 |
| MVFR2  | RO                 |

In an implementation that includes EL3, the Advanced SIMD and Floating-point registers are common registers, see Common System registers.

## G1.21.3.2 Accessing the Advanced SIMD and floating-point System registers

Software accesses the Advanced SIMD and floating-point System registers using the VMRS and VMSR instructions, see:

- VMRS.
- VMSR.

## For example:

```
VMRS <Rt>, FPSID ; Read Floating-Point System ID Register VMRS <Rt>, MVFR1 ; Read Media and VFP Feature Register 1 VMSR FPSCR, <Rt> ; Write Floating-Point System
```

```
Control Register
```

Software can access the Advanced SIMD and floating-point System registers only if the access controls permit the access, see Enabling Advanced SIMD and floating-point support.

Note

All hardware ID information can be accessed only from EL1 or higher. This means:

## The FPSID is accessible only from EL1 or higher.

This is a change introduced from VFPv3. Previously, the FPSID register can be accessed in all modes.

## The MVFR registers are accessible only from EL1 or higher.

Unprivileged software must issue a system call to determine what features are supported.

## G1.21.4 Context switching when using Advanced SIMD and floating-point functionality

When the Advanced SIMD and floating-point functionality is used by only a subset of processes, the operating system might implement lazy context switching of the Advanced SIMD and floating-point register file and System registers.

In the simplest lazy context switch implementation, the primary context switch software uses the CPACR.{cp10, cp11} controls to disable access to the Advanced SIMD and floating-point functionality, see Enabling Advanced SIMD and floating-point support. Subsequently, when a process or thread attempts to use an Advanced SIMD or floating-point instruction, it triggers an Undefined Instruction exception. The operating system responds by saving and restoring the Advanced SIMD and floating-point register file and System registers. Typically, it then re-executes the Advanced SIMD or floating-point instruction that generated the Undefined Instruction exception.