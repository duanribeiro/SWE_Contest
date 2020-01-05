import React from 'react'
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Grid from '@material-ui/core/Grid';



import Hearts from './../Hearts'
import Clock from './../Clock'
import TextBox from './../TextBox'
import CardAction from './../CardAction'

import "./styles.scss";

export default function MainWindow() {

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
                                <TextBox/>
                            </div>
                        </Grid>

                        {/* ACTIONS (BOTTOM) */}
                        <Grid
                        container
                        direction="column"
                        justify="center"
                        alignItems="stretch"
                        >   
                            <CardAction/>
                        </Grid>
                    </Grid>
                </CardContent>
            </Card>
        </>
    )
}