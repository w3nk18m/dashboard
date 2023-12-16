import { Fragment, useCallback, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { Event, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, set_val, spreadArraysOrObjects, uploadFiles, useEventLoop } from "/utils/state"
import { ColorModeContext, EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import range from "/utils/helpers/range.js"
import "@glideapps/glide-data-grid/dist/index.css"
import "focus-visible/dist/focus-visible"
import { Avatar, Box, Button, Center, Container, Divider, Drawer, DrawerContent, DrawerOverlay, Heading, HStack, Image, Input, Link, Menu, MenuButton, MenuDivider, MenuItem, MenuList, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, Spacer, Text, VStack } from "@chakra-ui/react"
import { getEventURL } from "/utils/state.js"
import { ChevronDownIcon, CloseIcon, HamburgerIcon } from "@chakra-ui/icons"
import NextLink from "next/link"
import dynamic from "next/dynamic"
import { GridCellKind } from "@glideapps/glide-data-grid"
import { formatDataEditorCells } from "/utils/helpers/dataeditor.js"
import NextHead from "next/head"

const DataEditor = dynamic(() => import('@glideapps/glide-data-grid'), { ssr: false });


export default function Component() {
  const state = useContext(StateContext)
  const router = useRouter()
  const [ colorMode, toggleColorMode ] = useContext(ColorModeContext)
  const focusRef = useRef();
  
  // Main event loop.
  const [addEvents, connectError] = useContext(EventLoopContext)

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => addEvents(initialEvents())
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])

  
    const handleSubmitjoaaufna = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...{"역량": getRefValue(ref_역량), "평가요소": getRefValue(ref_평가요소), "주제": getRefValue(ref_주제), "목표": getRefValue(ref_목표)}}

        addEvents([Event("state.ability_grade_state.handle_register", {form_data:form_data})])

        if (false) {
            $form.reset()
        }
    })
    
  const ref_주제 = useRef(null); refs['ref_주제'] = ref_주제;
  const ref_평가요소 = useRef(null); refs['ref_평가요소'] = ref_평가요소;
  function getData_emoylmrw([col, row]){
    return formatDataEditorCells(col, row, state.ability_grade_state.table_col, state.ability_grade_state.table_data);
  }
  const ref_역량 = useRef(null); refs['ref_역량'] = ref_역량;
  const ref_목표 = useRef(null); refs['ref_목표'] = ref_목표;

  return (
    <Fragment>
  <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <Modal isOpen={connectError !== null}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Connection Error`}
</ModalHeader>
  <ModalBody>
  <Text sx={{"fontFamily": "Instrument Sans", "fontSize": 16}}>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {getEventURL().href}
</Text>
</ModalBody>
</ModalContent>
</ModalOverlay>
</Modal>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  <Box sx={{"fontFamily": "Instrument Sans"}}>
  <VStack spacing={`0`} sx={{"position": "sticky", "zIndex": "999", "top": "0", "width": "100%"}}>
  <Fragment>
  {isTrue(state.navbar_state.banner) ? (
  <Fragment>
  <Box sx={{"backgroundColor": "#110F1F", "paddingY": ["0.8em", "0.8em", "0.5em"], "width": "100%"}}>
  <HStack alignItems={`center`} sx={{"width": "100%", "paddingX": ["1em", "2em", "5em"]}}>
  <Center sx={{"width": "100%"}}>
  <Box sx={{"color": "#FFFFFF", "fontWeight": 600}}>
  {`✨ 역량 평가 Dashboard is in Hosting Alpha! ✨`}
</Box>
</Center>
  <Spacer/>
  <CloseIcon onClick={(_e) => addEvents([Event("state.navbar_state.toggle_banner", {})], (_e), {})} sx={{"color": "#FFFFFF", "textDecoration": "underline", "Hover": {"color": "#AD9BF8"}, "zIndex": 1000}}/>
</HStack>
</Box>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  <Box sx={{"bg": "rgba(255,255,255, 0.9)", "backdropFilter": "blur(10px)", "paddingY": ["0.8em", "0.8em", "0.5em"], "borderBottom": "1px solid #F4F3F6", "width": "100%"}}>
  <HStack justify={`space-between`} sx={{"paddingX": ["1em", "2em", "5em"]}}>
  <HStack spacing={`2em`}>
  <Link as={NextLink} href={`/`} sx={{"textDecoration": "none", "Hover": {}}}>
  <Image src={`/Reflex.svg`} sx={{"height": "1.25em"}}/>
</Link>
  <Menu>
  <MenuButton>
  <HStack sx={{"cursor": "pointer", "display": ["none", "none", "none", "flex", "flex", "flex"]}}>
  <Text sx={{"color": "#494369", "fontFamily": "Instrument Sans", "fontWeight": "600", "fontSize": 16}}>
  {`입력`}
</Text>
  <ChevronDownIcon sx={{"color": "#494369", "fontFamily": "Instrument Sans", "fontWeight": "600"}}/>
</HStack>
</MenuButton>
  <MenuList>
  <Link as={NextLink} href={`/input/subject_concept`} sx={{"textDecoration": "none", "Hover": {}}}>
  <MenuItem sx={{"color": "#494369", "fontFamily": "Instrument Sans", "fontWeight": "500", "Hover": {"color": "#5646ED", "bg": "#F5EFFE"}}}>
  {`교과 성취 기준`}
</MenuItem>
</Link>
  <Link as={NextLink} href={`/input/subject_grading_criteria`} sx={{"textDecoration": "none", "Hover": {}}}>
  <MenuItem sx={{"color": "#494369", "fontFamily": "Instrument Sans", "fontWeight": "500", "Hover": {"color": "#5646ED", "bg": "#F5EFFE"}}}>
  {`교과 채점 기준`}
</MenuItem>
</Link>
  <Link as={NextLink} href={`/input/ability_grading_criteria`} sx={{"textDecoration": "none", "Hover": {}}}>
  <MenuItem sx={{"color": "#494369", "fontFamily": "Instrument Sans", "fontWeight": "500", "Hover": {"color": "#5646ED", "bg": "#F5EFFE"}}}>
  {`역량 채점 기준`}
</MenuItem>
</Link>
  <MenuDivider/>
  <Link as={NextLink} href={`/input/subject_concept`} sx={{"textDecoration": "none", "Hover": {}}}>
  <MenuItem sx={{"color": "#494369", "fontFamily": "Instrument Sans", "fontWeight": "500", "Hover": {"color": "#5646ED", "bg": "#F5EFFE"}}}>
  {`학생 점수 입력`}
</MenuItem>
</Link>
</MenuList>
</Menu>
  <Menu>
  <MenuButton>
  <HStack sx={{"cursor": "pointer", "display": ["none", "none", "none", "flex", "flex", "flex"]}}>
  <Text sx={{"color": "#494369", "fontFamily": "Instrument Sans", "fontWeight": "600", "fontSize": 16}}>
  {`출력`}
</Text>
  <ChevronDownIcon sx={{"color": "#494369", "fontFamily": "Instrument Sans", "fontWeight": "600"}}/>
</HStack>
</MenuButton>
  <MenuList>
  <Link as={NextLink} href={`/output/subject_concept`} sx={{"textDecoration": "none", "Hover": {}}}>
  <MenuItem sx={{"color": "#494369", "fontFamily": "Instrument Sans", "fontWeight": "500", "Hover": {"color": "#5646ED", "bg": "#F5EFFE"}}}>
  {`교과 및 역량 기준`}
</MenuItem>
</Link>
  <Link as={NextLink} href={`/output/subject_concept`} sx={{"textDecoration": "none", "Hover": {}}}>
  <MenuItem sx={{"color": "#494369", "fontFamily": "Instrument Sans", "fontWeight": "500", "Hover": {"color": "#5646ED", "bg": "#F5EFFE"}}}>
  {`학생별 피드백`}
</MenuItem>
</Link>
  <Link as={NextLink} href={`/output/subject_concept`} sx={{"textDecoration": "none", "Hover": {}}}>
  <MenuItem sx={{"color": "#494369", "fontFamily": "Instrument Sans", "fontWeight": "500", "Hover": {"color": "#5646ED", "bg": "#F5EFFE"}}}>
  {`교과별 피드백`}
</MenuItem>
</Link>
</MenuList>
</Menu>
  <Menu>
  <MenuButton>
  <HStack sx={{"cursor": "pointer", "display": ["none", "none", "none", "flex", "flex", "flex"]}}>
  <Text sx={{"color": "#494369", "fontFamily": "Instrument Sans", "fontWeight": "600", "fontSize": 16}}>
  {`기타`}
</Text>
  <ChevronDownIcon sx={{"color": "#494369", "fontFamily": "Instrument Sans", "fontWeight": "600"}}/>
</HStack>
</MenuButton>
  <MenuList>
  <Link as={NextLink} href={`/changelog`} sx={{"textDecoration": "none", "Hover": {}}}>
  <MenuItem sx={{"color": "#494369", "fontFamily": "Instrument Sans", "fontWeight": "500", "Hover": {"color": "#5646ED", "bg": "#F5EFFE"}}}>
  {`성취기준`}
</MenuItem>
</Link>
</MenuList>
</Menu>
</HStack>
  <HStack sx={{"height": "full"}}>
  <Center sx={{"Hover": {"background": "radial-gradient(82.06% 100% at 50% 100%, rgba(91, 77, 182, 0.04) 0%, rgba(234, 228, 253, 0.2) 100%), #FEFEFF;", "boxShadow": "0px 0px 0px 3px rgba(149, 128, 247, 0.6), 0px 2px 3px rgba(3, 3, 11, 0.2), 0px 4px 8px rgba(3, 3, 11, 0.04), 0px 4px 10px -2px rgba(3, 3, 11, 0.02), inset 0px 2px 0px rgba(255, 255, 255, 0.01), inset 0px 0px 0px 1px rgba(32, 17, 126, 0.4), inset 0px -20px 12px -4px rgba(234, 228, 253, 0.36);"}, "boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14);", "display": ["none", "flex", "flex", "flex", "flex"], "height": "2em", "width": "2em", "borderRadius": "8px", "bg": "#FFFFFF"}}>
  <Avatar name={`Wan Kim`} size={`sm`}/>
</Center>
  <HamburgerIcon onClick={(_e) => addEvents([Event("state.navbar_state.toggle_sidebar", {})], (_e), {})} sx={{"width": "1.5em", "height": "1.5em", "Hover": {"cursor": "pointer", "color": "#5646ED"}, "display": ["flex", "flex", "flex", "none", "none", "none"]}}/>
</HStack>
</HStack>
</Box>
  <Drawer isOpen={state.navbar_state.sidebar_open} onClose={(_e) => addEvents([Event("state.navbar_state.toggle_sidebar", {})], (_e), {})} placement={`left`} sx={{"bg": "rgba(255,255,255, 0.5)"}}>
  <DrawerOverlay sx={{"bg": "rgba(255,255,255, 0.5)"}}>
  <DrawerContent sx={{"paddingX": "2em", "paddingTop": "2em", "bg": "rgba(255,255,255, 0.97)"}}>
  <HStack justify={`space-between`} sx={{"marginBottom": "1.5em"}}>
  <Link as={NextLink} href={`/`} sx={{"textDecoration": "none", "Hover": {}}}>
  <Image src={`/Reflex.svg`} sx={{"height": "1.25em"}}/>
</Link>
  <CloseIcon onClick={(_e) => addEvents([Event("state.navbar_state.toggle_sidebar", {})], (_e), {})} sx={{"width": "4em", "Hover": {"cursor": "pointer", "color": "#5646ED"}}}/>
</HStack>
  <Text sx={{"fontFamily": "Instrument Sans", "fontSize": 16}}>
  {`Sidebar`}
</Text>
</DrawerContent>
</DrawerOverlay>
</Drawer>
</VStack>
  <Container sx={{"flexDirection": "column", "maxWidth": "1800px"}}>
  <VStack alignItems={`stretch`} sx={{"minHeight": "80vh", "marginBottom": "4em", "paddingY": "2em"}}>
  <Box sx={{"textAlign": "left", "width": "100%"}}>
  <Heading sx={{"fontSize": ["2.2em", "2.4em", "2.5em"], "mt": 12, "mb": 4, "fontFamily": "Instrument Sans"}}>
  {`역량 채점 기준`}
</Heading>
  <Text sx={{"color": "#342E5C", "fontFamily": "Instrument Sans", "fontSize": 16}}>
  {`역량 채점 기준을 구성하기 위해 주제, 목표, 평가요소를 입력하세요.`}
</Text>
  <Divider sx={{"marginBottom": "1em", "marginTop": "0.5em"}}/>
</Box>
  <Box as={`form`} onSubmit={handleSubmitjoaaufna}>
  <VStack>
  <Input id={`주제`} placeholder={`주제`} ref={ref_주제} type={`text`}/>
  <Input id={`목표`} placeholder={`목표`} ref={ref_목표} type={`text`}/>
  <Input id={`평가요소`} placeholder={`평가요소`} ref={ref_평가요소} type={`text`}/>
  <Input id={`역량`} placeholder={`역량`} ref={ref_역량} type={`text`}/>
  <Button type={`submit`}>
  {`등록`}
</Button>
</VStack>
</Box>
  <Box sx={{"textAlign": "left", "width": "100%"}}>
  <Divider sx={{"marginBottom": "1em", "marginTop": "0.5em"}}/>
  <Heading sx={{"fontSize": ["2.2em", "2.4em", "2.5em"], "mt": 12, "mb": 4, "fontFamily": "Instrument Sans"}}>
  {`결과`}
</Heading>
  <Divider sx={{"marginBottom": "1em", "marginTop": "0.5em"}}/>
</Box>
  <Box sx={{"textAlign": "left", "width": "100%"}}>
  <Button onClick={(_e) => addEvents([Event("state.ability_grade_state.handle_clear", {})], (_e), {})}>
  {`빈 줄 삭제`}
</Button>
</Box>
  <Box sx={{"width": "100%"}}>
  <div style={{"width": "100%", "height": "100vh"}} sx={{"width": "100%", "height": "100vh"}}>
  <DataEditor columnSelect={`multiple`} columns={state.ability_grade_state.table_col} data={state.ability_grade_state.table_data} drawFocusRing={true} getCellContent={getData_emoylmrw} getCellForSelection={true} onCellEdited={(_pos,_data) => addEvents([Event("state.ability_grade_state.handle_update", {pos:_pos,new_vaule:_data})], (_pos,_data), {})} onPaste={true} rowHeight={40} rowMarkers={`both`} rows={state.ability_grade_state.table_data.length} smoothScrollX={true} smoothScrollY={true} sx={{"height": "100vh"}}/>
</div>
</Box>
</VStack>
</Container>
  <Box sx={{"boxShadow": "medium-lg", "borderTop": "0.1em solid #82799E", "verticalAlign": "bottom", "paddingTop": "2em", "paddingBottom": "2em", "paddingX": ["1em", "2em", "10em"], "bg": "#110F1F"}}>
  <VStack>
  <HStack justify={`space-between`} sx={{"color": "#94a3b8", "paddingBottom": "2em", "minWidth": "100%"}}>
  <Text sx={{"fontFamily": "Instrument Sans", "fontWeight": "500", "Hover": {"color": "#82799E"}, "fontSize": 16}}>
  {`Copyright © 2024 창덕여자중학교`}
</Text>
  <HStack spacing={`1em`}>
  <Link as={NextLink} href={`https://github.com/reflex-dev/reflex`} sx={{"textDecoration": "none", "Hover": {}}}>
  <Image src={`/companies/light/github.svg`} sx={{"height": "1.75em"}}/>
</Link>
  <Link as={NextLink} href={`https://www.linkedin.com/company/reflex-dev`} sx={{"textDecoration": "none", "Hover": {}}}>
  <Image src={`/companies/light/linkedin.svg`} sx={{"height": "1.75em"}}/>
</Link>
  <Link as={NextLink} href={`https://www.ycombinator.com/companies/reflex`} sx={{"textDecoration": "none", "Hover": {}}}>
  <Image src={`/companies/light/yc.svg`} sx={{"height": "1.75em"}}/>
</Link>
  <Link as={NextLink} href={`https://twitter.com/getreflex`} sx={{"textDecoration": "none", "Hover": {}}}>
  <Image src={`/companies/light/twitter.svg`} sx={{"height": "1.75em"}}/>
</Link>
  <Link as={NextLink} href={`https://discord.gg/T5WSbC2YtQ`} sx={{"textDecoration": "none", "Hover": {}}}>
  <Image src={`/companies/light/discord.svg`} sx={{"height": "1.75em"}}/>
</Link>
</HStack>
</HStack>
</VStack>
</Box>
</Box>
  <NextHead>
  <title>
  {`Reflex | 입력`}
</title>
  <meta content={`Keep up to date with the latest Reflex news.`} name={`description`}/>
  <meta content={`/previews/blog_preview.png`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
