import React from 'react';
import Countdown from 'react-countdown-now';


export default function Clock() {

    const Completed = () => <span>You are good to go!</span>
 
    const renderer = ({ hours, minutes, seconds, completed }) => {
    if (completed) {
        return <Completed />
    } else {
        if (seconds >= 10) {
            return (
                <>
                    <span style={{"fontSize": 70, "fontFamily": "Iceberg", "paddingRight": "10px"}}>{minutes}:{seconds}</span>
                </>
            )
        } else {
            return (
                <>
                    <span style={{"fontSize": 70, "fontFamily": "Iceberg", "paddingRight": "10px"}}>{minutes}:0{seconds}</span>
                </>
            )
        }
       
    }
    }

    return (
        <>
        <Countdown
        date={Date.now() + 500000}
        renderer={renderer}
        />
        </>
    )
}