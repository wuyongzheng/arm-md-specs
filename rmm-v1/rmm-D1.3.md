## D1.3 Realm exception model flows

This section contains flows which relate to the Realm exception model.

See also:

- Chapter A4 Realm exception model

## D1.3.1 Realm entry and exit flow

The following diagram shows how a Realm is executed, and illustrates the different reasons for exiting the Realm and returning control to the Host.

A REC is entered using the RMI\_REC\_ENTER command. The parameters to this command include:

- an RmiRecEnter object , which is a data structure used to pass values from the Host to the RMM on REC entry
- an RmiRecExit object , which is a data structure used to pass values from the RMM to the Host on REC exit

<!-- image -->

## See also:

- Chapter A4 Realm exception model
- D1.3.2 Host call flow
- D1.3.3 REC exit due to Data Abort fault flow
- D1.3.4 MMIO emulation flow

## D1.3.2 Host call flow

The following diagram shows how software executing inside the Realm can voluntarily yield control back to the Host by making a Host call.

A REC is entered using the RMI\_REC\_ENTER command. The parameters to this command include:

- an RmiRecEnter object , which is a data structure used to pass values from the Host to the RMM on REC entry
- an RmiRecExit object , which is a data structure used to pass values from the RMM to the Host on REC exit

On execution of RSI\_HOST\_CALL, arguments are copied from the RsiHostCall object in Realm memory into the RmiRecExit object in NS memory. On the subsequent RMI\_REC\_ENTER, return values are copied from the RmiRecEnter object in NS memory into the RsiHostCall object in Realm memory.

<!-- image -->

See also:

- A4.5 Host call

## D1.3.3 REC exit due to Data Abort fault flow

The following diagram shows how a Data Abort due to a Realm access is taken to the Host.

A REC is entered using the RMI\_REC\_ENTER command. The parameters to this command include:

- an RmiRecEnter object , which is a data structure used to pass values from the Host to the RMM on REC entry
- an RmiRecExit object , which is a data structure used to pass values from the RMM to the Host on REC exit

## D1.3. Realm exception model flows

<!-- image -->

See also:

- Chapter A4 Realm exception model

## D1.3.4 MMIO emulation flow

The following diagram shows how an MMIO access by a Realm can be emulated by the Host.

Chapter D1. Flows

## D1.3. Realm exception model flows

<!-- image -->

## See also:

- Chapter A4 Realm exception model