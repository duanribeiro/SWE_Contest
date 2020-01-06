import React from 'react'
import "./styles.scss"
import Typewriter from 'typewriter-effect';


export default function TextBox(props) {

    return (
        <>
            <Typewriter
            onInit={(typewriter) => {
                typewriter
                .changeDelay(20)
                .typeString(props.stage)
                .stop()
                .start();
            }}
            />
        </>
    )
}