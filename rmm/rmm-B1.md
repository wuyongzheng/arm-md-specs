## Chapter B1 Commands

This chapter describes how RMM commands are defined in this specification.

## B1.1 Overview

RVZRKZ

The RMM exposes the following interfaces to the Host:

- The Realm Management Interface (RMI)
- RNPLKX The RMM exposes the following interfaces to a Realm:
- The Realm Services Interface (RSI)
- The Power State Coordination Interface (PSCI)

Any other SMC executed by a Realm returns SMCCC\_NOT\_SUPPORTED.

- ITKQXF An RMM interface consists of a set of RMM commands.
- IRTRYT An RMM interface is compliant with the SMC Calling Convention (SMCCC).
- RNNFPH SMCCC version &gt;= 1.2 is required.
- XFDXJG SMCCC version 1.2 increases the number of SMC64 arguments and return values from 4 to 17. Some RMM commands use more than 4 input or output values.
- RVXJJQ On a CCA platform which implements FEAT\_SVE, SMCCC version &gt;= 1.3 is required.
- XKCMSY SMCCC version 1.3 introduces a bit in the FID which a caller can use to indicate that SVE state does not need to be preserved across the SMC call.

RJNVJQ On a CCA platform which implements FEAT\_SME, SMCCC version &gt;= 1.4 is required.

- XQXMZL SMCCC version 1.4 adds support for preservation of SME state across an SMC call.
- RKWMVX An RMM command uses the SMC64 calling convention.
- SDFNMZ To determine whether an RMM interface is implemented, software should use the following flow:
1. Determine whether the SMCCC\_VERSION command is implemented, following the procedure described in Arm SMC Calling Convention [13].
2. Check that the SMCCC version is &gt;= 1.1.
3. Execute the &lt;Interface&gt;.Version command, which returns:
- SMCCC\_NOT\_SUPPORTED (-1) if &lt;Interface&gt; is not implemented.
- A version number (&gt;0) if &lt;Interface&gt; is implemented.
- RYBXKR All data types defined in this specification are little-endian.

See also:

- Chapter B4 Realm Management Interface
- Chapter B5 Realm Services Interface
- Chapter B6 Power State Control Interface

## B1.2 Command definition

IWBMVP The definition of an RMM command consists of:

- A function identifier (FID)
- A set of input values (referred to as 'arguments' in SMCCC)
- A set of output values (referred to as 'results' in SMCCC)
- A set of context values
- A partially-ordered set of failure conditions
- A set of success conditions
- A set of footprint items

IGCVWC Each failure condition, success condition and footprint item has an associated identifier. Identifiers are unique within each of the above groups, within each command.

An identifier has no meaning. It is only a label by which a given condition or footprint item can be referred to.

RSTJHR On calling an RMI or RSI command, any of X1 - X16 which are not specified as input values in the command definition SBZ.

RKBWJD On return from an RMI or RSI command, any of X0 - X16 which are not specified as output values in the command definition MBZ.

See also:

- SMCCC Arm SMC Calling Convention [13]

## B1.2.1 Example command

- INFVGF The following command, EXAMPLE\_ADD, is an example of how the components of an RMM command definition are presented in this document.

This command takes as an input value the address params\_ptr of an NS Granule which contains two integer values x and y . On successful execution of the command:

- The output value sum contains the sum of x and y
- The output value zero indicates whether either of x or y is zero

EXAMPLE\_ADD is defined as follows:

Interface

FID

0x042

Input values

| Name       | Register   | Field   | Type    | Description      |
|------------|------------|---------|---------|------------------|
| fid        | X0         | [63:0]  | UInt64  | Command FID      |
| params_ptr | X1         | [63:0]  | Address | PA of parameters |

## Context

The EXAMPLE\_ADD command operates on the following context.

| Name   | Type          | Value              | Before   | Description   |
|--------|---------------|--------------------|----------|---------------|
| params | ExampleParams | Params(params_ptr) | false    | Parameters    |

