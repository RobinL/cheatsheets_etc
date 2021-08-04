## Getting started

When you go into a typescript project, you need to run 
`yarn --frozen-lockfile`
This installs all the 'things' needed for typescript to work.

The thing I struggled over was how to debug typescript files, especially if you just want to run them and set breakpoints without compiling.

You want to make sure you're running the latest version of node as well - otherwise some newer syntax doesn't seem to work.

## Debugging
https://medium.com/hackernoon/debugging-javascript-typescript-node-apps-with-chrome-devtools-vs-code-and-webstorm-97b882aee0ad

The key bit is that `ts-node` is needed, you can't just run a `.ts` file using node.

in `launch.json`:

```
 {
      "name": "Current TS File",
      "type": "node",
      "request": "launch",
      "program": "${workspaceRoot}/node_modules/.bin/ts-node",
      "args": [
        "${relativeFile}"
      ],
      "protocol": "inspector"
    },
```

or
in launch.json
```
    {
      "type": "node",
      "request": "launch",
      "name": "Launch via NPM",
      "runtimeExecutable": "npm",
      "runtimeArgs": [
        "run-script",
        "start:debug:ts:brk"
      ],
      "port": 9229
    },

```
in package.json. (change `myfile.ts` to the script you want to run.  There'd probably be a way of passing in a reference to the curretly active file.
```
"scripts": {
    "start:debug:ts:brk": "node --inspect-brk --require ts-node/register myfile.ts",
```

The later seems to work better.



