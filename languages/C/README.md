# All things C lives here
## Compiling
compiling hello-world.c to a file called hello 
```sh
	cc -o hello hello-world.c
```
## I/O
* puts -- simplest way to output strings
* printf -- user-supplied data as first agrument secuirty vuln Seacord 2013
## Escape Sequences
* \n -- new line
## Portability
### Issues
* Implementation-defined behavior
program behavior that is not specified by the C Standard. different results can occur among implementations. behavior is constent. **example:** number of bits in byte.
* Unspecified behavior
* Undefined behavior
* Locale-specific behavior
* Common extensions
