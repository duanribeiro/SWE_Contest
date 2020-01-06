import React from 'react'
import Typewriter from 'typewriter-effect';


export default function TextBox() {

    const text_1 = 
    '<span style="color: black; font-family: Courier New; font-size: 250%;"> \
        You came on time! \
    </span> \
    <br/> \
    <br/> \
    <span style="color: black; font-family: Courier New; font-size: 250%;"> \
        It will start shortly, get in the car now and I explain more on the way. \
    </span>'

    return (
        <>
            <Typewriter
            onInit={(typewriter) => {
                typewriter
                .changeDelay(10)
                .typeString(text_1)
                .stop()
                .start();
            }}
            />
        </>
    )
}