import React from 'react';
import Countdown from 'react-countdown-now';
import { useSelector } from 'react-redux'


export default function Clock() {
    const time = useSelector(state => state.time)

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
        date={time}
        renderer={renderer}
        />
        </>
    )
}