## Output values

| Name   | Register   | Field   | Type              | Description                    |
|--------|------------|---------|-------------------|--------------------------------|
| result | X0         | [15:0]  | CommandReturnCode | Command return status          |
| sum    | X1         | [63:0]  | UInt64            | Sum of x and y                 |
| zero   | X2         | [63:0]  | UInt64            | Whether either x or y was zero |

## Failure conditions

| ID           | Condition                                                                      |
|--------------|--------------------------------------------------------------------------------|
| params_align | pre: !AddrIsGranuleAligned(params_ptr) post: ResultEqual(result, ERROR_INPUT)  |
| params_gpt   | pre: Granule(params_ptr).gpt != GPT_NS post: ResultEqual(result, ERROR_MEMORY) |

## Success conditions

| ID   | Post-condition                                    |
|------|---------------------------------------------------|
| sum  | sum == params.x + params.y                        |
| zero | zero == (params.x == 0) &#124;&#124; (params.y == |

## B1.3 Command registers

DZDGNM An FID is a value which identifies a particular RMM command.

IMJQGK The FID of an RMM command is unique among the RMM commands in an RMM interface.

IRVPGY An FID is read from general-purpose register X0.

DXLSFS An input value is a value read by an RMM command from general-purpose registers.

DVCDCW An output value is a value written by an RMM command to general-purpose registers.

DCZLVJ A command return code is a value which specifies whether an RMM command succeeded or failed.

IFRZFT A command return code is written to general-purpose register X0.

## B1.4 Command condition expressions

DCHRYB A condition expression is an expression which evaluates to a boolean value.

IBNPKQ

ILTLQN

IYNDGD

DXBHPB

Following expansion of macros, a condition expression is a valid expression in Arm Specification Language (ASL). See also:

- Arm Specification Language Reference Manual [14]
- Chapter B3 Command condition functions

## B1.5 Command context values

- DDLBYC A context value is a value which is derived from the value of a command input register and which is used by a command condition expression.
- IVKKKY A context value can be thought of as a local variable for use by command condition expressions.

For example, consider the following example command condition expression:

!AddrIsGranuleAligned(RealmParams(params\_ptr).rtt\_base)

By introducing a context value params with the value RealmParams(params\_ptr) , this command condition expression can be re-written as:

!AddrIsGranuleAligned(params.rtt\_base)

- DQDFNW The before property of a context value indicates whether its expression is re-evaluated after the command has executed.
- before = true : the expression is not re-evaluated after the command has executed
- before = false : the expression is re-evaluated after the command has executed

Specifying before = true for a context value allows system state to be sampled before command execution, and then used after command execution in a command success condition.

For example, the RMI\_REALM\_DESTROY command takes as an input value the address rd of a Realm Descriptor. Successful execution of the command results observable effects including the following:

- The state of the RD Granule changes from RD to DELEGATED
- The state of the RTT base Granule, whose address was previously held in the RD, changes from RTT to DELEGATED

The address of the RTT base Granule is not included in the input values of the command.

A context value is defined as follows:

| Name     | Type    | Value              | Before   | Description      |
|----------|---------|--------------------|----------|------------------|
| rtt_base | Address | Realm(rd).rtt_base | true     | RTT base address |

The state change of the RTT Granule can then be expressed as:

Granule(rtt\_base).state == DELEGATED

The before property of a context value has no effect if the value is only used in command failure conditions.

An in-memory value is a value passed to a command via an in-memory data structure, the address of which is passed in an input register.

IZTYSS

An in-memory value is a context value.

See also:

- B4.3.9 RMI\_REALM\_CREATE command

## B1.6 Command failure conditions

- DDNQQC An RMM command failure condition defines a way in which the command can fail.

IGVBBZ A failure condition consists of a pre-condition and a post-condition

.

IWTSZH A failure pre-condition can be thought of as the 'trigger' of the failure: if the pre-condition is true then the command fails.

