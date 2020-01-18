import React, {useEffect, useState} from 'react'
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Grid from '@material-ui/core/Grid';


import axios from 'axios';

import Hearts from './../Hearts'
import Clock from './../Clock'
import TextBox from './../TextBox'
import CardAction from './../CardAction'

import "./styles.scss";

export default function MainWindow() {

    const [actions, setActions ] = useState([]) 
    const [stage, setStage ] = useState()

    const fetchStage = stage_name => {
        axios.post(`${process.env.REACT_APP_BACKEND_API}/api/v1/game`, {"name": stage_name})
        .then(response => {
            setActions(response.data.actions)
            setStage(response.data.text)
        })
        .catch(error => {
            console.error(error.message)
        })
    }

    useEffect( () => { fetchStage("introduction_0") }, [] )

    let textbox = <></>
    if (stage) {
        textbox =  <TextBox stage={stage}/>
    }
    return (
        <>
            <Card
            className="outer_card"
            >
                <CardContent>
                    <Grid
                    container
                    direction="column"
                    justify="center"
                    alignItems="center"
                    >
                        {/* STATS (TOP) */}
                        <Grid
                        container
                        direction="row"
                        justify="space-between"
                        alignItems="center"
                        >
                            <Grid
                            item
                            >
                                <Hearts/>
                            </Grid>
                            <Grid
                            item
                            >
                                <Clock/>
                            </Grid>
                        </Grid>

                        {/* TEXTBOX (MIDDLE) */}
                        <Grid
                        item
                        >
                            <div className="middle_card">
                                {
                                    textbox
                                }
                            </div>
                        </Grid>

                        {/* ACTIONS (BOTTOM) */}
                        <Grid
                        container
                        direction="column"
                        justify="center"
                        alignItems="stretch"
                        >   
                            <CardAction actions={actions} fetchStage={fetchStage} setStage={setStage}/>
                        </Grid>
                    </Grid>
                </CardContent>
            </Card>
        </>
    )
}