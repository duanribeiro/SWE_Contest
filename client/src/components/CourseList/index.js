import React from 'react'
import { useSelector, useDispatch } from 'react-redux'

export default function CourseList() {
    const courses = useSelector(state => state.data)
    const dispatch = useDispatch(state => state.data)

    function addCourse() {
        dispatch({type: 'ADD_COURSE', title: 'GRAPHQL'})
    }
    return (
        <>
            <ul>
                {courses.map(course => <li key={course}>{course}</li>)}
            </ul>
            <button type='button' onClick={addCourse}>
                Adicionar Curso
            </button>
        </>
    )
}