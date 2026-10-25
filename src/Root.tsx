import React from 'react';
import {AbsoluteFill, Audio, Composition, Easing, Img, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
export const ProductShot: React.FC = () => {
 const frame=useCurrentFrame(); const {fps}=useVideoConfig();
 return <AbsoluteFill style={{backgroundColor:'#161d25',fontFamily:'Arial, sans-serif',overflow:'hidden'}}>
 <AbsoluteFill style={{background:'radial-gradient(ellipse at 69% 42%, #303c48 0%, #1c2733 43%, #10161d 100%)'}}/>
 <div style={{position:'absolute',left:690,top:898,width:1100,height:74,borderRadius:'50%',background:'rgba(0,0,0,.46)',filter:'blur(30px)'}}/>
 <div style={{position:'absolute',left:660,top:90,width:1190,height:898,scale:interpolate(frame,[0,5.5*fps],[1,1.035],{extrapolateRight:'clamp',easing:Easing.bezier(.25,.1,.25,1)}),transformOrigin:'54% 58%'}}>
 <Img src={staticFile('pk3-hero.png')} style={{width:'100%',height:'100%',objectFit:'contain',filter:'brightness(1.015) contrast(1.015)'}}/>
 {frame>=Math.round(58/30*fps) && frame<=Math.round(90/30*fps) && <div style={{position:'absolute',inset:0,maskImage:`url(${staticFile('pk3-hero.png')})`,maskSize:'contain',maskPosition:'center',maskRepeat:'no-repeat',pointerEvents:'none',overflow:'hidden'}}>
 <div style={{position:'absolute',top:0,left:interpolate(frame,[58/30*fps,90/30*fps],[-1.45*1190,.45*1190],{extrapolateLeft:'clamp',extrapolateRight:'clamp',easing:Easing.bezier(.4,0,.2,1)}),width:2380,height:'100%',mixBlendMode:'screen',opacity:.28,
 background:'linear-gradient(115deg,transparent 36%,rgba(255,244,228,.06) 43%,rgba(255,244,228,.14) 47.5%,rgba(255,248,238,.5) 50%,rgba(255,244,228,.14) 52.5%,rgba(255,244,228,.06) 57%,transparent 64%)'}}/>
 </div>}
 </div>
 <div style={{position:'absolute',left:105,top:123,color:'#b6c5d0',fontSize:46,letterSpacing:4}}>BOROMOND</div>
 <div style={{position:'absolute',left:105,top:310,width:510,color:'#f1f4f5',opacity:interpolate(frame,[0,.65*fps],[0,1],{extrapolateRight:'clamp'})}}>
 <div style={{fontSize:91,fontWeight:500,letterSpacing:-3}}>PK3.0 <span style={{fontSize:54,color:'#8d9ba7',fontWeight:300}}>|</span></div>
 <div style={{marginTop:29,fontSize:48,lineHeight:1.38,fontWeight:400}}>Portable BDD<br/>Electro-Oxidation Kit</div>
 <div style={{marginTop:36,width:47,height:3,background:'#bc3e46'}}/>
 </div>
 <Sequence from={Math.round(.45*fps)} durationInFrames={Math.round(6.6*fps)} premountFor={fps}><Audio src={staticFile('pk3-voice.wav')} volume={1}/></Sequence>
 </AbsoluteFill>;
};
export const RemotionRoot: React.FC = () => <Composition id="PK3Hero" component={ProductShot} width={1920} height={1080} fps={30} durationInFrames={225}/>;

