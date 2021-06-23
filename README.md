## Features

The main feature of this project is to compute the molecular mass of a given molecule and a given data base of element mass.

The element mass data base is described by a simple json file.

## Ultimate features & Current status

The ultimate goals of the project aims to provide a rich syntax to express any molecule.

##### Isotopes

Current version only support simple molecules without isotopes. But the feature is among the final objectives.

##### Free syntax

Currently all elements should be fully indexed, for example CH4 is not allowed but C1H4 is allowed.

I will later add the support for a more 'natural' syntax to support a more free syntax, with more precise syntactic analysis 
indicating readable error to help user.

In fact, the name (case-insensitive) of all discovery elements is not a LL(2) language. However, without some rare cases, it may form a LL(2) language.

So i will add several mode: fully indexed, free but case-sensitive, or case-insensitive without some elements.

List of not supported elements in case-insensitive mode:
Si, Sc, Co, Ni, Cu, Nb, In, Sn, Sb, Cs, Hf, Os, Pb, Bi, Po, Bh, Hs, Cn, Nh, 
Ho, Yb, Np, Pu, Bk, Cf, No.

The case-sensitive mode will be the default mode.