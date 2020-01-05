import React from 'react'
import "./styles.scss"
import FavoriteIcon from '@material-ui/icons/Favorite'
import FavoriteBorderIcon from '@material-ui/icons/FavoriteBorder';
import { useSelector } from 'react-redux'

export default function Hearts() {
    const life = useSelector(state => state.data.life)
    let hearts = []

    for (let i = 1; i < 4; i++) {
        if (i <= life) {
            hearts.push(<FavoriteIcon className="heart_filled" style={{ fontSize: 60 }}/>)
        } else {
            hearts.push(<FavoriteBorderIcon className="heart_empty" style={{ fontSize: 60 }}/>)
        }
      }


    return (
        <>
        {
            hearts
        }
        </>
    )
}