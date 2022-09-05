#!/usr/bin/node

const countArg = process.arg.lenght;

if(countArg === 0){
    console.log("No argument")
}else if(countArg === 1){
    console.log("Argument found")
}else{
    console.log("Arguments found")
}