IKJHNX A failure post-condition can be thought of as the 'effect' of the failure: if the command failed due to a particular trigger, then the post-condition defines the error code which is returned.

ICVTGY A failure pre-condition is a condition expression whose terms can include input values and context values.

IHNDNN

A failure post-condition is a condition expression whose terms can include input values and context values.

- IKHJDY Observability of the checking of command failure conditions is subject to a partial order.

An ordering relation ' A precedes B ' means either of the following:

- The pre-condition of B is well-formed only if the pre-condition of A is false. This is referred to as a well-formedness ordering .
- If the pre-conditions of A and B are both true, then the post-condition of A is observed. This is referred to as a behavioral ordering .

The absence of an ordering relation ' A precedes B ' means that, if the pre-conditions of A and B are both true then either the post-condition of A is observed or the post-condition of B is observed.

Orderings are specified between groups of failure conditions. For example, the expression [A, B] &lt; [C, D] means that both conditions A and B precede both conditions C and D.

The same information is also presented graphically, with failure conditions represented as nodes and ordering relations represented as edges.

<!-- image -->

The specification does not state whether an individual ordering relation is a well-formedness ordering or a behavioral ordering.

- IJMTTY A given implementation of the RMM is expected to have deterministic behavior. That is, for a runtime instance of the RMM in a particular state, two executions of a command without an interleaving of other commands, with the same input values, results in the same outcome (either success, or the same failure condition.)
- RWXZJJ If a failure pre-condition evaluates to true then the corresponding failure post-condition evaluates to true.
- RDDGDW If a failure pre-condition evaluates to true then the command is aborted.
- RTFZMS If a command fails then all output values except for X0 are UNDEFINED, unless stated otherwise.
- RVHFHD If no failure pre-condition evaluates to true then the command succeeds.

## B1.7 Command success conditions

- DSZGNZ An RMM command success condition defines an observable effect of a successful execution of the command.
- ILZXHB A success condition is a condition expression whose terms can include input values, context values and output values.
- INMCSF The order in which success conditions are listed has no architectural significance.
- INJQFG If an RMM command succeeds then the return code is &lt;Interface&gt;\_SUCCESS.
- RMKRVV If an RMM command succeeds then all of its success conditions evaluate to true.

## B1.8 Concrete and abstract types

- DNXQWV A concrete type is a type which has a defined encoding.

Examples of concrete types include:

- An integer which has a defined bit width.
- An enumeration within which each label is associated with a unique binary value.
- A struct which has a defined width, and within which each member has a defined position. The type of each member of a concrete struct is a concrete type.
- IWDGMW Concrete types are used to define command input values and output values.
- DWTCVJ An abstract type is a type which does not have a defined encoding.

Examples of concrete types include:

- An integer which does not have a defined bit width.
- An enumeration which has a set of labels, but which does not define a binary value for each label.
- A struct which has a set of members, but which does not define a struct width nor a position for each member. The type of each member of an abstract struct is an abstract type.
- IQZRGY Abstract types are used to model the internal state of the RMM.

ILMKGP

A command failure condition or success condition may need to test for logical equality between a concrete type and a corresponding abstract type. For example, the command may set the value of an internal RMM variable to match the value of a command input. To enable such comparisons, the specification defines an Equal() function for each pair of corresponding concrete and abstract types.

See also:

- B3.17 Equal function

## B1.9 Command footprint

## Chapter B1. Commands B1.9. Command footprint

- DZDJDB The footprint of an RMM command defines the set of state items which successful execution of the command can modify.
- IXMZYS The footprint of an RMM command may include state items which are not modified by successful execution of the command.
- IRWQMJ If an RMM command changes the state of a Granule then the footprint typically does not include all attributes of the object which is created or destroyed.

For example, the footprint of RMI\_REALM\_CREATE includes the state of the RD Granule, but does not include attributes of the newly-created Realm.

- RWZYBV Except for items in the footprint of an RMM command and registers in the output values of the RMM command, execution of the command does not have any observable effects.